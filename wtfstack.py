import sys
import math
with open(sys.argv[1],'r') as f:
    code=f.read()
user_input = input("initial stack: ")
if user_input=='':
    stack=[]
    def push_input():
        pass
else:
    stack=[int(user_input)]
    def push_input():
        stack.append(int((user_input)))

def addition():
    global stack
    g=stack.pop()
    newstack=[q+g for q in stack]
    stack=newstack

def subtraction():
    global stack
    g=stack.pop()
    newstack=[q-g for q in stack]
    stack=newstack

def multiplication():
    global stack
    g=stack.pop()
    newstack=[q*g for q in stack]
    stack=newstack


def division():
    global stack
    g=stack.pop()
    newstack=[q/g for q in stack]
    stack=newstack

def exponentiation():
    global stack
    g=stack.pop()
    newstack=[q**g for q in stack]
    stack=newstack

def division_r():
    global stack
    g=stack.pop()
    newstack=[g/q for q in stack]
    stack=newstack

def exponentiation_r():
    global stack
    g=stack.pop()
    newstack=[g**q for q in stack]
    stack=newstack

def subtraction_r():
    global stack
    g=stack.pop()
    newstack=[g-q for q in stack]
    stack=newstack

def sqrt():
    global stack
    newstack=[math.sqrt(q) for q in stack]
    stack=newstack

def square():
    global stack
    newstack=[q**2 for q in stack]
    stack=newstack

def factorial():
    global stack
    newstack=[math.factorial(q) for q in stack]
    stack=newstack

def inc():
    global stack
    newstack=[q+1 for q in stack]
    stack=newstack

def dec():
    global stack
    newstack=[q-1 for q in stack]
    stack=newstack

def is_integer(num):
    if isinstance(num,int):
        return True
    if isinstance(num,float):
        return num.is_integer()
    return False

def integer_test():
    stack.append(int(is_integer(stack.pop())))

def is_true_else_exit():
    v=stack.pop()
    if v == 1:
        stack.append(v)
    else:
        print(stack)
        exit()

def greater_than():
    v1=stack.pop()
    v2=stack.pop()
    stack.append(int(v2>v1))
def swp():
    top=stack.pop()
    bottom=stack.pop()
    stack.append(top)
    stack.append(bottom)
def discard():
    stack.pop()
def fldivision():
    global stack
    g=stack.pop()
    newstack=[q//g for q in stack]
    stack=newstack
def range_from_one():
    for z in range(stack.pop()):
        stack.append(z+1)

def sum_stack():
    global stack
    z=sum(stack)
    stack=[]
    stack.append(z)
def equality():
    right=stack.pop()
    left=stack.pop()
    stack.append(int(right==left))
instruction_set = {
    '+' : addition,

    '-' : subtraction,

    '*' : multiplication,

    '/' : division,
    
    'n' : exponentiation,

    '_' : subtraction_r,

    '$' : division_r,

    '#' : exponentiation_r,

    's' : sqrt,

    '^' : square,
    '!' : factorial,
    ')' : inc,
    '(' : dec,
    'x' : integer_test,
    '?' : push_input,
    '{' : is_true_else_exit,
    '=' : equality,
    'g' : greater_than,
    '<' : swp,
    ';' : discard,
    ':' : fldivision,
    'r' : range_from_one,
    'E' : sum_stack,
}

for i in code:
    if i in instruction_set:
        instruction_set[i]()
    elif i in list("1234567890"):
        z=int(i)
        stack.append(z)
    else:
        stack.append(ord(i))
    
print(stack)