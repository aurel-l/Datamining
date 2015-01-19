#!/usr/bin/python3

import argparse

from lib.extract import main as extract
from lib.process import main as process
from lib.precluster import main as precluster
from lib.cluster import main as cluster
from lib.visualize import main as visualize

parser = argparse.ArgumentParser(description='Datamining of human proteins')
parser.add_argument(
    'input_file', type=str, help='an input file in uniprot XML'
)
parser.add_argument(
    'features', type=str, nargs='*',
    help=(
        'list of features to process. ' +
        'Available: "aminoacids", "structure", "phi", "weight", "length"'
    )
)
parser.add_argument(
    '--maximum', '-m', metavar='M', type=int, nargs='?',
    help='define a maximum number of proteins to process'
)
parser.add_argument(
    '--output-file', '-o', metavar='O', type=str, nargs='?',
    help='optional output file for csv formatted cluster information'
)
args = parser.parse_args()

extract_output = extract(
    args.input_file,
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
        'kept {:7.2%} of information '.format(i) +
        'in {:2}-dimensional feature "{}"'.format(d, f)
    )

precluster_output = precluster(
    process_output.matrix, min_clusters=10, max_clusters=29, n_replicates=6
)

clusters = cluster(process_output.matrix, precluster_output.best_k)

visualize(
    args.features, process_output.matrix, clusters,
    precluster_output.best_k, precluster_output.bics, precluster_output.range
)

if args.output_file:
    f = open(args.output_file, 'w')
    f.write('sequence name\tcluster\n')
    for (n, c) in zip(extract_output.extract, clusters):
        f.write('{}\t{}\n'.format(n, c))
