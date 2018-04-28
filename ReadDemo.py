




'''
print('-----1-----')

file = open('Ibanez_orginal_text.txt','r',encoding='utf-8')
for link in file:
    # link = file.readline()
    link = link.rstrip()
    print(link)

# file.next()
'''
'''
print('-----2-----')
for link in open('Ibanez_orginal_text.txt'):
    print(link)
'''

print('-----3-----')

t = range(2,12,2)
for i in t:
    print(i)

s = [ i*10 for i in t]
print(s)

print('-----4-----')
name = ('x', 'y', 'z', 'w')
num = (1, 2, 3)

x = list(zip(name, num))
print(x)

y = dict(zip(name, num))
print(y)

for key in y:
    print(y[key], "This is it")

print('-----5-----')
list = [1,2,3,4,3,321,2,4,"a",'b','c']
list = [x for x in list if x in range(0,9) ]
print(list)






