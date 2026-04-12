import os
import re

files = [
    '/Users/whitney/astro-blog/astro/src/content/posts/raq.md',
    '/Users/whitney/astro-blog/astro/src/content/posts/RAQexamples.md',
    '/Users/whitney/astro-blog/astro/src/content/posts/diracGR.md'
]

latex_header = r"""\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath, amssymb, amsfonts}
\usepackage{geometry}
\geometry{a4paper, margin=1in}
\usepackage{hyperref}

\title{LQG Notes}
\author{Whitney}
\date{Compiled: 2026-04-12}

\begin{document}
\maketitle
\tableofcontents

"""

latex_footer = r"""
\end{document}
"""

def md_to_latex(md_text, title):
    # Remove frontmatter
    md_text = re.sub(r'^---\n.*?\n---\n', '', md_text, flags=re.DOTALL)
    
    # section title
    out = f"\\section{{{title}}}\n\n"
    
    # Convert headings
    md_text = re.sub(r'^### (.*?)$', r'\\subsection{\1}', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^## (.*?)$', r'\\subsection{\1}', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^#### (.*?)$', r'\\subsubsection{\1}', md_text, flags=re.MULTILINE)
    
    # Convert bold
    md_text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', md_text)
    
    # Specific italic replacements to avoid breaking math
    md_text = md_text.replace("_-representation", "$*$-representation")
    md_text = md_text.replace("_-operations", "$*$-operations")
    md_text = md_text.replace("_strong_", "\\emph{strong}")
    md_text = md_text.replace("_weak_", "\\emph{weak}")
    
    # Blockquotes
    def replace_blockquote(match):
        lines = match.group(1).split('\n')
        clean_lines = [line.lstrip('> ').strip() for line in lines if line.strip()]
        return "\\begin{quote}\n" + "\n".join(clean_lines) + "\n\\end{quote}\n"
        
    md_text = re.sub(r'((?:^> .*?(?:\n|$))+)', replace_blockquote, md_text, flags=re.MULTILINE)
    
    # Lists
    def replace_list(match):
        lines = match.group(1).strip().split('\n')
        latex_lines = ["\\begin{itemize}"]
        for line in lines:
            if line.startswith('- '):
                latex_lines.append("\\item " + line[2:])
        latex_lines.append("\\end{itemize}\n")
        return "\n".join(latex_lines) + "\n"
        
    md_text = re.sub(r'((?:^- .*?(?:\n|$))+)', replace_list, md_text, flags=re.MULTILINE)
    
    # Links
    md_text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\\href{\2}{\1}', md_text)
    
    # horizontal rules
    md_text = re.sub(r'^---$', r'\\hrulefill', md_text, flags=re.MULTILINE)
    
    # Escape some % signs if not in math? Actually, let's leave it as is. This is a naive conversion that keeps math blocks.
    out += md_text + "\n\n"
    return out

titles = [
    "Refined Algebraic Quantization",
    "Some Trivial Examples of RAQ",
    "The Connection Formulation of General Relativity"
]

final_tex = latex_header

for file, title in zip(files, titles):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    final_tex += md_to_latex(content, title)

final_tex += latex_footer

with open('/Users/whitney/astro-blog/astro/LQG_Notes.tex', 'w', encoding='utf-8') as f:
    f.write(final_tex)

print("Successfully converted posts to LQG_Notes.tex")
