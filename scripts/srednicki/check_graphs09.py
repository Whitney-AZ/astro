"""Independently recount the symmetry factors of the diagrams used in section 9."""
from collections import Counter
from itertools import permutations, product
from math import factorial, prod
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
data = json.loads((ROOT / 'checks/srednicki/graphs09.json').read_text())
results = []
for graph in data['graphs']:
    nodes = graph['topology']['nodes']
    types = {node['id']: node['type'] for node in nodes}
    groups = [[n for n in types if types[n] == kind] for kind in sorted(set(types.values()))]
    edges = Counter()
    for edge in graph['topology']['edges']:
        edges[tuple(sorted((edge['from'], edge['to'])))] += edge['multiplicity']
    automorphisms = 0
    for choices in product(*(permutations(group) for group in groups)):
        mapping = {old: new for group, choice in zip(groups, choices) for old, new in zip(group, choice)}
        mapped = Counter({tuple(sorted((mapping[u], mapping[v]))): count for (u, v), count in edges.items()})
        automorphisms += mapped == edges
    loops = sum(count for (u, v), count in edges.items() if u == v)
    factor = automorphisms * 2**loops * prod(factorial(n) for n in edges.values())
    degrees = {node: sum(count * ((u == node) + (v == node)) for (u, v), count in edges.items()) for node in types}
    assert all(degrees[node] == (3 if kind == 'cubic_vertex' else 1) for node, kind in types.items()), graph['id']
    assert factor == graph['expected_symmetry_factor'], (graph['id'], factor)
    results.append({'id': graph['id'], 'node_automorphisms': automorphisms, 'loops': loops, 'symmetry_factor': factor})
(ROOT / 'checks/srednicki/graphs09-check.json').write_text(json.dumps(results, indent=2) + '\n')
print(f'Checked valences and symmetry factors for {len(results)} diagrams.')
