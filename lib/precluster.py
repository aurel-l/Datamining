import numpy as _np
#import matplotlib.pyplot as _plt
from multiprocessing import Pool as _Pool

from lib.stats.k_means import k_means as _k_means
from lib.progress import Progress as _Progress


class _Output:
    def __init__(self, best_k, ics, range):
        self.best_k = best_k
        self.ics = ics
        self.range = range


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

    return n_clusters, intra / inter


def main(matrix, min_clusters=2, max_clusters=10, n_replicates=4, log=True):
    """
    Computes a Bayesian Information Criterion for each k and return the best k
    :param matrix: input data matrix
    :type matrix: numpy.ndarray
    :param min_clusters: minimum number of clusters
    :type min_clusters: int
    :param max_clusters: maximum number of clusters
    :type max_clusters: int
    :param n_replicates: number of replicates for each k
    :type n_replicates: int
    :param log: log information to stdout
    :type log: bool
    :returns: output object with corresponding information
    :rtype: _Output
    """
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
        #_plt.plot(results)
        #_plt.show()
    return _Output(
        _np.argmin(results) + min_clusters,
        results, (min_clusters, max_clusters)
    )
