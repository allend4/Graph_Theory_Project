import shuntingre
import thompson
import argparse

# argparse
parser = argparse.ArgumentParser(description='program to search a text file, using a regular expression',)
parser.add_argument('-ix', "--inputInfix", help="This is the infix that will be compared to the string")
parser.add_argument('-s', "--string", help="This is the string that will be matched to the infix")
parser.add_argument('-v', '--version', action='version',version='Alpha v1.1', help="Display programs version number")
parser.add_argument('-i', '--info', action='version',version='David Allen, Graph Theory Project 2021', help="Information about the developer")
parser.parse_args()

# menu
def menu(): # menu input
    print("===============GraphTheory===============")
    print("|\t(David Allen - G00375372)\t|")
    print("=========================================")
    print("1. User inputs ")
    print("2. Run test samples")
    print("3. Run sample.txt file")
    print("4. Exit")

loop=True # loop = true until loop = false

# user input matching
def userInput():

    inputInfix = input("Enter an infix :")
    inputString = input("Enter a string to match :")

    if __name__ == "__main__":
        tests = [ [inputInfix, [inputString] ]]

        for test in tests:
            infix = test[0]
            print(f"infix:    {infix}")
            postfix = shuntingre.shunt(infix)
            print(f"postfix:  {postfix}")
            nfa = thompson.re_to_nfa(postfix)
            print(f"thompson: {nfa}")
            for s in test[1]:
                match = nfa.match(s)
                print(f"Match '{s}': {match}")
            print()
# errors if '+' used as its not built into thompson search

# user input matching
def sampleText():

    inputInfix = input("Enter an infix :")
    f = open('Sample.txt','r')

    if __name__ == "__main__":
        tests = [ [inputInfix, [f] ]]

        for test in tests:
            infix = test[0]
            print(f"infix:    {infix}")
            postfix = shuntingre.shunt(infix)
            print(f"postfix:  {postfix}")
            nfa = thompson.re_to_nfa(postfix)
            print(f"thompson: {nfa}")
            for s in test[1]:
                match = nfa.match(s)
                print(f"Match '{s}': {match}")
            print()
            # doesent process through lines correctly

# test samples
def test():
    
    testVersion = [ [ 'a.b',  ["", "a", "b", "ab", "aa", "bb", "aab", "abb"] ], # concat test '.'
                    [ 'a|b',  ["", "a", "b", "ab", "aa", "bb", "aab", "abb"] ], # or test '|'
                    [ 'a*',  ["", "a", "b", "ab", "aa", "bb", "aab", "abb"] ], # kleene test '*'
                    [ 'a.b|b*',  ["", "a", "b", "ab", "aa", "bb", "aab", "abb"] ], # mixed 1 test
                    [ 'a*|b*',  ["", "a", "b", "ab", "aa", "bb", "aab", "abb"] ], # mixed 2 test
                    [ 'a.(b.b)*.a',  ["", "a", "b", "ab", "aa", "bb", "aab", "abb"] ], # mixed 3 test
     ]

    if __name__ == "__main__":
        tests = testVersion

        for test in tests:
            infix = test[0]
            print(f"infix:    {infix}")
            postfix = shuntingre.shunt(infix)
            print(f"postfix:  {postfix}")
            nfa = thompson.re_to_nfa(postfix)
            print(f"thompson: {nfa}")
            for s in test[1]:
                match = nfa.match(s)
                print(f"Match '{s}': {match}")
            print()

# menu validation
while loop:  # While loop which will keep going until loop = False
    menu()
    option = input("Enter your choice [1-4]: ")
    
    if option=='1':     
        userInput() # call user input function
    elif option=='2': 
        test() # calls test samples
    elif option=='3': 
        sampleText() # reads in sample.txt    
    elif option=='4':
        print("Exiting...")
        loop=False # This will make the while loop end
    else:
        # Any input other than values 1-3 will print an error message
        print("Wrong option selected. Enter any key to try again..")