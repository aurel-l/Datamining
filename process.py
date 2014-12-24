#!/usr/bin/python3

import numpy as _np
from importlib import import_module as _import_module
from os.path import sep as _sep

from lib.stats.PCA import PCA as _PCA
from lib.progress import Progress as _Progress


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
        vector = (v * mm.T).T
    else:
        # no need to reduce dimensions
        vector = mm
    minValue, maxValue = vector.min(), vector.max()
    # returns normalized value (between 0.0 and 1.0)
    return ((vector - minValue) / (maxValue - minValue))[:, 0].T


def main(features=[], n_proteins=1, log=True):
    dimensions = len(features)
    if log:
        print('processing data from {} features'.format(dimensions))
        progress = _Progress(60, dimensions * 2 + 1)
    sizes = _np.empty(dimensions, dtype=_np.uint8)

    matrix = _np.empty(
        n_proteins * dimensions,
        dtype=_np.float64
    ).reshape(n_proteins, dimensions)
    if log:
        progress.increment()

    for (i, feature) in enumerate(features):
        if log:
            progress.increment()
        matrix[:, i] = _reduce(n_proteins, feature)
        if log:
            progress.increment()
    if log:
        progress.finish()

    return matrix

if __name__ == '__main__':
    main(['aminoacids', 'structure', 'length'], n_proteins, True)
