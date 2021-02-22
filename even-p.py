class State:
    # is this an accept state?
    accept = False
    # the arrows out of the state
    arrows = {}
    """A state in an automaton"""
    def __init__(self, accept, arrows):
        # true if this is an accept state
        self.accept = accept
        # Arrows (Keys are labels) out of state
        self.arrows = arrows

class DFA:
    """An automaton"""
    def __init__(self, start):
        # start state of the automaton
        self.start = start

    def match(self, s):
        """See if s is accpeted by automaton"""
        # current state
        current = self.start
        # loop through characters in s
        for c in s:
            # find the state in arrows with c
            current = current.arrows[c]
        # return whether we're in accept state
        return current.accept

def compile():
    """Create the automaton"""

    # create start state
    start = State(True, {})
    # create other state
    other = State(False, {})

    # state point to themselves on a 0
    start.arrows['0'] = start
    other.arrows['0'] = other

    # states point to themselves on a 0
    start.arrows['1'] = other
    other.arrows['1'] = start

    # creata a automaton
    parity = DFA(start)

    # return automaton
    return parity


# create automaton instance
myautomaton = compile()
# a few small tests
for s in ['1100', '11111', '', '1', '0']:
    # check if s is accpeted by automaton
    result = myautomaton.match(s)
    # print result
    print(f"{s} -> {result}")

for s in ['000', '001', '010', '011', '100', '101', '110', '111']:
    # check if s is accpeted by automaton
    result = myautomaton.match(s)
    # print result
    print(f"{s} -> {result}")