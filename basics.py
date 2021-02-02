# David Allen
# Python Basics
# 2021-02-02

print("Hello world!")

a = 1
b = 1.0
s = "Hello world from a string"
t = 'Hello from a different string'

print(a, b, s, t) 

print(type(a)) # prints type, eg int, string
print(s[0]) # prints letter in s - placement 0 is H
print(s[0:2]) # string slice - shows characters between 0-2 (but not 2)
print(s[3:10:2]) # start at index 3, jump up 2 everytime until limit 10 - character 3, 5, 7 ,9

# lists
x = [1, 2, 3, 'Hello', 1.0]
print(x) # print x
print(x[0]) # print first number in x
print(x[2]) # print third number in x
print(x[-1]) # print index -1

for i in x: # for loop iterates over x array - x[::2] every second element from x / increments of 2
    print(i)
    print(i + i)


for i in range(10): # allocates single integer and updates
    print(i)

# dictionarys
d = {"no_wheels": 4, "model": "Skoda"}

print(d["no_wheels"]) # prints number of wheels
print(d["model"]) # print model

d["model"] = "Superb" # updates model
print(d["model"]) # print model

# list comprehensions - s is a list created from another list r
r = [1, 2, 3, 4]
print(r)
s = [i*i for i in r]
print(s)