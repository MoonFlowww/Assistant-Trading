import time
import sys

animation = "|/-\\"
start_time = time.time()
def ProcessAnimation():
    while True:
        for i in range(4):
            time.sleep(0.212)  # Feel free to experiment with the speed here
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > 4:  # The animation will last for 10 seconds
            break
    #sys.stdout.write("\r -> Program Killed Successfully !")