
sum = 0
def fun(n):
    sum = 0
    sum += n
    if n == 1:
        return 1
    else:
        return sum + fun(n-1)



a = fun(10)

print(a)