#Tess Porter
#CS 171 Lab Section 070
#Professor Mark Boady


import sys #to exit at the end

altitude = 50
velocity = 0.00
sec_passed = 0
thruster = 0.10
level = 0 #will be used to increment through the lists
planet = ['Moon', 'Earth', 'Pluto', 'Neptune', 'Uranus', 'Saturn', 'Jupiter', 'Mars', 'Venus', 'Mercury', 'Sun']
planet_grav = [-1.622, -9.81, -0.42, -14.07, -10.67, -11.08, -25.95, -3.77, -8.87, -3.59, -247.13]
planet_fuel = [150, 5000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 50000]
           


#function one
def ask_fuel(current_fuel):
    while True:
        try:
            user_fuel = input('Enter units of fuel to use:\n')
            user_fuel = int(user_fuel)
            if 0 <= user_fuel <= current_fuel:
                user_fuel = user_fuel
                False
                #makes sure the while loop is exited
                return user_fuel
                #this is the only condition on which the user_fuel should be returned
            elif user_fuel < 0:
                print('Cannot use negative fuel.')
                True
            else:
                print('Not enough fuel. Max Fuel:', current_fuel)
                True
        except ValueError as e:
            print('Please Enter Integer Value.')
            True


#function two
def play_level(name, G, amount_fuel):
    print('GO')
    alt = 50
    vel = 0.00
    sec = 0
    thruster = 0.10
    while alt > 0:
        current_fuel = ask_fuel(amount_fuel)
        #calculations
        amount_fuel = amount_fuel - current_fuel
        vel = vel + G + thruster * current_fuel
        alt = alt + vel
        sec += 1
        if alt <= 0:
            print('After', sec, 'seconds Altitude is 0.00 meters, velocity is', round(vel, 2), 'm/s.')
        else:
            print('After', sec, 'seconds Altitude is', round(alt,2), 'meters, velocity is', round(vel, 2), 'm/s.')
        print('Remaining Fuel:', amount_fuel, 'units.')
    if -2 <= vel <= 2:
        print('Landed Successfully.')
        alive = True
    else:
        print('Crashed!')
        alive = False
    return alive


#main body of function
print('Welcome to Lunar Lander Game.')
run_again = True
while True:
    print('Do you want to play level', level + 1, '? (yes/no)')
    yes_no = input()
    if yes_no.lower() == 'yes':
        print('Entering Level', level + 1)
        print('Landing on the', planet[level])
        print('Gravity is', round(planet_grav[level], 2), 'm/s^2')
        print('Initial Altitude:', altitude,'meters')
        print('Initial Velocity: %.2f m/s' %float(velocity))
        print('Burning a unit of fuel causes %.2f m/s slowdown.' %float(thruster))
        print('Initial Fuel Level:', planet_fuel[level], 'units\n')
        run_again = play_level(planet[level], planet_grav[level], planet_fuel[level])
        #takes the boolean returned from run again to determine whether the lander is functional enough to move to the next level
        if run_again == True:
            level += 1
        else:
            level = level
    else:
        print('You made it past', level, 'levels.\nThank you Playing.')
        sys.exit()