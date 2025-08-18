import random
def randomquotes():
    quotes = [
        {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
        {"quote": "Innovation distinguishes between a leader and a follower.", "author": "Steve Jobs"},
        {"quote": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
        
    ]
    genarator=random.choice(quotes)
    return genarator
 
a=randomquotes()
print(a)    