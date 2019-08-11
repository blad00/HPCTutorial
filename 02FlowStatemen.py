ph = 5.1

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


#Runway
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


