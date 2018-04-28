

source = open("rainDropXinwu.txt", "r")
rain = ""
n = 0
for line in range(0,1000):
    line = source.readline()
    line = line.replace("\n",",")
    rain += line
    n += 1
    print(rain)

print(n)

file = open("rainPy.txt", "w", encoding="utf-8")
file.write(rain)
file.close()

rain = rain.split(",")

print(rain.index(""))
rain.pop(1830)


print(rain)
print(len(rain))

'''
for i in range(len(rain)):
    print(rain[i])
'''

'''
for day in words:
    print(day)

'''
