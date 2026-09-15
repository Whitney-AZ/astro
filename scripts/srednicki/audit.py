"""Check the built articles; keep mechanical checks distinct from editorial review."""
from collections import Counter
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[2]
CHECKS = ROOT / 'checks/srednicki'


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.links, self.images, self.errors = [], [], [], []
        self.math = 0
        self.red_math_depth = 0
        self.red_math_text = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.red_math_depth:
            self.red_math_depth += 1
        elif tag == 'mstyle' and attrs.get('mathcolor', '').lower() == '#cc0000':
            self.red_math_depth = 1
            self.red_math_text = []
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag == 'img' and attrs.get('src'):
            self.images.append(attrs['src'])
        if 'katex-error' in attrs.get('class', ''):
            self.errors.append(attrs.get('title', 'KaTeX error'))
        if tag == 'math':
            self.math += 1

    def handle_data(self, data):
        if self.red_math_depth:
            self.red_math_text.append(data)

    def handle_endtag(self, tag):
        if self.red_math_depth:
            self.red_math_depth -= 1
            if not self.red_math_depth:
                command = ''.join(self.red_math_text).strip()
                if command.startswith('\\'):
                    self.errors.append(f'Unsupported KaTeX command: {command}')


def main():
    problems, records = [], []
    pages = {}
    manifest = json.loads((CHECKS / 'source-manifest.json').read_text())
    for record in manifest['sections']:
        digest = sha256((ROOT / record['source']).read_bytes()).hexdigest()
        if digest != record['source_sha256']:
            problems.append({'source_changed': record['source']})
    for i in range(1, 98):
        source = ROOT / f'src/content/posts/Srednicki-{i:02}.md'
        built = ROOT / f'dist/posts/srednicki-{i:02}/index.html'
        if not source.exists() or not built.exists():
            problems.append({'missing_section': i})
            continue
        text = source.read_text()
        if not re.search(rf'srednickiSections:\s*\[{i}\]', text):
            problems.append({'section_mapping': i})
        if re.search(r'draft:\s*true', text):
            problems.append({'draft': i})
        for marker in ('【待核对', 'TODO', 'TBD', '\\input{', '\\eqref{', '\\label{', '{=latex}'):
            if marker in text:
                problems.append({'section': i, 'unconverted': marker})
        citations = list(re.finditer(r'\[@[^\]]+\]', text))
        for citation in citations:
            problems.append({'section': i, 'unresolved_citation': citation.group()})
        # Pandoc also allows bare citation keys (for example @Author2017Title).
        for citation in re.finditer(r'(?<![\w@])@[A-Z][A-Za-z0-9_-]*\d[A-Za-z0-9_-]*', text):
            if not any(c.start() <= citation.start() < c.end() for c in citations):
                problems.append({'section': i, 'unresolved_citation': citation.group()})
        if re.search(r'^:::', text, re.M):
            problems.append({'section': i, 'unconverted': 'Pandoc fenced div'})
        if re.search(r'^\[\](?=<span\b)', text, re.M):
            problems.append({'section': i, 'unconverted': 'Empty reference brackets'})
        if source.stat().st_mtime_ns > built.stat().st_mtime_ns:
            problems.append({'section': i, 'built_html_stale': True})
        page = Page(built)
        pages[built] = page
        problems.extend({'section': i, 'math_error': error} for error in page.errors)
        problems.extend({'section': i, 'duplicate_id': anchor} for anchor, count in Counter(page.ids).items() if count > 1)
        # A math-bearing manuscript must not silently become plain TeX.
        if i > 1 and page.math < text.count('\\tag{'):
            problems.append({'section': i, 'math_count_below_tag_count': page.math})
        records.append({'section': i, 'post_sha256': sha256(source.read_bytes()).hexdigest(),
                        'html_sha256': sha256(built.read_bytes()).hexdigest(),
                        'rendered_math': page.math, 'images': len(page.images)})
    for path, page in list(pages.items()):
        for href in page.links + page.images:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            if not url.path:
                target = path
            elif url.path.startswith('/'):
                target = ROOT / 'dist' / unquote(url.path.lstrip('/'))
            else:
                target = path.parent / unquote(url.path)
            if target.is_dir():
                target /= 'index.html'
            if not target.exists():
                problems.append({'page': path.parent.name, 'missing_link_or_image': href})
                continue
            if url.fragment and target.suffix == '.html':
                if target not in pages:
                    pages[target] = Page(target)
                if unquote(url.fragment) not in pages[target].ids:
                    problems.append({'page': path.parent.name, 'missing_anchor': href})
    reviews = []
    for entry in manifest['sections']:
        if entry['editorial_review'] != 'complete':
            continue
        review_path = ROOT / entry.get('review_record', '')
        if not review_path.is_file():
            problems.append({'section': entry['section'], 'review_record_missing': True})
            continue
        current_hash = sha256((ROOT / entry['post']).read_bytes()).hexdigest()
        if current_hash == entry.get('review_post_sha256'):
            reviews.append(entry['section'])
        else:
            problems.append({'section': entry['section'], 'review_stale': True})
    report = {'mechanical_pass': not problems, 'sections': records, 'problems': problems,
              'editorial_completed': reviews,
              'editorial_pending': [i for i in range(2, 98) if i not in reviews],
              'scope': 'HTML math, local links, assets, section metadata, source hashes. Physics and prose require recorded reading.'}
    (CHECKS / 'build-audit.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'pages': len(records), 'math': sum(r['rendered_math'] for r in records),
                      'problems': problems, 'editorial_complete': len(reviews)}, ensure_ascii=False, indent=2))
    raise SystemExit(bool(problems))


if __name__ == '__main__':
    main()
