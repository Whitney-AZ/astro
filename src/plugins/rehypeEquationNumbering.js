// src/plugins/rehypeEquationNumbering.js

import { visit } from 'unist-util-visit'

import { visit } from 'unist-util-visit'

export function rehypeEquationNumbering() {
  console.log('--- 正在运行公式编号插件 ---')
  return (tree) => {
    let counter = 1
    const labels = new Map()

    // 第一遍：找到所有块级公式，添加编号，并记录 \label
    visit(tree, 'element', (node) => {
      // remark-math 会将 $$...$$ 转换为带有 'math-display' 类的 div
      if (node.tagName === 'div' && node.properties?.className?.includes('math-display')) {
        const textNode = node.children?.[0]
        if (textNode && textNode.type === 'text') {
          let content = textNode.value

          // 如果公式包含 \nonumber，则不进行编号
          if (content.includes('\\nonumber')) {
            textNode.value = content.replace(/\\nonumber/g, '')
            return
          }

          const tag = counter++
          const labelMatch = content.match(/\\label\{(.*?)\}/)

          if (labelMatch) {
            const label = labelMatch[1]
            labels.set(label, tag)
            // 移除 \label 命令，因为它不是 KaTeX 的标准命令
            content = content.replace(labelMatch[0], '')
          }

          // 在公式末尾添加 \tag 命令
          textNode.value = content + ` \\tag{${tag}}`
        }
      }
    })

    // 第二遍：找到所有行内公式，替换 \ref
    visit(tree, 'element', (node) => {
      // remark-math 会将 $...$ 转换为带有 'math-inline' 类的 span
      if (node.tagName === 'span' && node.properties?.className?.includes('math-inline')) {
        const textNode = node.children?.[0]
        if (textNode && textNode.type === 'text') {
          // 使用正则表达式全局替换所有 \ref 命令
          textNode.value = textNode.value.replace(/\\ref\{(.*?)\}/g, (match, label) => {
            return labels.get(label) || '(???)' // 如果找不到标签，显示 ???
          })
        }
      }
    })
  }
}
