import math
#Tess Porter
#March 15, 2018
#CS 171 Lab Section 070
#Professor Mark Boady

#Homework 5 - 18.2 Foxes vs. Rabbits (20 points)

def bunnies(rabbits, foxes, years):
    end_pop = []
    #list for rabbits
    r = []
    #list for foxes
    f = []
    #intitial number of rabbits appended to position 0
    r.append(int(rabbits))
    #initial number of foxes appended to position 0
    f.append(int(foxes))
    #start list looping at 1
    i = 1
    while i <= int(years):
        r.append(r[i-1] + math.floor(r[i-1] * (0.04 - 0.0005 * f[i-1])))
        f.append(f[i-1] - math.floor(f[i-1] * (0.2 - 0.00005 * r[i-1])))
        i+= 1
    #append each population at position years (after number of years) to the end populations list
    end_pop.append(r[int(years)])
    end_pop.append(f[int(years)])
    return end_pop

if __name__=="__main__":
    print('Welcome to Predator-Prey Model.')
    rabbit_pop = input('Enter Initial Rabbit Population:\n')
    fox_pop = input('Enter Initial Fox Population:\n')
    y = input('Enter Number of Years to Simulate:\n')
    
    results = bunnies(rabbit_pop, fox_pop, y)
    
    print('After', y, 'years there will be', results[0], 'rabbits.')
    print('After', y, 'years there will be', results[1], 'foxes.')