# Here "name" is the parameter
def greet(name):
    print(f"hello {name}")
    print(f"How do you do? {name}")
    print(f"Isn't the weather nice today? {name}")


# here "Dinku" is the argument
greet("Dinku")


# functions more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it likes in {location}")


# greet_with('dinku', 'India')

# keyword arguments
greet_with(location="India", name="Dinku")



