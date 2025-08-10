row=5
a=5
for i in range(1,row-1):
    print("*"*i,end="")
    print(" "*((a-i)+2),end="")
    a-=1
    for j in range(1,i+1):
        print("*",end="")
    print()
row=4
a=4
for i in range(row,0,-1):
    print("*"*i,end="")
    print(" "*((a-i)),end="")
    a+=1
    for j in range(i,0,-1):
        print("*",end="") 
    print()  