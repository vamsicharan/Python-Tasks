# wap to find a number is prime number r not
number = int (input("enter number:--  "))
value = True
if number <=1:
    print("not a prime  and not a composite")
else:
    for i in range(2,number):
        if number % i ==0:
            value= False
            break
    if value == True:
        print("prime")
    else:
        print("not prime")