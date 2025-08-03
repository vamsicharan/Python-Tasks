#  Question 1: Name Vowels from Long Names
#  Task: - List of 5 people - Check names with length > 5 - Extract vowels from those names - Store vowels in a
# new list

def new_list(values,vowels):
    result=[]
    for value in values:
        if len(value) > 5:
            for char in value:
                if char in vowels:
                    result.append(char)
    return result
obj = new_list(["vamsi","charan","govardhan","hemanth"],"aeiouAEIOU")
print(obj)