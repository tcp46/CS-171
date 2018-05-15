#Tess Porter
#March 15, 2018
#CS 171 Lab Section 070
#Professor Mark Boady

#Homework 5 - 18.4 String Games (20 Points)

def rev(text):
    #slice the string into a list to loop through
    L = list(text)
    char_vals=""
    num_vals=""
    final_text=""
    i = 0
    while i<len(L):
        #loop until the position is no longer a character
        valid=True
        while valid == True and i < len(L):
            if not ((L[i] >= '0' and L[i] <='9') or (L[i] >= 'A' and L[i] <= 'Z')):
                char_vals += L[i]
            else:
                valid = False
                break
            i += 1
        final_text = final_text + char_vals
        #clear char_vals for next iteration of loop
        char_vals =""
        #add the values at i which are integers
        while valid == False and i<len(L):
            if (L[i] >= '0' and L[i] <='9') or (L[i] >= 'A' and L[i] <= 'Z'):
                num_vals += L[i]
            else:
                valid = True
                break
            i=i+1
        #add the list of numbers in reverse to the final_text
        final_text = final_text + num_vals[::-1]
        #clear num_vals for next iteration of loop
        num_vals =""
    return final_text
 
 
print("Welcome to Digit Flipper")
 
if __name__ == "__main__":
    line = input("Enter Some Text:\n")
    calling_function=rev(line)
    print("Revised String:\n%s"%calling_function)
