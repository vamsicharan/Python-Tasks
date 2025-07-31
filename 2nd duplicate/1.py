# Write a program that takes array of numbers are input, print the second duplicate number and it’s occurrence.
#
# Testcase1	:  [ 64, 1, 2, 7, 79, 7, 7, 1, 22]
# Output     	:  Second duplicate number is 7 and it is occurred 3 times
# Explanation	: In the given array [ 64, 1, 2, 7, 79, 7, 7, 1, 22],
# the second duplicate number is 7 and it is occurred for 3 times.

def Program(n):
    duplicates=[]
    items={}
    for char in n:
        if char not in items:
            items[char]=1
        else:
            items[char]+=1
    for key,value in items.items():
        if value>1:
            duplicates.append(key)
    return duplicates[1],items[duplicates[1]]
a=Program( [ 64, 1, 2, 7, 79, 7, 7, 1, 22])
print(a)