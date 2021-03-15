# Adapted from the pseudo code - https://en.wikipedia.org/wiki/Shunting-yard_algorithm
# Alignment is a big thing - if alignment is out, it causes errors in the code.

def shunt(infix):
    """ Convert infix expressions to postfix """
    # The eventual output
    postfix = ""
    # The shunting yard operator stack
    stack = ""
    # Operator precedence
    #prec = {'*': 100, '/': 90, '+': 80, '-': 70}
    prec = {'*': 100, '.': 90, '|': 80}
    # Loop through the input one character at a time
    for c in infix:
        # c is an operator.
        if c in {'*', '.', '|'}:
            # Check what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # Append - operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove - operator from stack.
                stack = stack[:-1]
            # Push - c to stack.
            stack = stack + c
        elif c == '(':
            # Push - c to stack.
            stack = stack + c
        elif c == ')':
            while stack[-1] != "(":
                # Append  - operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove - operator from stack.
                stack = stack[:-1]
            # Remove - open bracket from stack.
            stack = stack[:-1]
                # c  - is a non-special.
        else:
            # Push it -  to the output.
            postfix = postfix + c
    # Empty - the operator stack.
    while len(stack) != 0:
        # Append - operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove - operator from stack.
        stack = stack[:-1]
    # Return the postfix version of infix.
    return postfix


if __name__ == "__main__":
    #for infix in ["3+4*(2-1)", "1+2+3+4+5*6", "(1+2)*(4*(6-7))"]:
    for infix in ["a.(b.b)*.a", "1.(0.0)*.1"]:    
        print(f" infix:   {infix}")
        print(f" postfix: {shunt(infix)}")
        print()