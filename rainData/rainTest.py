def eachYear(num):
    start = int(2013)
    source2 = open("rainByYear.txt", "w")
    for i in range(0,num):
        ByYear = []
        for j in range(0, len(linesList)):
            ByYear.append(float(linesList[j][i]))
        print(len(ByYear))
        ByYearStr = str(ByYear)
        line = str(start+i) + " : "+ ByYearStr[1:len(ByYearStr)-1] + "\n"
        source2.write(line)
    source2.close()

source = open("rainDropXinwu.txt", "r")

lines = source.readlines()
linesList = []
for line in lines:
    line = line.rstrip("\n")
    lineList = line.split(",")
    linesList.append(lineList)

eachYear(5)






'''


'''

'''
rainString = ""
for line in lines:
    line = line.replace("\n", ",")
    print(line)
    rainString += line
print("After replace ",lines)
print("String = ",rainString)

rainString = rainString.split(',')
print('Replace , String = ', rainString)
'''

'''
for line in source:
    line = source.readline()
    line = line.replace("\n",",")
    rain += line
    n += 1
rain = rain.split(",")

'''

