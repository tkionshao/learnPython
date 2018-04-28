import math

print("--------\n")

_num = int(input("The highest number is? "))

for num in range(1, _num):
    num = str(num)

    numlist = list(num)
    # print(numlist,type(numlist))

    length = int(len(numlist))
    # print("length=",length)


    sum = 0
    for x in numlist:
        x = int(x)
        sum += math.pow(x,length)


    if sum == int(num):
        print("%s is a perfecrt number" % num)

    else: continue
