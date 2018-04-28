def f1():
    x = 123
    y = 12345
    def f2():
        print(x)
    print(y)
    return f2

f1()

a = f1() # output return f2

a()
