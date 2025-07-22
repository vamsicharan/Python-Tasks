num=int(input("enter num"))

# Fibonacci Sequence Generator
def  fibonacci(n,a=0,b=1,sequence=None):
    if sequence is None:
        sequence = []
    if n <= 0:
        return sequence
    sequence.append(a)
    return fibonacci(n-1, b, a+b ,sequence) 
obj= fibonacci(num, sequence = [])
print(obj)