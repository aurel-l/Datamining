import multiprocessing as _mp


class Worker:
    def __init__(self, target, args, duplex=False):
        self.duplex = duplex
        [pipeFrom, self.pipeInto] = _mp.Pipe(duplex=self.duplex)
        self.process = _mp.Process(target=target, args=args + [pipeFrom])
        self.process.start()

    def feed(self, value):
        self.pipeInto.send(value)

    def retrieve(self):
        if self.duplex:
            return self.pipeInto.recv()

    def join(self):
        self.pipeInto.close()
        self.process.join()
