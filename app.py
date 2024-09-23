import random
import time

while True:
    value = random.randint(1, 10)
    print (f"Running... Value is {value}")
    if value == 5:
        print ("Oops! Something went wrong.")
        exit(1)
    time.sleep(5)