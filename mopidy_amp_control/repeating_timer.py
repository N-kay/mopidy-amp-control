from threading import Timer

class RepeatingTimer():

    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs

        self.timer = Timer(self.interval, self.callback)

    def callback(self):
        self.function(*self.args, **self.kwargs)
        self.start()

    def cancel(self):
        self.timer.cancel()

    def start(self):
        self.timer.cancel()
        self.timer = Timer(self.interval, self.callback)
        self.timer.start()
