import sys
import time
def progress_bar():
    for i in range(1, 101):
        print("\r", end="")

        print("Download progress: {}%: ".format(i), "▋" * (i // 2), end="")

        sys.stdout.flush()

        time.sleep(0.04)


if __name__ == '__main__':
    progress_bar()