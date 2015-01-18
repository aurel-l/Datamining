from lib.progress import Progress as _Progress
from lib.stats.k_means import k_means as _k_means


def main(matrix, n_clusters, log=True):
    """
    Performs a k-means (k-medoid variant) on the input data
    :param matrix: input data matrix to cluster
    :type matrix: numpy.ndarray
    :param n_clusters: number of clusters
    :type n_clusters: int
    :param log: log information to stdout
    :type log: bool
    :returns: array containing, for every item of the matrix,
        its corresponding cluster (from 1 to n_clusters + 1)
    :rtype: numpy.ndarray
    """
    length = len(matrix)
    if log:
        print(
            'performing k-means clustering with {} cluster{}'.format(
                n_clusters,
                's' if n_clusters > 1 else ''
            )
        )
        progress = _Progress(60, length)
    for step in _k_means(matrix, n_clusters, True, True, True):
        if log:
            progress.set_value(length - step.changes)
        if step.converged or step.n_loops >= 80:
            if log:
                progress.finish(step.converged)
                print('k-means {} after {} loop{}'.format(
                    'converged' if step.converged else 'did not converge',
                    step.n_loops,
                    's' if step.n_loops > 1 else ''
                ))
            break
    return step.classes
