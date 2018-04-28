def maker(*x):
    list=[]
    for num in x:
        list.append(num**2)
    print(list)

maker(1,2,3,4,5)

def maker2(**x):
    # print(x.key("a"))
    print(x["a"])
    print(x)

maker2(a=5)

def maker3(*args):
    reg = list(args)
    print(reg)

maker3(1,3,4,5,6,6)


def maker4(x):
    x += 5
    return x

try:
    maker4()
except:
    print("Shut your mouse bitch")


def maker5(compare,*args):
    return 8

def equalToOne(x,y):
    print("Critical")
    return x > y

equalToOne(1,2)
ls = [1,2,3,4,5,6,67]

print(list(map(maker4,ls)))