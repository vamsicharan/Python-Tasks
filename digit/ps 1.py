"""Write a program to check whether the sum of digits in the number except   
first digit and digit is equal to the sum of first digit and last digit of that  
number. If both the sums are equal then print equal otherwise print not  
equal """  

num = 75547
temp = "75547"
sumFL = 0
sumRE = 0
for i in range(len(temp)):
    if i == 0:
        sumFL += int(temp[i])
    elif i == len(temp)-1:
        sumFL += int(temp[i])
    else : 
        sumRE += int(temp[i])
if sumFL == sumRE :
    print("equal",sumFL,sumRE)
else :
    print("NOT EQUAL")