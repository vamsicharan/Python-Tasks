row=5
for i in range(1,row+1):
    a=97
    A=65
    print(" "*(row-i),end="")
    for j in range(1,i+1):
        if i<2:
            print("*"*j,end="")
        elif i==2:
            print(j,end="")
        elif i==3:
            print(chr(a),end="")
            a+=1
        elif i==4:
            print(chr(A),end="")
            A+=1
        elif i==5:
            print("@",end="")
    print()