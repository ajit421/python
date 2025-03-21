# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
import random

def greet(name="User"):
    return "Hello, " + name + "!"

name = "jito"

# Check if a name is provided.
if name:
    # If a name is provided, greet the user with that name.
    print(greet(name))

else:
    names = ["Ajit", "Golden", "Newuser"]
    # random name from the list.
    name = random.choice(names)

    print(greet(name))
