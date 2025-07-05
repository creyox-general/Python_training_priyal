'''
1) # Program to add two matrices using nested loop
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

Z = [[0,8,4],
    [6,9,3],
    [9,1,9]]

Result Matrix = 3Y + (X + 2Y) + (5Z + 4X)
'''

x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]
z = [[0, 8, 4], [6, 9, 3], [9, 1, 9]]


def addition(array1, array2):
    sum = []
    for i in range(len(array1)):
        row = []
        for j in range(len(array1[0])):
            row.append(array1[i][j] + array2[i][j])
        sum.append(row)

    return (sum)


def multiplication(array1, n):
    mul = []
    for i in range(len(array1)):
        row = []
        for j in range(len(array1[0])):
            row.append(array1[i][j] * n)
        mul.append(row)

    return (mul)


result_matrix = addition(addition(multiplication(y, 3), addition(x, multiplication(y, 2))),
                         addition(multiplication(z, 5), multiplication(x, 4)))



print(result_matrix)

# 3Y + (X + 2Y) + (5Z + 4X)





