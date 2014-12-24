#!/usr/bin/python3

from extract import main as extract
from process import main as process
from cluster import main as cluster

file_name = 'data.xml'
features = ['aminoacids', 'structure', 'length']

output = extract(file_name, features, log=True)
process(features, output['n_proteins'], log=True)
#cluster()
