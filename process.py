#!/usr/bin/python3

import numpy as _np
from importlib import import_module as _import_module
from os.path import sep as _sep

from lib.stats.PCA import PCA as _PCA
from lib.progress import Progress as _Progress


class _Output:
    def __init__(self, matrix, informations):
        self.matrix = matrix
        self.informations = informations


def _reduce(length, feature):
    module = _import_module('lib.features.{}'.format(feature))
    mm = _np.memmap(
        'warehouse{}{}.dat'.format(_sep, feature),
        dtype=_np.float64,
        mode='r',
        shape=(length, module.size_values)
    )
    if (module.size_values > 1):
        # computes the PCA
        pca = _PCA(mm)
        # gets the first eigenvector
        v = pca.getVectors(1)
        # reduces dimensions to 1
        vector = (v * mm.T)[0]
        information = pca.information(1)
    else:
        # no need to reduce dimensions
        vector = mm.T[0]
        information = 1.0
    minValue, maxValue = vector.min(), vector.max()
    # returns normalized value (between 0.0 and 1.0)
    # and proportion of information kept
    return (((vector - minValue) / (maxValue - minValue)), information)


def main(features=[], n_proteins=1, log=True):
    dimensions = len(features)
    if log:
        print('processing data from {} feature{}'.format(
            dimensions,
            's' if dimensions > 1 else ''
        ))
        progress = _Progress(60, dimensions * 2 + 1)
    sizes = _np.empty(dimensions, dtype=_np.uint8)

    matrix = _np.empty(
        n_proteins * dimensions,
        dtype=_np.float64
    ).reshape(n_proteins, dimensions)
    informations = _np.empty(dimensions, dtype=_np.float16)
    if log:
        progress.increment()

    for (i, feature) in enumerate(features):
        if log:
            progress.increment()
        (matrix[:, i], informations[i]) = _reduce(n_proteins, feature)
        if log:
            progress.increment()
    if log:
        progress.finish()

    return _Output(matrix, informations)

if __name__ == '__main__':
    main(['aminoacids', 'structure', 'length'], 20195, True)
