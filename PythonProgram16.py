'''
16) get one string input and take an
other
string input untile that do not match with old string using while loop
'''
str = input("string1 = ")

while 1:
    str2 = input("string2 = ")
    if len(str) == len(str2):
        if str == str2:
            print("string matched")
            break

