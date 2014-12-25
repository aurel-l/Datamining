import numpy as _np


class _Eigen:
    def __init__(self, value, vector):
        self.value = value
        self.vector = vector


class PCA:
    def __init__(self, data):
        means = data.mean(0)
        cov_mat = _np.cov(data.T)
        values, vectors = _np.linalg.eig(cov_mat)
        eigList = [_Eigen(val, vect) for (val, vect) in zip(values, vectors)]
        self.eig = sorted(eigList, key=lambda eig: eig.value, reverse=True)
        self.n_dim = len(self.eig)

    def getVectors(self, k=1):
        if (k > 0) and (k <= self.n_dim):
            return _np.matrix([eig.vector for eig in self.eig[:k]])
        else:
            raise ValueError('Incorrect number of dimensions')

    def information(self, k=1):
        if (k > 0) and (k <= self.n_dim):
            total = _np.sum([eig.value for eig in self.eig])
            portion = _np.sum([eig.value for eig in self.eig[:k]])
            return portion / total
        else:
            raise ValueError('Incorrect number of dimensions')
