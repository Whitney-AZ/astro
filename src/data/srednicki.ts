export type SrednickiPart = 1 | 2 | 3

export type SrednickiSection = {
  id: number
  title: string
  prereqs: number[]
  part: SrednickiPart
  depth: number
}

const rawSections: Array<[number, string, number[]]> = [
  [1, 'Attempts at relativistic quantum mechanics', []],
  [2, 'Lorentz Invariance', [1]],
  [3, 'Canonical Quantization of Scalar Fields', [2]],
  [4, 'The Spin-Statistics Theorem', [3]],
  [5, 'The LSZ Reduction Formula', [3]],
  [6, 'Path Integrals in Quantum Mechanics', []],
  [7, 'The Path Integral for the Harmonic Oscillator', [6]],
  [8, 'The Path Integral for Free Field Theory', [3, 7]],
  [9, 'The Path Integral for Interacting Field Theory', [8]],
  [10, 'Scattering Amplitudes and the Feynman Rules', [5, 9]],
  [11, 'Cross Sections and Decay Rates', [10]],
  [12, 'Dimensional Analysis with ℏ = c = 1', [3]],
  [13, 'The Lehmann-Källén Form of the Exact Propagator', [9]],
  [14, 'Loop Corrections to the Propagator', [10, 12, 13]],
  [15, 'The One-Loop Correction in Lehmann-Källén Form', [14]],
  [16, 'Loop Corrections to the Vertex', [14]],
  [17, 'Other 1PI Vertices', [16]],
  [18, 'Higher-Order Corrections and Renormalizability', [17]],
  [19, 'Perturbation Theory to All Orders', [18]],
  [20, 'Two-Particle Elastic Scattering at One Loop', [19]],
  [21, 'The Quantum Action', [19]],
  [22, 'Continuous Symmetries and Conserved Currents', [8]],
  [23, 'Discrete Symmetries: P, T, C, and Z', [22]],
  [24, 'Nonabelian Symmetries', [22]],
  [25, 'Unstable Particles and Resonances', [14]],
  [26, 'Infrared Divergences', [20]],
  [27, 'Other Renormalization Schemes', [26]],
  [28, 'The Renormalization Group', [27]],
  [29, 'Effective Field Theory', [28]],
  [30, 'Spontaneous Symmetry Breaking', [21]],
  [31, 'Broken Symmetry and Loop Corrections', [30]],
  [32, 'Spontaneous Breaking of Continuous Symmetries', [22, 30]],
  [33, 'Representations of the Lorentz Group', [2]],
  [34, 'Left- and Right-Handed Spinor Fields', [3, 33]],
  [35, 'Manipulating Spinor Indices', [34]],
  [36, 'Lagrangians for Spinor Fields', [22, 35]],
  [37, 'Canonical Quantization of Spinor Fields I', [36]],
  [38, 'Spinor Technology', [37]],
  [39, 'Canonical Quantization of Spinor Fields II', [38]],
  [40, 'Parity, Time Reversal, and Charge Conjugation', [23, 39]],
  [41, 'LSZ Reduction for Spin-One-Half Particles', [5, 39]],
  [42, 'The Free Fermion Propagator', [39]],
  [43, 'The Path Integral for Fermion Fields', [9, 42]],
  [44, 'Formal Development of Fermionic Path Integrals', [43]],
  [45, 'The Feynman Rules for Dirac Fields', [10, 12, 41, 43]],
  [46, 'Spin Sums', [45]],
  [47, 'Gamma Matrix Technology', [36]],
  [48, 'Spin-Averaged Cross Sections', [46, 47]],
  [49, 'The Feynman Rules for Majorana Fields', [45]],
  [50, 'Massless Particles and Spinor Helicity', [48]],
  [51, 'Loop Corrections in Yukawa Theory', [19, 40, 48]],
  [52, 'Beta Functions in Yukawa Theory', [28, 51]],
  [53, 'Functional Determinants', [44, 45]],
  [54, 'Maxwell’s Equations', [3]],
  [55, 'Electrodynamics in Coulomb Gauge', [54]],
  [56, 'LSZ Reduction for Photons', [5, 55]],
  [57, 'The Path Integral for Photons', [8, 56]],
  [58, 'Spinor Electrodynamics', [45, 57]],
  [59, 'Scattering in Spinor Electrodynamics', [48, 58]],
  [60, 'Spinor Helicity for Spinor Electrodynamics', [50, 59]],
  [61, 'Scalar Electrodynamics', [58]],
  [62, 'Loop Corrections in Spinor Electrodynamics', [51, 59]],
  [63, 'The Vertex Function in Spinor Electrodynamics', [62]],
  [64, 'The Magnetic Moment of the Electron', [63]],
  [65, 'Loop Corrections in Scalar Electrodynamics', [61, 62]],
  [66, 'Beta Functions in Quantum Electrodynamics', [52, 62]],
  [67, 'Ward Identities in Quantum Electrodynamics I', [22, 59]],
  [68, 'Ward Identities in Quantum Electrodynamics II', [63, 67]],
  [69, 'Nonabelian Gauge Theory', [24, 58]],
  [70, 'Group Representations', [69]],
  [71, 'The Path Integral for Nonabelian Gauge Theory', [53, 69]],
  [72, 'The Feynman Rules for Nonabelian Gauge Theory', [71]],
  [73, 'The Beta Function in Nonabelian Gauge Theory', [70, 72]],
  [74, 'BRST Symmetry', [70, 71]],
  [75, 'Chiral Gauge Theories and Anomalies', [70, 72]],
  [76, 'Anomalies in Global Symmetries', [75]],
  [77, 'Anomalies and the Path Integral for Fermions', [76]],
  [78, 'Background Field Gauge', [73]],
  [79, 'Gervais–Neveu Gauge', [78]],
  [80, 'The Feynman Rules for N × N Matrix Fields', [10]],
  [81, 'Scattering in Quantum Chromodynamics', [60, 79, 80]],
  [82, 'Wilson Loops, Lattice Theory, and Confinement', [29, 73]],
  [83, 'Chiral Symmetry Breaking', [76, 82]],
  [84, 'Spontaneous Breaking of Gauge Symmetries', [32, 70]],
  [85, 'Spontaneously Broken Abelian Gauge Theory', [61, 84]],
  [86, 'Spontaneously Broken Nonabelian Gauge Theory', [85]],
  [87, 'The Standard Model: Gauge and Higgs Sector', [84]],
  [88, 'The Standard Model: Lepton Sector', [75, 87]],
  [89, 'The Standard Model: Quark Sector', [88]],
  [90, 'Electroweak Interactions of Hadrons', [83, 89]],
  [91, 'Neutrino Masses', [89]],
  [92, 'Solitons and Monopoles', [84]],
  [93, 'Instantons and Theta Vacua', [92]],
  [94, 'Quarks and Theta Vacua', [77, 83, 93]],
  [95, 'Supersymmetry', [69]],
  [96, 'The Minimal Supersymmetric Standard Model', [89, 95]],
  [97, 'Grand Unification', [89]],
]

