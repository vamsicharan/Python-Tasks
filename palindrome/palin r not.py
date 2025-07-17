# palindrome

name="markram"
result=""
for i in range(len(name)-1,-1,-1):
    result=result+name[i]
if result==name:
  print(f"{name} is palindrome")
else:
     print(f"{name} is not a palinrome")
