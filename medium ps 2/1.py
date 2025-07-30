# Write a program that takes array of numbers as input, among the numbers in array,
# check how many numbers starts with the same digit and ends with the same digits.
# Print the count of such kind of numbers in the given array.
# Testcase1	:  [ 34, 88, 423, 121, 2382, 10]
# Output     	:  3

def array_numbers(list_array):
    count = 0
    for item in list_array:
        result=str(item)
        if result[0]==result[-1]:
            count += 1
    return count
A=array_numbers([ 34, 88, 423, 121, 2382, 10])
print(A)