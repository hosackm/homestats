from __future__ import print_function
from subprocess import check_output, CalledProcessError
from threading import Thread
import time
import re


class Pinger(object):
    def __init__(self, domain="www.google.com", timeout=5):
        self.domain = domain
        self.timeout = timeout
        self.kill = True
        self.lastrun = (time.ctime(), 0)

    def ping(self):
        cmd = "ping -n 1 {}".format(self.domain)
        try:
            out = check_output(cmd, shell=True)
        except CalledProcessError:
            out = "timeout or unresponsive domain"
        finally:
            return out

    def parse(self, s):
        ms = re.findall("Maximum = (\d+)ms", str(s))
        try:
            ms = int(ms[0])
        except (IndexError, ValueError):
            return -1
        else:
            return ms

    def loop(self):
        t = Thread(target=self._loop)
        t.start()

    def display(self):
        print("{}: took {} ms".format(*self.lastrun))

    def _loop(self):
        self.kill = False
        while not self.kill:
            t = time.ctime()

            resp = self.ping()
            ms = self.parse(resp)

            self.lastrun = (t, ms)
            self.display()

            time.sleep(self.timeout)

    def stop(self):
        self.kill = True


if __name__ == "__main__":
    p = Pinger()
    p.loop()
    time.sleep(10)
    p.stop()
