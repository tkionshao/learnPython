def maker():
    list = []
    for i in range(5):
        list.append(lambda x: i**x)
    return list

f1 = maker()
print(f1[0](2))

print(f1[1](2))

print(f1[2](2))

print(f1[3](2))

