#  Question 2: Vowels from Odd Index in Sentence
# Task: - Given a sentence - Pick characters at odd indices only - From those, extract vowels - Concatenate
# those vowels and find length
def new_list(values,vowels):
    result=""
    for value in range(len(values)):
        if type(values[value]) == str and values[value] != " ":
            if value %2==1 and values[value] in vowels:
                result += values[value]
    return result
obj = new_list("characters at odd indices only","aeiouAEIOU")
print(obj)
