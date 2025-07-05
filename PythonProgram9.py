'''
9. Given a string, take the last char and return a new string with the last char added at the
front and back, so "cat" yields "tcatt". The original string will be length 1 or more.
backAround("cat") → "tcatt"
backAround("Hello") → "oHelloo"
backAround("a") → "aaa"
'''
str = input("enter string =")
l = len(str)
last = str[l-1:]
#print(l,last)
output = last + str + last
print(output)