#Tess Porter
#March 15, 2018
#CS 171 Lab Section 070
#Professor Mark Boady

#Homework 5 - 18.5 Roman Numerals (30 points)

import sys

#dictionay of characters that correlate with each value
roman_dict = {'one' : 'I', 'five' : 'V', 'ten' : 'X', 'fifty' : 'L', 'hundred' : 'C', 'fivehundred' : 'D', 'thousand' : 'M', 'fivethousand' : 'v', 'tenthousand' : 'x'}

def roman(n, one, five, ten):
    #given a number, what characters do you return
    if n > 9:
        return ''
    else:
        if n <= 3:
            return n * one
        else:
            if n == 4:
                return one + five
            else:
                if n <= 8:
                    return five + one * (n - 5)
                else:
                    if n == 9:
                        return one + ten

def roman_num(n):
    final_roman = ''
    #if num > 1000
    x = int(n) // 1000
    y = int(n) % 1000
    final_roman += roman(x, roman_dict['thousand'], roman_dict['fivethousand'], roman_dict['tenthousand'])
    #if num > 100
    x = y // 100
    y = y % 100
    final_roman += roman(x, roman_dict['hundred'], roman_dict['fivehundred'], roman_dict['thousand'])
    #if num > 10
    x = y // 10
    y = y % 10
    final_roman += roman(x, roman_dict['ten'], roman_dict['fifty'], roman_dict['hundred'])
    final_roman += roman(y, roman_dict['one'], roman_dict['five'], roman_dict['ten'])
    return final_roman

if __name__ == "__main__":
    print('Roman Number Generator. Enter 0 to quit.')
    num = input('Enter a number between 1 and 9,999:\n')
    while True:
        if num == '0':
            print('Roman Numerals: ')
            print('Bye.')
            sys.exit()
        else:
            num = int(num)
            print('Roman Numerals:', roman_num(num))
            num = input('Enter a number between 1 and 9,999:\n')