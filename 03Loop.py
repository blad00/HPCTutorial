#ISBN
first_digit = input()
while first_digit != 'stop':
    # read next eight digits and compute check digit
    computed_check_digit = int(first_digit)
    for index in range(2, 10):
        next_digit = int(input())
        computed_check_digit += index * next_digit
    computed_check_digit %= 11
    # read given check digit
    given_check_digit = int(input())
    # output correctness of given check digit
    print('OK' if given_check_digit == computed_check_digit else 'WRONG')
    # read first digit of next ISBN-10 code
    # NOTE: at this point we cannot assume the first line of the next ISBN-10
    # code contains a digit, since it may also contain the word stop
    first_digit = input()

#Generators

g = int(input("Enter g: "))
p = int(input("Enter p: "))

counter = 2

result = 0

while result != g:
    result = (g**counter) % p
    print(f'({g}^{counter}) mod {p} = {result}')
    counter += 1

counter -= 1
if counter == p:
    print(f'{g} is a generator of {p}')
else:
    print(f'{g} is not a generator of {p}')


# Frogs

import math

nFrog = int(input("Number of frog: "))
#print("Please enter all ratings for such frogs: ")

ratsFrogs = []

stopKiss = math.ceil(nFrog/math.e)

biggestRating = 0

for i in range(nFrog):
    ratsFrogs.append(float(input()))
    if i < stopKiss:
        if biggestRating < ratsFrogs[i]:
            biggestRating = ratsFrogs[i]

for i in range(stopKiss,nFrog):
    if ratsFrogs[i]>biggestRating:
        result = ratsFrogs[i]
        break
    result = ratsFrogs[i]

print(result)

#Early warning
# read number of buildings
buildings = int(input())
# read name of first building
building = input()
# read height of first building (in meters) and set as current maximal height
maximal_height = int(input())
# first building is always entirely visible
print(f'{building} is visible from the ground floor up to {maximal_height} meters.')
# process other buildings
for _ in range(buildings - 1):
    # read name of next building
    building = input()
    # read height of next building (in meters)
    height = int(input())
    # building is visible if higher than current maximal height
    if height > maximal_height:
        print(f'{building} is visible from {maximal_height} meters up to {height} meters.')
        maximal_height = height

#Elevator paradox
# read information about the simulation
steps = int(input()) # number of steps in simulation
floor_start = int(input()) # index of floor where simulation starts
floor_top = int(input()) # index of top floor
direction = -1 if input() == 'v' else 1 # initial direction of elevator
hour = int(input()) # time at start of simulation (hours)
minute = int(input()) # time at start of simulation (minutes)
verbose = input() == 'verbose' # verbose output of information?
# simulation starts at given floor
floor = floor_start
# simulate successive steps of elevator
for _ in range(steps):
# modify direction if elevator arrives at lobby or top floor
    if floor == 0:
        direction = 1
    elif floor == floor_top:
        direction = -1
    # output information at current floor
    if verbose or floor == floor_start:
        direction_pointer = 'v' if direction == -1 else '^'
        print(f'{hour:02d}:{minute:02d} {floor} [{direction_pointer}]')
    # go to next floor
    floor += direction
    # step one minute forward in time
    minute += 1
    if minute == 60:
        hour = (hour + 1) % 24
        minute = 0

#Billiards table
# read dimensions of billiards table
height = int(input())
width = int(input())
# define position of ball after first step
x, y, dx, dy = 1, 1, 1, 1
# simulate movement of ball until it hits a corner pocket
while x % width or y % height:
    # check if ball hits a cushion
    if x % width == 0:
        dx *= -1
        cushion = 'right' if x else 'left'
    elif y % height == 0:
        dy *= -1
        cushion = 'top' if y else 'bottom'
    if x % width == 0 or y % height == 0:
        print(f'{cushion} cushion ({x}, {y})')
    # ball moves to next position
    x += dx
    y += dy
# determine corner in which ball has disappeared
if x == 0 and y == 0:
    pocket = 'bottom left'
elif x == 0:
    pocket = 'top left'
elif y == 0:
    pocket = 'bottom right'
else:
    pocket = 'top right'
print(f'{pocket} pocket ({x}, {y})')

