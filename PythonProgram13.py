'''
13)
#  Program to sort alphabetically the words form a string provided by the user
'''

str = input("string = ")
l = len(str)
y = str
list = []
for i in range(l):
    x = y[:1]
    y = str[i+1:]
    list.append(x)
#print(list)
list.sort()
#print(list)
for j in list:
    print(j, end="")
