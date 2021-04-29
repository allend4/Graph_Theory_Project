import shuntingre
import thompson

def menu(): # menu input
    print("===============GraphTheory===============")
    print("|\t(David Allen - G00375372)\t|")
    print("=========================================")
    print("1. User inputs ")
    print("2. Run test samples")
    print("3. Exit")

loop=True # loop = true until loop = false

#---------------------------------

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
#-----------------------------------------------

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

#-----------------------------------------------

while loop:  # While loop which will keep going until loop = False
    menu()
    option = input("Enter your choice [1-3]: ")
    
    if option=='1':     
        userInput() # call user input function
    elif option=='2': 
        test() # calls test samples
    elif option=='3':
        print("Exiting...")
        loop=False # This will make the while loop end
    else:
        # Any input other than values 1-3 will print an error message
        print("Wrong option selected. Enter any key to try again..")
        


