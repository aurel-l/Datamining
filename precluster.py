import numpy as _np
import matplotlib.pyplot as _plt
from multiprocessing import Pool as _Pool

from lib.stats.k_means import k_means as _k_means
from lib.progress import Progress as _Progress


def _process(args):
    n_clusters, matrix = args
    for step in _k_means(matrix, n_clusters, True, True, True):
        if step.converged or step.n_loops >= 80:
            break

    inter = _np.array([
        _np.sqrt(
            _np.power((step.barycenters[n] - step.barycenters), 2).sum(1)
        ) / (n_clusters - 1)
        for n in range(n_clusters)
    ]).mean()

    intra = _np.zeros(n_clusters)
    for n in range(n_clusters):
        classPop = _np.matrix([
            row
            for i, row in enumerate(matrix)
            if step.classes[i] == (n + 1)
        ])
        lengthPop = len(classPop)
        intra[n] = _np.sqrt(
            _np.power((step.barycenters[n] - classPop), 2).sum(1)
        ).mean()
    intra = intra.mean()

    return n_clusters, inter / intra


def main(matrix, min_clusters=2, max_clusters=10, n_replicates=4, log=True):
    pool = _Pool()
    async_results = pool.imap_unordered(
        _process,
        [
            (i, matrix)
            for i in range(min_clusters, max_clusters + 1)
            for _ in range(n_replicates)
        ]
    )

    if log:
        print('computing best k for clustering step')
        p = _Progress(60, (max_clusters + 1 - min_clusters) * n_replicates)
    results = _np.zeros(max_clusters + 1 - min_clusters)
    for k, value in async_results:
        if log:
            p.increment()
        results[k - min_clusters] += value
    results /= n_replicates
    if log:
        p.finish()
        _plt.plot(results)
        _plt.show()
    return _np.argmax(results) + min_clusters
