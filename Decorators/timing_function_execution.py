# Problem: Write a decorator that measures the time a function takes to execute.

import time
from unittest import result

def timer(func):
    def wrapper (*args, **kwargs):

        start = time.time()
        result=func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} run in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)