import { getCollection } from 'astro:content'

export type SrednickiNoteLink = {
  title: string
  href: string
}

export async function getSrednickiNotes() {
  const posts = await getCollection('posts', ({ data }) => {
    return import.meta.env.PROD ? data.draft !== true : true
  })

  const notesBySection: Record<string, SrednickiNoteLink[]> = {}

  for (const post of posts) {
    for (const sectionId of post.data.srednickiSections) {
      const key = String(sectionId)
      const note = { title: post.data.title, href: `/posts/${post.slug}` }
      notesBySection[key] = [...(notesBySection[key] ?? []), note]
    }
  }

  return notesBySection
}
