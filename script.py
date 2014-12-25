#!/usr/bin/python3

from extract import main as extract
from process import main as process
from cluster import main as cluster

file_name = 'data.xml'
features = ['aminoacids', 'structure', 'length']
n_clusters = 50

extract_output = extract(
    file_name,
    features=features,
    extract_lambda=lambda s: s.name
)
process_output = process(features, extract_output.n_proteins)
for (f, i) in zip(features, process_output.informations):
    print('kept {:7.2%} of information in {} feature'.format(i, f))
classes = cluster(process_output.matrix, n_clusters)
print('class counts')
count = [(classes == (i + 1)).sum() for i in range(n_clusters)]
print(count)
#for (n, c) in zip(output.extract, classes):
#    print('protein {} belongs to class {}'.format(n, c))
