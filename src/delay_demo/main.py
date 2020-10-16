import time


def cli():
    try:
        for i in range(15):
            print(i, flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("delay-demo caught the KeyboardInterrupt, yay!")
