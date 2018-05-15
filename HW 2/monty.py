import sys
import random
#list of doors, with the car in the first position
L = ['C', 'G', 'G']
#statement asking the player to pick a number that will control the sequence of random numbers generated
user_seed = input('Enter Random Seed:\n')
while True:
    try:
        user_seed = int(user_seed)
        break
    except ValueError as e:
        print('Seed is not a number!')
        sys.exit()
random.seed(user_seed)
#function to decide if player should switch or not
def stay_or_switch(num):
    if L[num - 1] == 'C':
        #user will enter a number between 1 and 3, but a list of three objects goes from 0 to 2
        return True
    else:
        return False
#function to determine the value of Monty's pick
def monty_pick():
    x = random.randint(1,3)
    while x == user_pick or L[x-1] == 'C':
        x = random.randint(1,3)
    return x
print('Welcome to Monty Hall Analysis')
print('Enter \'exit\' to quit.')
boolean = True
rounds = input('How many tests should we run?\n')
while boolean == True:
    if rounds == 'exit' or rounds == 'Exit':
        print('Thank you for using this program.')
        break
    else:
        try:
            rounds == int(rounds)
            i = 1
            stay = 0
            switch = 0
            if int(rounds) <= 10:
                while i <= int(rounds):
                    print('Game', i)
                    random.shuffle(L)
                    print('Doors:', L)
                    user_pick = random.randint(1,3)
                    print('Player Selects Door', user_pick)
                    print('Monty Selects Door', monty_pick())
                    res = stay_or_switch(user_pick)
                    if res == True:
                        print('Player should stay to win.')
                        stay += 1
                    else:
                        print('Player should switch to win.')
                        switch += 1
                    i += 1
            else:
                while i <= int(rounds):
                    user_pick = random.randint(1,3)
                    monty_pick()
                    res = stay_or_switch(user_pick)
                    if res == True:
                        stay += 1
                    else:
                        switch += 1
                    i += 1
            #summary print out
            print('Stay Won', round(stay/int(rounds)*100,1),'% of the time.')
            print('Switch Won', round(switch/int(rounds)*100,1),'% of the time.')
            #resarting the while loop
            rounds = input('How many tests should we run?\n')
        except ValueError as e:
            #restarting the while loop
            rounds = input('Please enter a number:\n')
            boolean == False