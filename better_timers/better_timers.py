from threading import Thread, Timer as threadTimer
from pygame import event as pyEvent
from math import floor

# By Gudni Natan Gunnarsson, 2017


class Timer(object):
    def __init__(self, event, rate):
        self.__running = False
        self.__event = event
        self.__rate = rate
        self.__t = None

    def eventPoster(self, event, rate):
        e = pyEvent

        def post(event):
            if self.__running and self.__rate == rate:
                if type(event) is e.EventType:
                    e.post(event)
                else:
                    e.post(e.Event(event))
                postThread.run()
                if not postThread.daemon:
                    postThread.daemon = True

        postThread = threadTimer(float(rate - 1) / 1000.0, post, args=(event,))
        postThread.daemon = True
        postThread.start()

    def start_timer(self):
        if not self.__running:
            self.__t = Thread(
                target=self.eventPoster,
                args=(self.__event, self.__rate)
            )
            self.__t.daemon = True
            self.__running = True
            self.__t.start()

    def stop_timer(self):
        if self.__running:
            self.__running = False
            self.__t.join()

    def change_rate(self, rate):
        self.__rate = rate

        self.stop_timer()
        self.start_timer()

    def get_event(self):
        return self.__event


class BetterTimers():
    def __init__(self):
        self.__timers = list()

    def set_timer(self, event, rate, delay=0):
        if floor(delay) > 0:
            delayTimer = threadTimer(
                float(delay - 1) / 1000.0,
                self.set_timer,
                args=(event, rate)
            )
            delayTimer.daemon = True
            delayTimer.start()
            return

        t = Timer(event, rate)
        for e in self.__timers:
            if e.get_event() == event:
                if floor(rate) > 0:
                    e.change_rate(rate)
                else:
                    e.stop_timer()
                    self.__timers.remove(e)
                return
        if floor(rate) > 0:
            t.start_timer()
            self.__timers.append(t)

    def end_all_timers(self):
        for t in self.__timers:
            t.stop_timer()

        self.__timers = list()

timers = BetterTimers()
