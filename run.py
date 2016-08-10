from pinger import Pinger
from time import sleep


def main():
    p = Pinger(timeout=1)
    p.loop()
    sleep(5)
    p.stop()

if __name__ == "__main__":
    main()
