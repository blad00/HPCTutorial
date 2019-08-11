#Sum of two integers
#ask nums
import math

num1 = input('input num 1: ')
num2 = input('input num 2: ')

#make sum

mySum = int(num1) + int(num2)

print(mySum)


#	Mercator projection

lan0 = float(input('Landa0: '))
lan = float(input('Landa: '))
p = float(input('P: '))

x = ((lan-lan0 + 180)%360) - 180

print("x: "+ str(x))

import math

up = 1 + math.sin(math.radians(p))
down = 1 - math.sin(math.radians(p))

y = 15 * math.log(up/down)

print("y: "+ str(y))

#Light work

# read number of stacks (and number of coins per stack)
num_stacks = int(input("Num Stacks?"))
# read weight of genuine coin
coinW = int(input("Weight of am actual coin?"))
# read measured weight of selected coins
stackW_current = int(input("Current weight of sampled coins?"))
# compute weight if all selected coins would be genuine
stackW_calc = coinW * (num_stacks * (num_stacks + 1)) / 2
# determine stack containing counterfeit coins
print(abs(int(stackW_calc - stackW_current)))

# Vis Viva

#import math functions from math module
from math import pi, sqrt
# read distance between satellite and center of the Earth
r = float(input())
# read speed of satellite relative to Earth
v = float(input())
# define geocentric gravitational constant
mu = 398600.4418e9
# compute major axis of the elliptical orbit (in meters)
major_axis = (mu * r) / (2 * mu - r * v ** 2)
print(f'major axis: {major_axis} meters')
# determine length of a single rotation (in seconds)
period = 2 * pi * sqrt((major_axis ** 3) / mu)
print(f'period: {period} seconds')
# determine length of a single rotation (in days, hours and minutes)
# truncate period (expressed in seconds) to an integer, because the period
# expressed in days, minutes and seconds should entirely fit with the period
# expressed in seconds
period = int(period)
# convert period expressed in seconds into period expressed in minutes
# note: we don’t need the remaining number of seconds
minutes = period // 60
# determine number of days that completely fit within the period (expressed in
# minutes) and subtract the corresponding number of minutes from the total
# number of minutes
days = minutes // (24 * 60)
minutes %= 24 * 60
# determine number of hours that completely fit within the remaining period
# (expressed in minutes) and subtract the corresponding number of minutes from
# the remaining number of minutes
hours = minutes // 60
minutes %= 60
print(f'period: {days} days, {hours} hours and {minutes} minutes')

#Alarm clock

# read time currently displayed on the alarm clock
hours_now = int(input())
minutes_now = int(input())
# read time that needs to be displayed on the alarm clock
hours_target = int(input())
minutes_target = int(input())
# determine minimal number of key strokes needed to reset the hours
hours = abs(hours_target - hours_now)
hours = min(hours, 24 - hours)
# determine minimal number of key strokes needed to reset the minutes
minutes = abs(minutes_target - minutes_now)
minutes = min(minutes, 60 - minutes)
# print minimal number of key strokes needed to reset the alarm clock
print(hours + minutes)