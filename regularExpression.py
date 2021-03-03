import re
# import regular expression - known as RegEx

# dont seperate a + b - a+b+ creates the object to search for - '+' requires at least one occurance
myre = re.compile('a+b+')

# array
examples = ['ab', 'aab', 'abb', 'aaabbb', 'ca', 'abab', 'baa', 'bba', 'bbbaaa', 'ac']

# searching for pattern matches - myre matching anything in example array
for e in examples:
    if myre.match(e):
        ismatch = True
    else:
        ismatch = False
    print(f"{e} -> {ismatch}")