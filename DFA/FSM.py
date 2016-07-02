class TransitionTable:
    def __init__(self):
        self.data = {}
        
    def addentry(self, state, input, newstate):
        self.data[(state, input)] = newstate
        
    def gettransition(self, state, input):
        return self.data[(state, input)]
    
    def gethash(self):
        return self.data
# 5-tuple(Q, E, &, q0, F) where
# Q = all states
# E = alphabet
# & = transistion function/table
# q0 = start state
# F = set of accept states
class StateMachine:
    def __init__(self, table, inital, accepts):
        self.table = table
        self.currentQ = inital
        self.acceptStates = accepts
        
    def feedstring(self, wholestring):
        for i in wholestring:
            self.feed(i)
            
    def feed(self, symbol):
        self.currentQ = self.table.gettransition(self.currentQ, symbol)
        
    def doesrecognize(self, wholestring):
        self.feedstring(wholestring)
        return self.isacceptstate()
    
    def isacceptstate(self):
        return self.acceptStates.__contains__(self.currentQ)