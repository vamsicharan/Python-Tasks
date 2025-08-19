# +1
# ++12
# +++123
# ++++1234

for i in range(1,5):
    print("+"*i,end="")
    for j in range(1,i+1):
        print(j,end="")
    print()