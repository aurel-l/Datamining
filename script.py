#!/usr/bin/python3

from extract import main as extract
from process import main as process
from precluster import main as precluster
from cluster import main as cluster
from visualize import main as visualize

file_name = 'data.xml'
features = ['aminoacids', 'structure', 'phi', 'weight', 'length']

extract_output = extract(
    file_name,
    extract_lambda=lambda s: s.name,
    features=features
)

process_output = process(features, extract_output.n_proteins)
for (i, d, f) in zip(
    process_output.informations,
    process_output.original_dimensions,
    features
):
    print(
        'kept {:7.2%} of information'.format(i) +
        'in {:2}-dimensional feature "{}"'.format(d, f)
    )

n_clusters = precluster(
    process_output.matrix, min_clusters=10, max_clusters=110, n_replicates=5
)

classes = cluster(process_output.matrix, n_clusters)

print('class counts')
count = [(classes == (i + 1)).sum() for i in range(n_clusters)]
print(count)
#for (n, c) in zip(process_output.extract, classes):
#    print('protein {} belongs to class {}'.format(n, c))

visualize(features, process_output.matrix, classes)
