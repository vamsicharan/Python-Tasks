# 11111
# 2222
# 333
# 44
# 5
rows=int(input("enter rows "))
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print((rows+1)-i,end="")
    print()