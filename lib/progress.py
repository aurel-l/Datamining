from sys import stdout as _stdout

class Progress:
    def __init__(self, length, endValue):
        self.template = '\b' * (length + 7) + '[\x1b[32m{:<' + str(length) + '}\x1b[0m] {:3d}%'
        self.length = length
        self.value = 0
        self.endValue = endValue
        self.stepSize = endValue / length
        self.currentStep = 0
        self.currentPercent = 0
        self.__update__()
    
    def increment(self, value = 1):
        self.value += value
        update = False
        if (self.value - (self.currentStep * self.stepSize)) >= self.stepSize:
            self.currentStep = int(self.value / self.stepSize)
            update = True
        if (self.value - (self.currentPercent * (self.endValue / 100))) >= 1:
            self.currentPercent = int(self.value * 100 / self.endValue)
            update = True
        if update:
            self.__update__()
    
    def finish(self, ended = True):
        if ended:
            self.value = self.endValue
            self.currentStep = self.length
        self.__update__()
        _stdout.write('\n')
    
    def __update__(self):
        percent = int(self.value * 100 / self.endValue)
        _stdout.write(self.template.format('#' * self.currentStep, self.currentPercent))
