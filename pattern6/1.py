row=5
a = 5
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print(" " * ((a * 2 - 2)), end="")
    a -= 1
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# *      *
# **    **
# ***  ***
# ********