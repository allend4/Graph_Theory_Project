import shuntingre
import thompson

def menu(): # menu input
    print("===============GraphTheory===============")
    print("|\t(David Allen - G00375372)\t|")
    print("=========================================")
    print("1. Menu Option 1")
    print("2. Menu Option 2")
    print("5. Exit")

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

#-----------------------------------------------

while loop:  # While loop which will keep going until loop = False
    menu()
    option = input("Enter your choice [1-5]: ")
    
    if option=='1':     
        userInput()
    elif option=='2': 
        print("option 2")
        ## You can add your code or functions here
    elif option=='5':
        print("Exiting...")
        ## You can add your code or functions here
        loop=False # This will make the while loop en
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong option selected. Enter any key to try again..")
        


