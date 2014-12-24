#!/usr/bin/python
# -*- coding: utf-8 -*-

from Bio import SeqIO
import sys
import time

nSeq = 0
stats = {
    'seq': {'presence': 0, 'length': 0, 'type': None},
    'id': {'presence': 0, 'length': 0, 'type': None},
    'name': {'presence': 0, 'length': 0, 'type': None},
    'description': {'presence': 0, 'length': 0, 'type': None},
    'dbxrefs': {'presence': 0, 'length': 0, 'type': None},
    'features': {'presence': 0, 'length': 0, 'type': None},
    'annotations': {'presence': 0, 'length': 0, 'type': None},
    'letter_annotations': {'presence': 0, 'length': 0, 'type': None},
    }
features = {}
types = {}
annotations = {}

sequences = SeqIO.parse(sys.stdin, 'uniprot-xml')
begin = time.time()
for s in sequences:
    nSeq += 1
    for attr in stats:
        length = len(getattr(s, attr))
        if length:
            stats[attr]['presence'] += 1
            stats[attr]['length'] += length
        if not stats[attr]['type']:
            stats[attr]['type'] = type(getattr(s, attr))
    for f in s.features:
        for q in f.qualifiers:
            if not q in features:
                features[q] = 0
            features[q] += 1
        if 'type' in f.qualifiers:
            t = f.qualifiers['type']
            if not t in types:
                types[t] = 0
            types[t] += 1
    for a in s.annotations:
        if not a in annotations:
            annotations[a] = 0
        annotations[a] += 1
    sys.stdout.write("\b" * 80
                     + 'analyzed {} sequences in {:.3f} seconds'.format(nSeq,
                     round(time.time() - begin, 3)))
    sys.stdout.flush()
sys.stdout.write('\n')

# prints results

for attr in sorted(stats, key=lambda x: stats[x]['length'],
                   reverse=True):
    print '{} (type: {}):'.format(attr, stats[attr]['type'])
    print '  length: {: >8} (mean: {: >8.2f})'.format(stats[attr]['length'
            ], round(stats[attr]['length'] / float(nSeq), 2))
    print '  present in {: >5} sequences ({: >6.2f}%)'.format(stats[attr]['presence'
            ], round(100.0 * stats[attr]['presence'] / nSeq, 2))
print 'feature qualifiers:'
for f in sorted(features, key=features.get, reverse=True):
    print '  {: >6} {}'.format(features[f], f)
print 'feature qualifier types:'
for t in sorted(types, key=types.get, reverse=True):
    print '  {: >6} {}'.format(types[t], t)
print 'annotations:'
for a in sorted(annotations, key=annotations.get, reverse=True):
    print '  {: >6} ({: >6.2f}%) {}'.format(annotations[a], round(100.0
            * annotations[a] / nSeq, 2), a)
