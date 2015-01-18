from sys import stdout as _stdout


class Progress:
    def __init__(self, length, endValue, char='█'):
        self.template = (
            '\b' * (length + 7) + char + '\x1b[32m{:<' +
            str(length) + '}\x1b[0m' + char + ' {:3d}%'
        )
        self.length = length
        self.value = 0
        self.endValue = endValue
        self.stepSize = endValue / length
        self.currentStep = 0
        self.currentPercent = 0
        self.char = char
        self._update()

    def setValue(self, value):
        self.value = value
        update = False
        if abs(
            self.value - (self.currentStep * self.stepSize)
        ) >= self.stepSize:
            self.currentStep = int(self.value / self.stepSize)
            update = True
        if abs(
            self.value - (self.currentPercent * (self.endValue / 100))
        ) >= 1:
            self.currentPercent = int(self.value * 100 / self.endValue)
            update = True
        if update:
            self._update()

    def increment(self, value=1):
        self.setValue(self.value + value)

    def finish(self, ended=True):
        if ended:
            self.value = self.endValue
            self.currentStep = self.length
        self._update()
        _stdout.write('\n')

    def _update(self):
        percent = int(self.value * 100 / self.endValue)
        _stdout.write(
            self.template.format(
                self.char * self.currentStep, self.currentPercent
            )
        )
        _stdout.flush()
