#  Count Occurrences of a Character
# Question: Write a function that counts the occurrences of a specific character in a string. "hello world", "l"

def digit (char):
    count = 0
    for i in char:
        if i == "l":
            count +=1
    return count
values=digit("hello world")
print(values)