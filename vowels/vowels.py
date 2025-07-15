#vowels contrains

name="vamsicharanneelam"
vowels="aeiou"
result=""
result_con=""
for str in name:
    if str in vowels:
        print(str)
        result=result+str
    else:
        result_con+=str

print(result)
print(result_con)