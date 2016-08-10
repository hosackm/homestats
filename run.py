from pinger import Pinger
from time import sleep


def main():
    p = Pinger(timeout=5)
    p.loop()
    while True:
        try:
            sleep(1)
        except KeyboardInterrupt:
            break
    p.stop()

if __name__ == "__main__":
    main()
