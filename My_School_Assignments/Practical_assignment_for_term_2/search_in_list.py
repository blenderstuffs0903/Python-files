# Q.3
Avengers = ["iron man", "captain america", "thor", "hulk", "hawkeye",
            "black widow", "spider man", "vision", "scarlett witch"]

search = input("Enter the element you are searching for\n").lower()

if search in Avengers:
    print(search, "is an Avenger with index number", Avengers.index(search))
else:
    print(search, "is not an avenger.")
