'''

7) Take number inputs from users till he press "q" key, after that print

Minimum Number
Maximum Number
Closest Number
Longest Number
Total Sum
Average Of All


input 1,12,45,7,56

Minimum Number: 1
Maximum Number: 56
Closest Numbers :7,12
Longest Number: 1,56
Total Sum: 121
Average Of All : 24.20

'''

list = []
q=1
while (q == 1):
    x = input("enter")
    if x == 'q':
        q=0
    else:
        if x.isalpha():
            print("invalid")
        else:
            y = int(x)
            list.append(y)
#print(list)
#--------------------------------------------------------------------------------------
min_num = min(list)
print ("Minimum Number : ",min_num)
#--------------------------------------------------------------------------------------
max_num = max(list)
print("Maximum Number : ",max_num)
#--------------------------------------------------------------------------------------
sum1 = 0
for i in list:
    sum1 = sum1 + i
print("Total Sum : ",sum1)
#--------------------------------------------------------------------------------------
length = len(list)
avg = sum1/length
print("Average if all : ",avg)
#--------------------------------------------------------------------------------------
list.sort()
#print(list)
minimum = list[1]-list[0]

for p in range(len(list)-1):
    diff = abs(list[p] - list[p+1])
    if minimum > diff:
        min1 = list[p]
        min2 = list[p+1]
print("Closest Number =",min1,",",min2)
#-------------------------------------------------------------------------------------
maximum = list[1]-list[0]

for q in range(len(list)-1):
    diff1 = abs(list[q]-list[q+1])
    if maximum < diff:
        max1 = list[q]
        max2 = list[q+1]
print("Longest Number =",max1,",",max2)













