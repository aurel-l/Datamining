import matplotlib.pyplot as _plt
import os as _os


def main(features, matrix, classes, ignored=[]):
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

    for i in range(0, dimensions - 1):
        for j in range(i + 1, dimensions):
            fig, ax = _plt.subplots()
            fig.set_size_inches(10, 10)
            ax.scatter(
                matrix[:, i], matrix[:, j], c=classes,
                s=20, marker='.', lw=0
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
