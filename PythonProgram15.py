'''
15) Please write
 a program
 which accepts a string from console and print it in reverse order.

'''
str = input()
length = len(str)
for i in range(length-1,-1,-1):
    print(str[i],end="")



