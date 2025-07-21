# Armstrong Number Checker
def armstrong():
    number= input("Enter a number: ")
    sum=0
    for digit in number:
        sum += int(digit) ** len(number)
    if sum == int(number):
        return "armstrong  number"
    else:
        return "not an armstrong number"
obj=armstrong()
print(obj)