#Tess Porter
#March 15, 2018
#CS 171 Lab Section 070
#Professor Mark Boady

#Homework 5 - 18.3 Two's Complement (20 points)

import math

def binary_to_int(b):
    a = len(b)
    i = 0
    reg_num = 0
    while a >= 0:
        reg_num += int(b[a-1])*(2**i)
        a -= 1
        i += 1
    return reg_num
    #returns an integer

def int_to_binary(num):
    i = 0
    empty = ''
    while i < 8:
        y = int(num) % 2
        empty += str(y)
        z = int(num) // 2
        num = z
        i += 1
    string = empty[::-1]
    return string
    #returns a binary number in string format

def twoscomp(num):
    new_num = ''
    for i in range(len(num)):
        if num[i] == '1':
            new_num += '0'
        else:
            new_num += '1'
    #takes the value just generated and turns it into a integer
    integer_val = binary_to_int(new_num)
    #adds 1 to integer value
    integer_val += 1
    #turns the new int back into a binary number
    new_binary = int_to_binary(integer_val)
    #returns new binary
    return new_binary  

if __name__=="__main__":
    print('Welcome to Two\'s Complement Creator')
    #user enters a string binary value
    binary = input('Enter a Binary Value:\n')
    print('In Two\'s Complement:') 
    print(twoscomp(binary))