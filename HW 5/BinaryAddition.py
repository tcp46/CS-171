import sys
def getStr(question):
    binary = ''
    while True:
        binary = input(question)
        if binary.lower() == 'exit':
            sys.exit()
        return binary

def binarySun(X,Y):
    carry = 0
    binary = ''
    x = len(X)
    while x > 0:
        sum = (carry + int(X[x-1]) + int(Y[x-1]))
        binary = str(sum%2) + binary
        carry = sum // 2
        x -=1
    return binary

print('Welcome to Binary Adder\nEnter exit to quit at any time.')
while True:
    first = getStr('Enter first Binary Value:\n')
    second = getStr('Enter Second Binary Value:\n')
    if len(first) != len(second):
        print('Sum: Cannot Add!')
    else:
        print('Sum:', binarySun(first, second))