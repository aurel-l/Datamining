from sys import stdout as _stdout


class Progress:
    """
    Object to display a progress bar to stdout
    """
    def __init__(self, length, end_value, char='█'):
        """
        :param length: length (in chars) of the inner part of the progress bar
        :type length: int
        :param end_value: final value of the progress bar
        :type end_value: int
        :param char: character used for the progress bar
        :type char: str
        """
        self.template = (
            '\b' * (length + 7) + char + '\x1b[32m{:<' +
            str(length) + '}\x1b[0m' + char + ' {:3d}%'
        )
        self.length = length
        self.value = 0
        self.end_value = end_value
        self.step_size = end_value / length
        self.current_step = 0
        self.current_percent = 0
        self.char = char
        self._update()

    def set_value(self, value):
        """
        Sets the value of the progress bar to a specified value
        :param value: value to use to set the progress bar
        :type value: int
        """
        self.value = value
        update = False
        if abs(
            self.value - (self.current_step * self.step_size)
        ) >= self.step_size:
            self.current_step = int(self.value / self.step_size)
            update = True
        if abs(
            self.value - (self.current_percent * (self.end_value / 100))
        ) >= 1:
            self.current_percent = int(self.value * 100 / self.end_value)
            update = True
        if update:
            self._update()

    def increment(self, value=1):
        """
        Increments the value of the progress bar by specified value
        :param value: value to use to increment the progress bar
        :type value: int
        """
        self.set_value(self.value + value)

    def finish(self, ended=True):
        """
        Frees the line used by the progress bar
        :param ended: specifies if the progress has to end to its final value
        :type ended: bool
        """
        if ended:
            self.value = self.end_value
            self.current_step = self.length
        self._update()
        _stdout.write('\n')

    def _update(self):
        percent = int(self.value * 100 / self.end_value)
        _stdout.write(
            self.template.format(
                self.char * self.current_step, self.current_percent
            )
        )
        _stdout.flush()
