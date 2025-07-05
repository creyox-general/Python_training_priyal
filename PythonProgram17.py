'''
Sorted dic sequence wise

INPUT : dic1 = {‘list1’ : {‘id’: 123 ,’name’: ‘ABC’ , sequence: ‘5’},

list2’ : {‘id’: 124 ,’name’: ‘DEF’ , sequence: ‘4’},

list3’ : {‘id’: 125 ,’name’: ‘XYZ’ , sequence: ‘1’},

list4’ : {‘id’: 126 ,’name’: ‘MNO’ , sequence: ‘3’},

list5’ : {‘id’: 127 ,’name’: ‘PQR’ , sequence: ‘2’}}


OUTPUT :
dic1 = { list3’ : {‘id’: 125 ,’name’: ‘XYZ’ , sequence: ‘1’},
list5’ : {‘id’: 127 ,’name’: ‘PQR’ , sequence: ‘2’},

list4’ : {‘id’: 126 ,’name’: ‘MNO’ , sequence: ‘3’},

list2’ : {‘id’: 124 ,’name’: ‘DEF’ , sequence: ‘4’},

‘list1’ : {‘id’: 123 ,’name’: ‘ABC’ , sequence: ‘5’}}


'''

dic1 = {'list1' : {'id': 123 ,'name': 'ABC' , 'sequence': '5'},'list2' : {'id': 124 ,'name': 'DEF' , 'sequence': '4'},'list3' : {'id': 125 ,'name': 'XYZ' , 'sequence': '1'},'list4' : {'id': 126 ,'name': 'MNO' , 'sequence': '3'},'list5' : {'id': 127 ,'name': 'PQR' , 'sequence': '2'}}
dic2 = {}

for i in dic1:
    for j in dic1[i]:
        if dic1[i][j] == '1':
            dic2.update({ i : dic1[i]})
for i in dic1:
    for j in dic1[i]:
        if dic1[i][j] == '2':
            dic2.update({ i : dic1[i]})
for i in dic1:
    for j in dic1[i]:
        if dic1[i][j] == '3':
            dic2.update({ i : dic1[i]})
for i in dic1:
    for j in dic1[i]:
        if dic1[i][j] == '4':
            dic2.update({ i : dic1[i]})
for i in dic1:
    for j in dic1[i]:
        if dic1[i][j] == '5':
            dic2.update({ i : dic1[i]})
print(dic2)


