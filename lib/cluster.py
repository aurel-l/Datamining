from lib.progress import Progress as _Progress
from lib.stats.k_means import k_means as _k_means


def main(matrix, n_clusters, log=True):
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
            progress.setValue(length - step.changes)
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
