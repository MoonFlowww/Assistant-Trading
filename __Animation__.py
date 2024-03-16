import threading
import time
import sys

animation = "|/-\\"
start_time = time.time()

def ProcessAnimation(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(5):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
    sys.stdout.write('\b \b')
    sys.stdout.flush()

def RunWithAnimation(func, *args):
    animation_thread = threading.Thread(target=lambda: func(*args))
    animation_thread.start()
    animation_thread.join()