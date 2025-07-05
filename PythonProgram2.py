'''
2)

str = 'What is Lorem Ip
sum Lorem Ipsum is simpl
y dummy text of the print

ing and typesetting indust
ry Lorem Ipsum has been th
e industry's standard dummy
text ever since the 1500s wh
en an unknown printer took a
galley
Of
 type and scrambled it to make a type specimen book it has? '

find total occurance of each letter = ‘aeiou’

'''

str = "What is Lorem Ip sum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry's standard dummy text ever since the 1500s when n unknown printer took a galley Of type and scrambled it to make a type specimen book it has?"

a=0
for x in str:
    if x =='a':
        a=a+1
print('a =',a)

e=0
for x in str:
    if x =='e':
        e=e+1
print("e =",e)

i=0
for x in str:
    if x =='i':
        i=i+1
print("i =",i)

o=0
for x in str:
    if x =='o':
        o=o+1
print("o =",o)

u=0
for x in str:
    if x =='u':
        u=u+1
print('u =',u)
