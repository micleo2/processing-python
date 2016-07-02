import FSM
def setup():
    size(600, 600)
framecount = 0
table = FSM.TransitionTable()
# table.addentry ("q1", "1", "q2")
# table.addentry ("q1", "0", "q1")

# table.addentry ("q2", "0", "q2")
# table.addentry ("q2", "1", "q1")

table.addentry ( "q1", "1", "q2")
table.addentry ( "q1", "0", "q1")

table.addentry ( "q2", "1", "q3")
table.addentry ( "q2", "0", "q2")

table.addentry ( "q3", "1", "q4")
table.addentry ( "q3", "0", "q3")

table.addentry ( "q4", "1", "q4")
table.addentry ( "q4", "0", "q4")

machine = FSM.StateMachine(table, "q1", ["q4"])

teststring = "100101"
currentindex = 0
strlen = len(teststring)
trace = [machine.currentQ]

def stringify(stack):
    buildstr = ""
    for i in stack[:-1]:
        buildstr += i + " --> "
    buildstr += stack[-1]
    return buildstr
machine.feed(teststring[currentindex])
def draw():
    global framecount, currentindex
    framecount += 1
    background(255)
    fill(0)
    text("Input symbol... " + teststring[currentindex], 15, 15)
    text("Total input so far... " + teststring[:(currentindex+1)], 15, 35)
    text("State machine \'stack trace\'... " + stringify(trace), 15, 55)
    
    if machine.isacceptstate():
        fill(0, 255, 0)
        text("STRING RECOGNIZED AS MEMBER OF LANGUAGE", 200, 200)
    else:
        fill(255, 0, 0)
        text("STRING NOT RECOGNIZED AS MEMBER OF LANGUAGE", 200, 200)
    
    if framecount % 100 == 0 and currentindex != strlen-1:
        currentindex += 1
        machine.feed(teststring[currentindex])
        trace.append(machine.currentQ)
    