const rawLookup = new Map(rawSections.map(([id, title, prereqs]) => [id, { id, title, prereqs }]))
const depthMemo = new Map<number, number>()

function getDepth(id: number): number {
  const cached = depthMemo.get(id)
  if (cached !== undefined) return cached

  const prereqs = rawLookup.get(id)?.prereqs ?? []
  const depth = prereqs.length ? 1 + Math.max(...prereqs.map(getDepth)) : 0
  depthMemo.set(id, depth)
  return depth
}

export const srednickiSections: SrednickiSection[] = rawSections.map(([id, title, prereqs]) => ({
  id,
  title,
  prereqs,
  part: id <= 32 ? 1 : id <= 53 ? 2 : 3,
  depth: getDepth(id),
}))

export const srednickiSectionById = new Map(
  srednickiSections.map((section) => [section.id, section]),
)

export const srednickiChildren = new Map(
  srednickiSections.map((section) => [section.id, [] as number[]]),
)

for (const section of srednickiSections) {
  for (const prereq of section.prereqs) {
    srednickiChildren.get(prereq)?.push(section.id)
  }
}

export const srednickiPartNames: Record<SrednickiPart, string> = {
  1: 'I · Spin Zero',
  2: 'II · Spin One Half',
  3: 'III · Spin One',
}

export function getSrednickiSectionHref(id: number, hasNote = false, noteHref?: string) {
  return hasNote && noteHref ? noteHref : `/srednicki/sections/${id}`
}
