# even or odd numbers using for loop
for i in range(0,19):
    if i%2==0:
        print(i,"even")
    elif i%2==1:
        print(i,"odd")

# sum of even and odd numbers using for loop
a=0
b=0
for i in range(0,10):
    if i%2==0:
        a=a+i
    elif i%2==1:
        b=b+i
print(a)
print(b)