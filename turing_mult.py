#This is my implementatoin of the multiplication 
# turing machine graph that I previosly created

#After running, the input must have a space inbetween
#each 1 and has to have a '*' in between each number
#for example: 
#   1 1 1 * 1 1 1 is valid 
#   111*111 is not valid

import timeit
import sys 

sys.setrecursionlimit(10**6) 

emp = "v" 
pointer =  0
global pcount 
pcount = 0


def q0(tape, pointer):
    print()
    global pcount
    print("THIS IS Q0")
    while tape[pointer] == "v":
        pointer += 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
    if tape[pointer] == "1":
        tape[pointer] = "0"
        pointer +=1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
        q1(tape,pointer)

    if tape[pointer] == "*":
        pointer -= 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
        q11(tape, pointer)

def q1(tape, pointer):
    print()
    global pcount
    print("THIS IS Q1")
    while tape[pointer] == "1":
        pointer += 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
    if tape[pointer] == "*":
        pointer += 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
        q2(tape, pointer)

def q2 (tape,pointer):
    print()
    global pcount
    print("THIS IS Q2")
    if tape[pointer] == "1":
        tape[pointer] = "0"
        pointer +=1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
        q4(tape, pointer)
    if tape[pointer] == "v":
        pointer -=1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
        q8(tape, pointer)

def q4 (tape,pointer):
    print()
    global pcount
    print("THIS IS Q4")
    while tape[pointer] == "1":
        pointer += 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
    if tape[pointer] == "v":
        pointer += 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
        q5(tape,pointer)

def q5 (tape, pointer):
    print()
    global pcount
    print("THIS IS Q5")
    while tape[pointer] == "1":
        pointer += 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
    if tape[pointer] == "v":
        tape[pointer] = "1"
        tape.append("v")
        pointer -= 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
        q6(tape, pointer)
    
def q6 (tape, pointer):
    print()
    global pcount
    print("THIS IS Q6")
    while tape[pointer] == "1":
        pointer -= 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
    if tape[pointer] == "v":
        pointer -= 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
        q7(tape, pointer)

def q7 (tape, pointer):
    print()
    global pcount
    print("THIS IS Q7")
    while tape[pointer] == "1":
        pointer -= 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
    if tape[pointer] == "0":
        tape[pointer] = "1"
        pointer += 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
        q2(tape, pointer)
    
def q8 (tape, pointer):
    print()
    global pcount
    print("THIS IS Q8")
    while tape[pointer] == "1":
        pointer -= 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
    if tape[pointer] == "*":
        pointer -= 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
        q9(tape, pointer)

def q9 (tape, pointer):
    print()
    global pcount
    print("THIS IS Q9")
    while tape[pointer] == "1":
        pointer -= 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
    if tape[pointer] == "0":
        tape[pointer] = "1"
        pointer += 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
        q0(tape, pointer)

def q11 (tape, pointer):
    print()
    global pcount
    print("THIS IS Q11")
    while tape[pointer] == "1":
        pointer -= 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
    if tape[pointer] == "v":
        pointer += 1
        print("the pointer is at: " , (pointer))
        print (tape)
        pcount +=1
        q12(tape, pointer)

def q12 (tape, pointer):
    print()
    global pcount
    print("THIS IS Q12")
    print("the pointer is at: " , (pointer))
    print (tape)
    pcount +=1
    print("end")

def getinput():
    input_string = input("input the tape with a space inbetween each element: \n")
    tape = input_string.split()
    tape = [emp] + tape + [emp] + [emp]
    print("the pointer is at: " , (pointer))
    print(tape)
    return tape

tape = getinput()
start = timeit.default_timer()
q0(tape,pointer)
stop = timeit.default_timer()
print('Time: ', stop - start)  
print("Number of tapes used: " , pcount)