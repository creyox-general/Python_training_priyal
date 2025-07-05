'''

4) Sort the values of first list using second list

Input : list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

Output :['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']
'''

list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
dic = {}
for x in range(len(list2)):
    if list2[x] == 0:
        dic.setdefault('0', []).append(list1[x])
    if list2[x] == 1:
        dic.setdefault('1', []).append(list1[x])
    if list2[x] == 2:
        dic.setdefault('2', []).append(list1[x])

output = []
output.append(dic.get('0'))
output.append(dic.get('1'))
output.append(dic.get('2'))

output1 = [j for i in output for j in i]
print(output1)

