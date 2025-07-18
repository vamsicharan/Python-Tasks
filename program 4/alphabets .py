#10.wap to get only alphabets from a string using for loop in reverse direction and store them in empty string and find alphabets count?

str=input("Enter a string: ")
result=""
for rev in range (len(str)-1,-1,-1):
    if str[rev].isalpha() :
        result+=str[rev]
print(result,len(result))