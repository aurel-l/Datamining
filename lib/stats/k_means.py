import numpy as _np


class _Step:
    def __init__(self, classes, n_loops, changes):
        self.classes = classes
        self.n_loops = n_loops
        self.converged = (changes == 0)
        self.changes = changes


# Initialization function
def _initialization(data, k, useElements, useQuasiRandom):
    #barycenters = _np.zeros((k, data.shape[1]))
    if useElements:
        if useQuasiRandom:
            #k-means++
            barycenters = _np.zeros((k, data.shape[1]), dtype=_np.float64)
            lenData = data.shape[0]
            available = _np.ones(lenData, bool)
            for i in range(k):
                if i == 0:
                    weights = _np.ones(lenData, dtype=_np.float64) / lenData
                else:
                    weights = (
                        (barycenters[i - 1, :] - data) ** 2
                    ).sum(1) * available
                    weights /= weights.sum()
                choice = _np.random.choice(lenData, 1, False, weights)
                available[choice] = False
                barycenters[i, :] = data[choice]
        else:
            #default
            barycenters = data[_np.random.choice(data.shape[0], k, False)]
    else:
        minValues, maxValues = data.min(0), data.max(0)
        deltaValues = maxValues - minValues
        if useQuasiRandom:
            raise('Not Implemented Yet')
            #dimensions = data.shape[1]
            #side = int(_np.ceil(k ** (1 / dimensions)))
            #nHyper = side ** dimensions
            #hypercube = _np.empty((nHyper, dimensions))
            #iHyper = 0
            #i = 0
            #for comb in _np.ndindex(tuple([side for _ in range(side)])):
            #    i = _np.round(iHyper / k
            #
            #    iHyper += 1
            #not correct
            #for i in range(data.shape[1]):
            #    barycenters[:, i] = _np.arange(
            #        minValue, maxValue, (maxValue - minValue) / (k + 1)
            #    )[1:]
        else:
            #random values in value space
            barycenters = (
                _np.rand(k, data.shape[1], dtype=_np.float64) * deltaValues
            ) + minValues
    return barycenters


def _min_distance(item, others):
    return _np.argmin(_np.sqrt(((item - others) ** 2).sum(1)))


def k_means(data, k, useElements=True, useQuasiRandom=False, useMedoids=False):
    lenData = data.shape[0]
    # Initialization step
    barycenters = _initialization(data, k, useElements, useQuasiRandom)
    n_loops = 0
    changes = lenData
    classes = _np.zeros(
        lenData,
        dtype=getattr(_np, 'uint{}'.format((int(int(_np.log2(k))/8)+1)*8))
    )
    classChanges = _np.ones(k, bool)
    while changes != 0:
        # Assignement step
        changes = 0
        for i in range(lenData):
            newClass = _min_distance(data[i, :], barycenters) + 1
            if classes[i] != newClass:
                changes += 1
                classChanges[classes[i] - 1] = True
                classChanges[newClass - 1] = True
                classes[i] = newClass
        # Update step
        if changes:
            for classIndex in [
                i for i in _np.arange(1, k + 1) if classChanges[i - 1]
            ]:
                classItems = data[classes == classIndex]
                mean = classItems.mean(0)
                if useMedoids:
                    bar = classItems[_min_distance(mean, classItems)]
                else:
                    bar = mean
                barycenters[classIndex - 1] = bar
        # Partial result
        n_loops += 1
        yield _Step(classes, n_loops, changes)
