"""Render the saved, original TikZ drawings as self-contained SVG assets."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
FIGURES = ROOT / 'checks/srednicki/figures.json'
PREAMBLE = r'''\documentclass[tikz,border=6pt]{standalone}
\usepackage{amsmath,amssymb,slashed}
\newcommand{\symbf}[1]{\boldsymbol{#1}}
\usepackage{xeCJK}
\setCJKmainfont{Songti SC}
\usetikzlibrary{decorations.pathmorphing,decorations.markings,arrows.meta,calc,positioning}
\begin{document}
'''


def render(entry):
    source, output = ROOT / entry['source'], ROOT / entry['output']
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='srednicki-figure-') as temp:
        work = Path(temp)
        if source.suffix == '.pdf':
            pdf = source
        else:
            tex = work / 'figure.tex'
            tex.write_text(PREAMBLE + source.read_text() + '\n\\end{document}\n')
            result = subprocess.run(['xelatex', '-no-shell-escape', '-interaction=nonstopmode',
                                     '-halt-on-error', 'figure.tex'], cwd=work,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if result.returncode:
                log = ROOT / 'checks/srednicki' / (output.stem + '.log')
                log.write_text(result.stdout)
                return {'source': entry['source'], 'error_log': str(log.relative_to(ROOT))}
            pdf = work / 'figure.pdf'
        result = subprocess.run(['pdftocairo', '-svg', str(pdf), str(output)],
                                capture_output=True, text=True)
        if result.returncode:
            return {'source': entry['source'], 'error': result.stderr}
        return {'output': entry['output'], 'sha256': hashlib.sha256(output.read_bytes()).hexdigest()}


if __name__ == '__main__':
    entries = json.loads(FIGURES.read_text())
    unique = {entry['output']: entry for entry in entries}
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(render, unique.values()))
    (ROOT / 'checks/srednicki/figure-render.json').write_text(json.dumps(results, indent=2) + '\n')
    failed = [r for r in results if 'output' not in r]
    print(f'Rendered {len(results)-len(failed)}/{len(results)} figures.')
    for result in failed:
        print(result)
    raise SystemExit(bool(failed))
