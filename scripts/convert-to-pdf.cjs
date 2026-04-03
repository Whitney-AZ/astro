const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const POSTS_DIR = path.join(__dirname, '..', 'src', 'content', 'posts');
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'pdfs');
const TEMP_DIR = path.join(__dirname, '..', '.tex-build');
const SKIP_FILES = ['test.md'];

// ========== Frontmatter Parser ==========
function parseFrontmatter(content) {
  content = content.replace(/\r\n/g, '\n');
  const match = content.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!match) return { meta: {}, body: content };
  const meta = {};
  for (const line of match[1].split('\n')) {
    const m = line.match(/^(\w+):\s*(.+)$/);
    if (m) {
      let val = m[2].trim();
      if (val.startsWith('[') && val.endsWith(']')) {
        val = val.slice(1, -1).split(',').map(s => s.trim().replace(/^['"]|['"]$/g, ''));
      } else if (val === 'true') val = true;
      else if (val === 'false') val = false;
      else val = val.replace(/^['"]|['"]$/g, '');
      meta[m[1]] = val;
    }
  }
  return { meta, body: match[2] };
}

// ========== Math Extraction ==========
function extractMath(text) {
  const placeholders = [];
  // Display math $$...$$
  text = text.replace(/\$\$([\s\S]*?)\$\$/g, (_, math) => {
    const i = placeholders.length;
    placeholders.push({ type: 'd', content: math });
    return `\x00D${i}\x00`;
  });
  // Inline math $...$
  text = text.replace(/\$([^\$\n]+?)\$/g, (_, math) => {
    const i = placeholders.length;
    placeholders.push({ type: 'i', content: math });
    return `\x00I${i}\x00`;
  });
  return { text, placeholders };
}

function restoreMath(text, placeholders) {
  for (let i = 0; i < placeholders.length; i++) {
    const p = placeholders[i];
    const marker = p.type === 'd' ? `\x00D${i}\x00` : `\x00I${i}\x00`;
    let content = p.content;
    if (p.type === 'd') {
      // Remove blank lines inside display math (they break LaTeX math mode)
      content = content.replace(/\n\s*\n/g, '\n');
    }
    const replacement = p.type === 'd' ? `\\[${content}\\]` : `$${content}$`;
    text = text.split(marker).join(replacement);
  }
  return text;
}

// ========== Inline Markdown Processing ==========
function processInline(text) {
  // HTML entities
  text = text.replace(/&emsp;&emsp;/g, '');
  text = text.replace(/&emsp;/g, '');
  text = text.replace(/&amp;/g, '\\&');
  text = text.replace(/&lt;/g, '<');
  text = text.replace(/&gt;/g, '>');
  text = text.replace(/&nbsp;/g, '~');
  // HTML tags
  text = text.replace(/<br\s*\/?>/gi, '\\\\');
  text = text.replace(/<\/?span[^>]*>/gi, '');
  text = text.replace(/<\/?p[^>]*>/gi, '');
  // Bold **text**
  text = text.replace(/\*\*(.+?)\*\*/g, '\\textbf{$1}');
  // Italic _text_
  text = text.replace(/(?<!\w)_(.+?)_(?!\w)/g, '\\textit{$1}');
  // Italic *text* (after bold is already handled)
  text = text.replace(/(?<!\\)\*(.+?)\*/g, '\\textit{$1}');
  // Links [text](url)
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '\\href{$2}{$1}');
  // Escape %
  text = text.replace(/%/g, '\\%');
  return text;
}

// ========== Convert Markdown Body to LaTeX ==========
function convertBody(body, headingOffset) {
  const { text, placeholders } = extractMath(body);
  const lines = text.split('\n');
  const output = [];
  let inBlockquote = false;
  let bqContent = [];
  let inList = false;

  function flushBQ() {
    if (bqContent.length > 0) {
      output.push('\\begin{quote}');
      output.push(processInline(bqContent.join(' ')));
      output.push('\\end{quote}');
      bqContent = [];
    }
    inBlockquote = false;
  }
  function flushList() {
    if (inList) { output.push('\\end{itemize}'); inList = false; }
  }

  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];

    // Blockquote
    if (line.startsWith('> ') || line === '>') {
      if (inList) flushList();
      if (!inBlockquote) inBlockquote = true;
      const content = line.replace(/^>\s?/, '').trim();
      if (content && !content.match(/^<br\s*\/?>$/i)) {
        bqContent.push(content);
      }
      continue;
    } else if (inBlockquote) {
      flushBQ();
    }

    // Horizontal rule
    if (line.trim() === '---') {
      flushList();
      output.push('');
      output.push('\\bigskip\\noindent\\rule{\\textwidth}{0.4pt}\\bigskip');
      output.push('');
      continue;
    }

    // Headings
    const hm = line.match(/^(#{1,4})\s+(.+)$/);
    if (hm) {
      flushList();
      const level = hm[1].length - 3 + headingOffset; // ### = level 0 + offset
      const cmds = ['\\section', '\\subsection', '\\subsubsection', '\\paragraph'];
      const cmd = cmds[Math.max(0, Math.min(level, cmds.length - 1))];
      output.push(`${cmd}{${processInline(hm[2])}}`);
      output.push('');
      continue;
    }

    // List items
    const lm = line.match(/^-\s+(.+)$/);
    if (lm) {
      if (!inList) { output.push('\\begin{itemize}'); inList = true; }
      output.push(`  \\item ${processInline(lm[1])}`);
      continue;
    } else if (inList) {
      flushList();
    }

    // Math placeholder line
    if (line.trim().match(/^\x00D\d+\x00$/)) {
      output.push(line.trim());
      continue;
    }

    // Empty line
    if (line.trim() === '') {
      output.push('');
      continue;
    }

    // Regular text
    output.push(processInline(line));
  }
  flushBQ();
  flushList();

  let result = output.join('\n');
  result = restoreMath(result, placeholders);
  return result;
}

// ========== LaTeX Document Template ==========
function generateTex(title, date, body, hasTOC) {
  // Escape title for LaTeX
  const safeTitle = title.replace(/%/g, '\\%');
  return `\\documentclass[a4paper, 11pt]{ctexart}

% Math
\\usepackage{amsmath, amssymb, amsthm, mathtools}

% Layout
\\usepackage[margin=2.5cm]{geometry}

% Colors
\\usepackage{xcolor}

% Links
\\usepackage[hidelinks]{hyperref}
\\hypersetup{
  colorlinks=true,
  linkcolor=blue!70!black,
  urlcolor=blue!60!black,
  pdftitle={${safeTitle}}
}

\\title{${safeTitle}}
\\author{}
\\date{${date}}

\\begin{document}
\\maketitle
${hasTOC ? '\\tableofcontents\n\\newpage\n' : ''}
${body}
\\end{document}
`;
}

// ========== Series filename map ==========
const SERIES_FILENAMES = {
  'LQG Notes': 'LQG-Notes',
  'LQG Basics': 'LQG-Basics',
  '甜甜圈宇宙': 'DonutUniverse',
};

// ========== Main ==========
function main() {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  fs.mkdirSync(TEMP_DIR, { recursive: true });

  // Read all posts
  const files = fs.readdirSync(POSTS_DIR).filter(f => f.endsWith('.md') && !SKIP_FILES.includes(f));
  const posts = files.map(f => {
    const content = fs.readFileSync(path.join(POSTS_DIR, f), 'utf-8');
    const { meta, body } = parseFrontmatter(content);
    return { filename: f, meta, body };
  });

  // Group by series
  const seriesMap = {};
  const standalone = [];
  for (const post of posts) {
    if (post.meta.series) {
      if (!seriesMap[post.meta.series]) seriesMap[post.meta.series] = [];
      seriesMap[post.meta.series].push(post);
    } else {
      standalone.push(post);
    }
  }
  // Sort series posts by date
  for (const s of Object.values(seriesMap)) {
    s.sort((a, b) => new Date(a.meta.date) - new Date(b.meta.date));
  }

  const documents = [];

  // Series documents
  for (const [seriesName, sPosts] of Object.entries(seriesMap)) {
    const safeName = SERIES_FILENAMES[seriesName] || seriesName.replace(/[^a-zA-Z0-9]/g, '-');
    let body = '';
    for (let j = 0; j < sPosts.length; j++) {
      const p = sPosts[j];
      body += `\\section{${processInline(p.meta.title)}}\n\n`;
      if (p.meta.summary) body += `\\noindent\\textit{${processInline(p.meta.summary)}}\n\n\\bigskip\n\n`;
      body += convertBody(p.body, 1);
      if (j < sPosts.length - 1) body += '\n\n\\newpage\n\n';
    }
    const dates = sPosts.map(p => p.meta.date).filter(Boolean);
    documents.push({ name: safeName, tex: generateTex(seriesName, dates.join(' — '), body, sPosts.length > 1) });
  }

  // Standalone documents
  for (const post of standalone) {
    const safeName = post.filename.replace('.md', '');
    const body = convertBody(post.body, 0);
    documents.push({ name: safeName, tex: generateTex(post.meta.title, post.meta.date || '', body, false) });
  }

  // Write and compile
  let successCount = 0;
  for (const doc of documents) {
    const texPath = path.join(TEMP_DIR, `${doc.name}.tex`);
    fs.writeFileSync(texPath, doc.tex, 'utf-8');
    console.log(`\nWritten: ${doc.name}.tex`);

    try {
      for (let pass = 1; pass <= 2; pass++) {
        console.log(`  Compiling pass ${pass}...`);
        execSync(
          `xelatex -interaction=nonstopmode -output-directory="${TEMP_DIR}" "${texPath}"`,
          { cwd: TEMP_DIR, stdio: 'pipe', timeout: 120000 }
        );
      }
      const pdfSrc = path.join(TEMP_DIR, `${doc.name}.pdf`);
      const pdfDst = path.join(OUTPUT_DIR, `${doc.name}.pdf`);
      if (fs.existsSync(pdfSrc)) {
        fs.copyFileSync(pdfSrc, pdfDst);
        console.log(`  ✓ ${doc.name}.pdf`);
        successCount++;
      } else {
        console.error(`  ✗ PDF not generated`);
      }
    } catch (err) {
      console.error(`  ✗ Compile failed for ${doc.name}`);
      // Print log for debugging
      const logPath = path.join(TEMP_DIR, `${doc.name}.log`);
      if (fs.existsSync(logPath)) {
        const log = fs.readFileSync(logPath, 'utf-8');
        const errors = log.split('\n').filter(l => l.startsWith('!') || l.includes('Error'));
        if (errors.length > 0) console.error('  Errors:', errors.slice(0, 5).join('\n  '));
      }
    }
  }

  console.log(`\n========================================`);
  console.log(`Done! ${successCount}/${documents.length} PDFs generated in ${OUTPUT_DIR}`);
}

main();
