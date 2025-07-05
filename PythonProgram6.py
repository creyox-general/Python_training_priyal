'''

6)


A A A A A A A
A A
A A
A A
A
A A
A A
A A
A A A A A A A

'''

for i in range(9):
    if i == 0 or i == 8:
        for a in range(7):
            if a == 6:
                print("A ")
            else:
                print("A ", end="")
    elif i == 4:
        print("A")
    else:
        for c in range(2):
            if c == 1:
                print("A ")
            else:
                print("A ",end="")

