#!/usr/bin/python3

import argparse

from lib.extract import main as extract
from lib.process import main as process
from lib.precluster import main as precluster
from lib.cluster import main as cluster
from lib.visualize import main as visualize

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

precluster_output = precluster(
    process_output.matrix, min_clusters=10, max_clusters=110, n_replicates=5
)

clusters = cluster(process_output.matrix, precluster_output.best_k)
#for (n, c) in zip(process_output.extract, classes):
#    print('protein {} belongs to class {}'.format(n, c))

visualize(
    args.features, process_output.matrix, clusters,
    precluster_output.best_k, precluster_output.bics, precluster_output.range
)
