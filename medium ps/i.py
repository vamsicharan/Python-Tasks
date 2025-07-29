def Program(even_number):
    vowels="aeiouAEIOU"
    length_even=len(even_number)
    result= length_even // 2
    result1=""
    result2=""
    for i in  range(0,result):
        if even_number[i] in vowels:
            result1+=even_number[i]
    for j in range(result,length_even):
        if even_number[j] in vowels:
            result2+=even_number[j]
    if len(result1) == len(result2):
        return True
    else:
        return False
A=Program("rebels")
print(A)