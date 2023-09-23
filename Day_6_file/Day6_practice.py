def my_function():
    print("hello", end=" ")
    print("world")


my_function()


def mul_table(n):
    if n.isdigit():
        n = int(n)

    while type(n) is str:
        n = input("Enter a valid number").strip()
        if n.isdigit():
            n = int(n)
    for i in range(1, 11):
        print(n, "×", i, "=", n * i)


t = input("Enter the number\n").strip()
mul_table(t)



