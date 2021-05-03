# Project: Graph Theory 2021

### Description
This program is a programming exercise for the module 'Graph Theory' in 3rd year Software and Developement. The aim of the project is to be able to search a text file using a regular expression. Created using the Python 3 programming language.

### Instructions
Running the program
```bash
git clone https://github.com/allend4/Graph_Theory_Project
```
```bash
cd Graph_Theory_Project
```
```bash
cd Project
```
```bash
Python main.py
```

The program will automatically load the menu.
The menu will promt the user enter a string to search, run various test, search a sample text or quit. 
The program wil return if the string matches or doent not match the regular expression.

### Explanation.
My project is a blend of the labs we done over the semester. The main algorithm used in my project are the shunting yard algorithm and the Thompsons construction algorithm.
Together the shunting yard algorithm takes a regular expression and puts  it into an output which is ordered. The *infix* is converted into the *postfix* by precedence. Thompson’s construction transforms a regular expression into an NFA. The NFA is used to match strings.

### What is a regular expression?
A regular expression, sometimes known as  *RegEx*  is a sequence of characters that form a search pattern. Regular expressions are used all throughout the world and are built into to all programming languages such as Python, that has been used for this project.
RegEx is not a programming language but is a term for the theory used to describe regular languages. Regular expressions can be simple and complicated, depending on its use, such as searching, manipulating and editing. From searching words in a text document, to being used in google analytics to match patterns.Even email validation and passwords are a few areas of strings where Regex are widely used to define the constraints.

**Regex**
- ' ^ ' - The beginning of a line.
- ' . ' - Any character.
- ' | ' - The OR operator.
- ' ? ' - Matches the character before the '?' (zero OR one).
- ' + ' - Matches character before '+' (one OR more).
- ' * ' - Matches everyhting in place of the Kleene Star.

### How do regular expressions differ across implementations?
there are two implementations of regular expression. DFA - Deterministic Finite Automaton and NFA - Nondeterministic Finite Automaton.

**What is an automaton?** An automaton performs a range of functions according to a predetermined set of coded instruction. Expressions known as regular expressions are the are the language accepted by infinite automata.

**DFA?** Descrived as one machine. There is only one path for the specific input from the current state to the next. All DFA are NFA.

**NFA?** Described as multiple small machines. There are many paths for the specific input from the current state to the next. Not all NFA are DFA..

### Can all formal languages be encoded as regular expressions?
The short answer is Yes. A formal language is basically a string. Regular expressions are encoded to search strings. Therefore, regular expressions can be used in all formal languages. Regular expression can be as basic and as complicated as you want to make them. their use may be simple or overly complicated, but the main thing to notice is that they can be used. 


### References
- Main poin of reference - -Ian McLoughlin
- For other reference see Research.txt under Doc's
