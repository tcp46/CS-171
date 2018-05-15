#Tess Porter
#CS 171 Lab Section 070
#Professor Mark Boady


import sys #to exit at the end
          
#main body of program
print('Welcome to a fun word replacement game.')
file_name = input('Enter the name of the file to use:\n')
if file_name == 'example1.txt' or file_name == 'example2.txt' or file_name == 'mad_lib.txt' or file_name == 'tcp46.txt':
    file_name = file_name
else:
    print('Error Bad File Name')
    sys.exit()

f = open(file_name, 'r') #each element of f will hold a line from the file
vowels = ['a', 'e', 'i', 'o', 'u']

story = ''

for line in f: #read the line
    for word in line.split(): #read each word in the line
        if word[0] == '[':
            #this set of if/else brackets checks to see if the word being filled in is the last in the sentence
            if word[len(word) - 1] == ']':
                w = word[1:len(word) - 1]
                w = w.replace('-',' ')
                if w[0].lower() in vowels:
                    print('Please give an', w,)
                    new_word = input()
                    story += new_word
                    story += ' '
                else:
                    print('Please give a', w,)
                    new_word = input()
                    story += new_word
                    story += ' '
            else:
            #condition for words at the end of a sentence [something].
            #if the last of a sentence need to be aware of punctuation
                w = word[1:len(word) - 2]
                w = w.replace('-',' ')
                if w[0].lower() in vowels:
                    print('Please give an', w,)
                    new_word = input()
                    story += new_word
                    story += ' '
                else:
                    print('Please give a', w,)
                    new_word = input()
                    story += new_word
                    story += (word[len(word)-1] + ' ')
        else:
            #if not a word just add it to the story string with a space following
            story += word
            story += ' '

print('Here is your story:')
print('--------------------')
print(story)