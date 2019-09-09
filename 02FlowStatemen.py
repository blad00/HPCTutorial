ph = 51

if ph > 7:
    print('basic')
    print("other basic")
elif ph <7:
    print('acid')
else:
    print('Neutral')
print('done')


mass = int(input("Enter you weight (Kg): "))
height = int(input("ENter height: "))

BMI = mass / (height / 100) ** 2

print(BMI)

#2.1 ISBN
# read ten digits of an ISBN-10 code (each on a separate line)
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())
x7 = int(input())
x8 = int(input())
x9 = int(input())
x10 = int(input())
# compute check digit
check_digit = (
x1 + 2 * x2 + 3 * x3 + 4 * x4 + 5 * x5 + 6 * x6 + 7 * x7 + 8 * x8 + 9 * x9
) % 11
# check correctness of check digit
print("OK" if x10 == check_digit else "WRONG")

if x10 == check_digit:
    print("OK")
else:
    print("WRONG")

#2.2 Runway
# read magnetic azimuth of the runway’s heading
angle = float(input())
# compute first runway number
direction1 = int(round(angle / 10))
if direction1 == 0:
    direction1 = 36
# compute second runway number
direction2 = (18 + direction1) % 36
if direction2 == 0:
    direction2 = 36
# first runway number is always smaller than second runway number
if direction2 < direction1:
    direction1, direction2 = direction2, direction1
# output runway number in format dd/dd
print(f'{direction1:02d}/{direction2:02d}')

#2.3 Digit work
# read two factors
factor1 = int(input())
factor2 = int(input())
# determine smallest and largest factor
smallest, largest = min(factor1, factor2), max(factor1, factor2)
# use fingers to compute product of two factors
if (0 <= smallest <= largest <= 5) or factor1 == 10 or factor2 == 10:
    # method 0: product of two integers between 0 and 5
    print(f"{factor1} x {factor2} = {factor1 * factor2}")
elif 6 <= smallest <= largest <= 10:
    # method 1: product of two integers between 6 and 10
    print("{} x {} = 10 x ({} + {}) + ({} x {}) = {}".format(
        factor1,
        factor2,
        factor1 - 5,
        factor2 - 5,
        10 - factor1,
        10 - factor2,
        factor1 * factor2
    ))
else:
    # method 2: product of two integers between 10 and 15
    # note: this method also works in general for other products
    print("{0} x {1} = 100 + 10 x ({2} + {3}) + ({2} x {3}) = {4}".format(
        factor1,
        factor2,
        factor1 - 10,
        factor2 - 10,
        factor1 * factor2
    ))

#2.4 Finding mates
# read color and value of first playing card
color1 = input()
value1 = input()
# read color and value of second playing card
color2 = input()
value2 = input()
# determine the color of the first playing card’s mate
if color1 == "spades":
    mate = "clubs"
elif color1 == "hearts":
    mate = "diamonds"
elif color1 == "clubs":
    mate = "spades"
else:
    mate = "hearts"
# determine whether or not the two cards are mates
mates = "not " if mate != color2 or value1 != value2 else ""
# output whether or not the two cards are mates
print(f"the {value1} of {color1} and the {value2} of {color2} are {mates}mates")

# 2.5 APGAR score
# initialisation of score and validity
score, valid = 0, True
# criterium: respiration
observation = input().lower()
if observation == "strong cry":
    score += 2
elif observation == "weak":
    score += 1
elif observation != "absent":
    valid = False
# criterium: pulse rate
try:
    observation = int(input())
    if observation >= 100:
        score += 2
    elif observation > 0:
        score += 1
    elif observation != 0:
        valid = False
except ValueError:
    valid = False
# criterium: muscle tone
observation = input().lower()
if observation == "resist extension":
    score += 2
elif observation == "some flexion":
    score += 1
elif observation != "none":
    valid = False
# criterium: appearance
observation = input().lower()
if observation == "pink":
    score += 2
elif observation == "extremities":
    score += 1
elif observation != "blue" and observation != "pale":
    valid = False
# criterium: reflex irritability
observation = input().lower()
if observation == "cry or pull away":
    score += 2
elif observation == "grimace":
    score += 1
elif observation != "no response":
    valid = False
# make final evaluation based on APGAR score
if not valid:
    print("invalid input")
elif score < 4:
    print("alarm")
else:
    print(score)

#2.6 Stopwatch baby
# read date
day = int(input())
month = input()
year = int(input())
# day
# month name
# year
# determine stopwatch baby"s age in months from month name

#   alternative way to convert month name into age in months of stopwatch baby:
age_months = "january,february,march,april,may,june,july,"
age_months += "august,september,october,november,december"
age_months = (age_months.split(",").index(month.lower()) + 1) % 12

    # determine age in years from year
age_years = year - 2000 + int(not age_months)
    # generate singular or plural version of time units
days = "day" if day == 1 else "days"
months = "month" if age_months == 1 else "months"
years = "year" if age_years == 1 else "years"
    # print formatted age of stopwatch baby
print(
    f"Stopwatch babies are {day} {days}, {age_months} {months} and " +
    f"{age_years} {years} old on {day} {month} {year}."
)


#During class

counter = 5
while counter > 0:
	print(f'{counter}....')
	counter -= 1
print('Ignition !!!!')

number = 1
while number <= 20:
    print(number, number ** 2, number**3, sep = '\t')
    number += 1


