#Tess Porter
#March 15, 2018
#CS 171 Lab Section 070
#Professor Mark Boady

#Homework 5 - 18.1 Auto-Testing Functions (10 points)

import math
def hypotenuse(a,b):
    c = math.sqrt((a*a) + (b*b))
    return c

#You do not need to make changes below this line.
if __name__=="__main__":
	print("Hypotenus Example")
	a=int(input("Enter Side One:\n"))
	b=int(input("Enter Side Two:\n"))
	
	print("Hypotenuse is %0.4f"%(hypotenuse(a,b)))