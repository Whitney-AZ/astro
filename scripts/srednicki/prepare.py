"""One-time conversion of the supplied chapters into editable Astro posts.

Existing posts are never overwritten. Subsequent editorial work belongs in posts/.
The PDF is read locally; neither it nor its extracted text is published.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import unicodedata

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
POSTS = ROOT / 'src/content/posts'
CHECKS = ROOT / 'checks/srednicki'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def number(tag):
    return re.sub(r'C0?(\d+)\.0*(\d+)', r'\1.\2', tag)


def macro(text, command, replacement):
    """Replace a braced TeX command, including nested braces in its argument."""
    pattern = re.compile(re.escape('\\' + command) + r'\{')
    while match := pattern.search(text):
        start = end = match.end()
        depth = 1
        while depth and end < len(text):
            if text[end] == '{' and text[end-1] != '\\':
                depth += 1
            elif text[end] == '}' and text[end-1] != '\\':
                depth -= 1
            end += 1
        if depth:
            raise ValueError(f'Unclosed {command}')
        text = text[:match.start()] + replacement(text[start:end-1]) + text[end:]
    return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--figure-origin', type=Path, required=True)
    args = parser.parse_args()
    if (CHECKS / 'source-manifest.json').exists():
        parser.error('The import already exists. Edit posts directly; do not overwrite the editorial manifests.')
    CHECKS.mkdir(parents=True, exist_ok=True)
    source = ROOT / '量子场论（Srednicki中译本）.pdf'
    pdf = subprocess.check_output(['pdftotext', '-layout', str(source), '-'], text=True)
    pages = pdf.split('\f')
    titles = []
    for page, body in enumerate(pages, 1):
        if page < 14:
            continue
        match = re.search(r'^\s*第[一二三四五六七八九十百]+节\s+(.+)$', body, re.M)
        if match:
            titles.append((page, unicodedata.normalize('NFKC', match[1].strip())))
    assert len(titles) == 97, len(titles)
    texts = {i: (ROOT / f'chapters/{i:02}.md').read_text() for i in range(1, 98)}
    anchors, equations = {}, {}
    for i, body in texts.items():
        for anchor in re.findall(r'\{#([^}]+)\}', body):
            anchors[anchor] = i
        for math in re.findall(r'\$\$(.*?)\$\$', body, re.S):
            tag = re.search(r'\\tag\{([^}]+)\}', math)
            if tag:
                for label in re.findall(r'\\label\{([^}]+)\}', math):
                    equations[label] = (i, number(tag[1]))
                    anchors[label] = i
        for label in re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}', body):
            anchors[label] = i

    assets, manifest, missing = [], [], []
    for i, original in texts.items():
        path = POSTS / f'Srednicki-{i:02}.md'
        if path.exists():
            continue
        body = original.split('\n', 1)[1].strip()
        title = titles[i-1][1]
        body = re.sub(r'^```(?:\{=latex\})?\s*$', '', body, flags=re.M)

        def asset(match):
            name = match[1]
            local = Path(name).relative_to('notes/figures')
            origin = args.figure_origin / local
            assert origin.is_file(), origin
            saved = HERE / 'figure-sources' / local
            saved.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(origin, saved)
            slug = '-'.join(local.with_suffix('').parts)
            assets.append({'chapter': i, 'source': str(saved.relative_to(ROOT)),
                           'sha256': digest(saved), 'output': f'public/images/srednicki/{slug}.svg'})
            return f'\n\n![第 {i} 节的场论图示](/images/srednicki/{slug}.svg)\n\n'

        body = re.sub(r'\\input\{([^}]+)\}', asset, body)
        body = re.sub(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', asset, body)
        inline = 0

        def tikz(match):
            nonlocal inline
            inline += 1
            slug = f'{i:02}-inline-{inline}'
            saved = HERE / f'figure-sources/{slug}.tex'
            saved.parent.mkdir(parents=True, exist_ok=True)
            saved.write_text(match[0] + '\n')
            assets.append({'chapter': i, 'source': str(saved.relative_to(ROOT)),
                           'sha256': digest(saved), 'output': f'public/images/srednicki/{slug}.svg'})
            return f'\n\n![第 {i} 节的场论图示](/images/srednicki/{slug}.svg)\n\n'

        body = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', tikz, body, flags=re.S)
        body = macro(body, 'caption', lambda text: '\n\n' + text + '\n\n')
        body = re.sub(r'\\renewcommand\{\\thefigure\}\{[^}]+\}', '', body)
        body = re.sub(r'\\(?:begin|end)\{(?:center|figure|minipage)\}(?:\[[^\]]*\])?(?:\{[^}]+\})?', '', body)
        body = re.sub(r'\\Needspace\{[^}]+\}|\\(?:centering|phantomsection|smallskip)\b', '', body)
        body = re.sub(r'\\hypertarget\{([^}]+)\}\{\}', lambda m: f'<span id="{m[1]}"></span>', body)
        body = re.sub(r'\{\\(?:small|footnotesize)\s+(.*?)\}', r'\1', body, flags=re.S)
        body = re.sub(r'\\(?:small|footnotesize|par)\b', '', body)

        def heading(match):
            return f'<span id="{match[3]}"></span>\n\n{match[1]} {match[2].strip()}'

        body = re.sub(r'^(#{1,6})\s+(.+?)\s+\{#([^}]+)\}\s*$', heading, body, flags=re.M)
        body = re.sub(r'\{#([^}]+)\}', lambda m: f'<span id="{m[1]}"></span>', body)

        def display(match):
            math = match[1]
            labels = re.findall(r'\\label\{([^}]+)\}', math)
            math = re.sub(r'\\label\{[^}]+\}', '', math)
            math = re.sub(r'\\tag\{([^}]+)\}', lambda m: '\\tag{' + number(m[1]) + '}', math)
            return '\n'.join(f'<span id="{label}"></span>' for label in labels) + '\n\n$$' + math + '$$'

        body = re.sub(r'\$\$(.*?)\$\$', display, body, flags=re.S)

        def eqref(match):
            label = match[1]
            if label in equations:
                chapter, tag = equations[label]
                href = f'#{label}' if chapter == i else f'/posts/srednicki-{chapter:02}/#{label}'
                if chapter == 1:
                    missing.append({'chapter': i, 'kind': 'existing-post-equation', 'target': label})
                    href = '/posts/srednicki-01/'
                return f'[（{tag}）]({href})'
            missing.append({'chapter': i, 'kind': 'equation', 'target': label})
            return f'【待核对公式：{label}】'

        body = re.sub(r'\\eqref\{([^}]+)\}', eqref, body)
        body = re.sub(r'\\ref\{([^}]+)\}', lambda m: f'[图示](#{m[1]})' if anchors.get(m[1]) == i else eqref(m), body)
        body = re.sub(r'\\label\{([^}]+)\}', lambda m: f'<span id="{m[1]}"></span>', body)

        def link(match):
            label, href = match[1], match[2]
            if href.startswith('/'):  # Already converted equation or image.
                return match[0]
            if '#' not in href:
                return match[0]
            anchor = href.split('#')[-1]
            if anchor in anchors:
                chapter = anchors[anchor]
                dest = f'#{anchor}' if chapter == i else f'/posts/srednicki-{chapter:02}/#{anchor}'
                if chapter == 1:
                    dest = '/posts/srednicki-01/'
                return f'[{label}]({dest})'
            missing.append({'chapter': i, 'kind': 'supporting-reference', 'target': href, 'text': label})
            return label

        body = re.sub(r'\[([^\]\n]+)\]\(([^)\n]+)\)', link, body)
        body = re.sub(r'第(\d+)章', r'第\1节', body).replace('上一章', '上一节').replace('下一章', '下一节').replace('本章', '本节').replace('章末', '节末')
        body = re.sub(r'图C0?(\d+)', r'图\1', body)
        body = re.sub(r'\n{3,}', '\n\n', body).strip()
        front = ('---\n' + f'title: "Srednicki §{i} {title}"\n' +
                 'date: 2026-09-14\ncategory: 笔记\ntags: [物理, 量子场论, Srednicki]\n' +
                 f'series: "Srednicki QFT"\nsrednickiSections: [{i}]\nhideFromHome: true\ndraft: false\n---\n\n')
        navigation = f'[← 第 {i-1} 节](/posts/srednicki-{i-1:02}/) · [章节地图](/srednicki/)'
        if i < 97:
            navigation += f' · [第 {i+1} 节 →](/posts/srednicki-{i+1:02}/)'
        path.write_text(front + f'<span id="c{i:02}"></span>\n\n' + body + '\n\n---\n\n' + navigation + '\n')
        manifest.append({'section': i, 'title': title, 'source': f'chapters/{i:02}.md',
                         'source_sha256': digest(ROOT / f'chapters/{i:02}.md'),
                         'pdf_pages': [titles[i-1][0], titles[i][0]-1 if i < 97 else 410],
                         'post': str(path.relative_to(ROOT)), 'editorial_review': 'pending'})
    (CHECKS / 'source-manifest.json').write_text(json.dumps({'pdf_sha256': digest(source), 'sections': manifest}, ensure_ascii=False, indent=2) + '\n')
    (CHECKS / 'conversion-references.json').write_text(json.dumps(missing, ensure_ascii=False, indent=2) + '\n')
    (CHECKS / 'figures.json').write_text(json.dumps(assets, ensure_ascii=False, indent=2) + '\n')
    print(f'Created {len(manifest)} posts, {len(assets)} figures, {len(missing)} references for editorial review.')


if __name__ == '__main__':
    main()
