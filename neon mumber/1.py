# neon number
number = int(input("number: "))
neon= number** 2
sum_neon= 0
while neon > 0:
    n = neon % 10
    sum_neon += n
    neon = neon // 10
if sum_neon == number:
    print("neon number")
else:
    print("not neon number")