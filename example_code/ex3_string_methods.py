'''
There are also several string methods that we haven't gone over in detail but will use for this project:
- .upper() converts a string to uppercase (the opposite is .lower())
- .count(s) counts how many times the string s occurs inside of a larger string
'''
myString = 'Hello, World! 123'

print(myString.upper()) # HELLO, WORLD! 123
print(myString.lower()) # hello, world! 123
print(myString.count('l')) # 3

s = 'python is pythonic'
print(s.count('python')) # 2
