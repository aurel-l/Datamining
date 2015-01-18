import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as _plt
import os as _os
import numpy as _np

from lib.progress import Progress as _Progress


def main(features, matrix, clusters, n_clusters, bics, bic_range, log=True):
    """
    Visualize data after clustering
    :param features: features of the clustered data
    :type features: list[str]
    :param matrix: input data matrix
    :type matrix: numpy.ndarray
    :param clusters: cluster for each piece of data in the matrix data
    :type clusters: numpy.ndarray
    :param n_clusters: number of clusters
    :type n_clusters: int
    :param bics: Bayesian Information Criterions
    :type bics: list[float]
    :param log: log information to stdout
    :type log: bool
    """
    try:
        # tries to create a directory for the data warehouse
        _os.makedirs('visualization')
    except OSError:
        # already exists
        filelist = [
            filename
            for filename in _os.listdir('visualization')
            if filename.endswith('.png')
        ]
        for filename in filelist:
            try:
                _os.remove('visualization{}{}'.format(_os.path.sep, filename))
            except FileNotFoundError:
                # prevents error due to race condition
                pass

    dimensions = len(features)
    length = len(matrix)

    if log:
        print('generating data visualizations')
        p = _Progress(60, _np.array([range(dimensions + 1)]).sum() + 2)

    # scatter plots
    for i in range(dimensions - 1):
        for j in range(i + 1, dimensions):
            fig, ax = _plt.subplots()
            fig.set_size_inches(10, 10)
            ax.scatter(
                matrix[:, i], matrix[:, j], c=clusters,
                s=25, marker='.', lw=0
            )

            ax.set_xlabel(features[i])
            ax.set_xlim(0, 1)
            ax.set_ylabel(features[j])
            ax.set_ylim(0, 1)
            ax.set_title('{} vs {}'.format(features[i], features[j]))

            ax.grid(True)
            fig.tight_layout()

            filename = 'visualization{}scatter-{}-{}.png'.format(
                _os.path.sep, features[i], features[j]
            )
            _plt.savefig(filename, bbox_inches='tight', dpi=120)
            if log:
                p.increment()

    # histograms
    for i in range(dimensions):
        fig, ax = _plt.subplots()
        fig.set_size_inches(10, 10)
        ax.hist(
            [
                _np.array([
                    cell
                    for i, cell in enumerate(matrix[:, i])
                    if clusters[i] == c
                ])
                for c in range(1, n_clusters + 1)
            ],
            bins=100, range=(0, 1), histtype='barstacked', rwidth=1
        )

        ax.set_xlabel(features[i])
        ax.set_xlim(0, 1)
        ax.set_ylabel('count')
        ax.set_title(features[i])

        ax.grid(True)
        fig.tight_layout()

        filename = 'visualization{}histogram-{}.png'.format(
            _os.path.sep, features[i]
        )
        _plt.savefig(filename, bbox_inches='tight', dpi=120)
        if log:
            p.increment()

    # BIC
    fig, ax = _plt.subplots()
    fig.set_size_inches(10, 10)
    ax.plot(range(bic_range[0], bic_range[1] + 1), bics)

    ax.set_xlabel('k')
    ax.set_ylabel('BIC')
    ax.set_title('BIC for different values of k')

    ax.grid(True)
    fig.tight_layout()

    filename = 'visualization{}bics.png'.format(_os.path.sep, features[i])
    _plt.savefig(filename, bbox_inches='tight', dpi=120)
    if log:
        p.increment()

    # cluster counts
    fig, ax = _plt.subplots()
    fig.set_size_inches(10, 10)
    ax.hist(
        clusters, bins=range(1, n_clusters + 2),
        align='left', histtype='bar', rwidth=1
    )

    ax.set_xlabel('cluster')
    ax.set_xlim(0.5, n_clusters + 0.5)
    ax.set_ylabel('number of proteins')
    ax.set_title('sorted number of proteins by clusters')

    ax.grid(True)
    fig.tight_layout()

    filename = 'visualization{}counts.png'.format(_os.path.sep, features[i])
    _plt.savefig(filename, bbox_inches='tight', dpi=120)
    if log:
        p.increment()
        p.finish()
