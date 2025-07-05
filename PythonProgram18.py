'''
I am having an list [1,2,3,4,5,6,7,8,9,10,11,12,13].
Now i am creating a function that returns if the input is a valid sequence or not, but i
have some exceptions that need to be resolved.

1. Input will always be in a sorted manner.
2. Function should return true or false.
3. input length should be >= 3 and < 14. from (numbers 1 to 13)

Examples.
	[1,2,3] - true
	[1,2,3,4,5] - true
	[8,9,10,11] - true
	[11,12,13] - true

	Exceptions.
	[1,11,12,13] - false
	[1,8,9,10,11,12,13] - false
	[1,4,5,6] - false
	[1,3,4,5] – false

'''
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
list2 = []
print("Press 'a' to terminate.")
for i in range(13):
    x = input("Number")
    if x == 'a':
        break
    list2.append(int(x))
print(list2)
k=0
f = 0
for j in range(13):
    #print(list2[0],list1[j])
    if (int(list2[0]) == list1[j]):
        for k in range(len(list2)):
            #print(list2[k],list1[j])
            if list2[k] == list1[j]:
                j = j + 1
            else:
                print("false")
                f = 1
                break
if f == 0:
    print("true")





