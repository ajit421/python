# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
print_kwargs(name="shaktiman")
print_kwargs(name="suparman")
print_kwargs(power="lazer")
print_kwargs(other="zero")
