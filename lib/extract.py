from Bio.SeqIO import parse as _parse
import numpy as _np
from sys import argv as _argv
import os as _os
from importlib import import_module as _import_module

from lib.progress import Progress as _Progress


class _Output:
    def __init__(self, n_proteins, features, extract):
        self.n_proteins = n_proteins
        self.features = features
        self.extract = extract


def main(file_name, extract_lambda, features=[], n_proteins=None, log=True):
    """
    Extract information from the input file
    :param file_name: input file to parse
    :type file_name: str
    :param extract_lambda: lambda function to extract additional information
    :type extract_lambda: builtins.function
    :param features: features to extract
    :type features: list[str]
    :param n_proteins: number of proteins to extract, if None, extract all
    :type n_proteins: int or None
    :param log: log information to stdout
    :type log: bool
    :returns: output object with corresponding information
    :rtype: _Output
    """
    if not n_proteins:
        # Tries to get the number of proteins in the file if not provided
        try:
            # Quickest way, with unix command 'wc'
            n_proteins = int(_os.popen(
                'grep "</entry" {} | wc -l'.format(file_name)
            ).readline())
            if not n_proteins:
                raise ValueError
        except:
            # Slowest way, parsing the file with BioPython
            n_proteins = 0
            g = _parse(open(file_name, encoding='utf-8'), 'uniprot-xml')
            for _ in g:
                n_proteins += 1

    try:
        # tries to create a directory for the data warehouse
        _os.makedirs('warehouse')
    except OSError:
        # already exists
        filelist = [
            filename
            for filename in _os.listdir('warehouse')
            if filename.endswith('.dat')
        ]
        for filename in filelist:
            try:
                _os.remove('warehouse{}{}'.format(_os.path.sep, filename))
            except FileNotFoundError:
                # prevents error due to race condition
                pass

    modules = [
        _import_module('lib.features.{}'.format(feature))
        for feature in features
    ]
    memmaps = [
        _np.memmap(
            'warehouse{}{}.dat'.format(_os.path.sep, feature),
            dtype=_np.float64,
            mode='w+',
            shape=(n_proteins, module.size_values)
        )
        for (feature, module) in zip(features, modules)]

    if log:
        print('extracting data from {} protein{}'.format(
            n_proteins,
            's' if n_proteins > 1 else ''
        ))
        progress = _Progress(60, n_proteins)

    extracted = []
    for (seq, i) in zip(
        _parse(open(file_name, encoding='utf-8'), 'uniprot-xml'),
        range(n_proteins)
    ):
        for (module, memmap) in zip(modules, memmaps):
            memmap[i] = module.value(seq)
        if extract_lambda:
            extracted.append(extract_lambda(seq))
        if log:
            progress.increment()

    if log:
        progress.finish()

    return _Output(n_proteins, features, extracted)
