#!/usr/bin/python3

import argparse

from extract import main as extract
from process import main as process
from precluster import main as precluster
from cluster import main as cluster
from visualize import main as visualize

parser = argparse.ArgumentParser(description='Datamining of human proteins')
parser.add_argument(
    'input', metavar='I', type=str, help='an input file in uniprot XML'
)
parser.add_argument(
    'features', metavar='F', type=str, nargs='+',
    help=(
        'list of features to process. ' +
        'Available: "aminoacids", "structure", "phi", "weight", "length"'
    )
)
parser.add_argument(
    '--maximum', '-m', metavar='M', type=int, nargs='?',
    help='define a maximum number of proteins to process'
)
args = parser.parse_args()

extract_output = extract(
    args.input,
    extract_lambda=lambda s: s.name,
    features=args.features,
    n_proteins=args.maximum
)

process_output = process(args.features, extract_output.n_proteins)
for (i, d, f) in zip(
    process_output.informations,
    process_output.original_dimensions,
    args.features
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

visualize(args.features, process_output.matrix, classes)
