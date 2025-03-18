# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

wait_time=1 # start with 1 second
max_retries=5 # stop after 5 retries
attempts=0 # counter for attempts

while attempts < max_retries:
    print("Attempt", attempts +1, "- wait time", wait_time, "Seconds" )
    time.sleep(wait_time)
    wait_time *= 2 # Double the wait time
    attempts +=1
print ("Max retries reached. Stopping attempts.")
