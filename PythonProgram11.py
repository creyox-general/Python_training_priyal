'''
11. From a given list of natural numbers, return the two closest numbers.

Input = [3, 9, 50, 15, 99, 7, 98, 65]
Output = [98,99]

'''

list = [3, 9, 50, 15, 99, 7, 98, 65]
list.sort()

minimum = list[1]-list[0]

for i in range(len(list)-1):
    diff = abs(list[i] - list[i+1])
    if minimum > diff:
        min1 = list[i]
        min2 = list[i+1]
print("Closest Number =",min1,",",min2)
