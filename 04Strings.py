#ISBN
# read first ISBN-10 code (or the word stop)
code = input()
# read successive ISBN-10 codes until line containing "stop" is read
while code != 'stop':
    # compute check digit
    check_digit = int(code[0])
    for i in range(2, 10):
        check_digit += i * int(code[i - 1])
    check_digit %= 11
    """
    # compute check digit: alternative solution using list comprehension
    check_digit = sum((i + 1) * int(code[i]) for i in range(9)) % 11
    """
    # extract check digit from ISBN-10 code
    x10 = code[-1]
    # check whether computed and extracted check digits are the same
    if (check_digit == 10 and x10 == 'X') or x10 == str(check_digit):
        print('OK')
    else:
        print('WRONG')
    # read next ISBN-10 code (or the word stop)
    code = input()

#Piece of cake
# read given number
number = input()
# repeat procedure until it yields number 123
while number != '123':
    # determine number of even and odd digits
    even, odd = 0, 0
    for digit in number:
        if int(digit) % 2:
            odd += 1
        else:
            even += 1
    # string together the three numbers to come up with a new number
    number = f'{even}{odd}{len(number)}'
    # output resulting number
    print(number)

#Torn numbers
def torn(number):
    """
    Returns a Boolean that indicates whether the given number is torn.
    >>> torn(88209)
    True
    >>> torn(88210)
    False
    """

    # convert the number into a string if this were not already the case
    number = str(number)
    # try out all possible combinations to tear the number in two halves that
    # each contain at least one digit
    for pos in range(1, len(number)):
        part1, part2 = int(number[:pos]), int(number[pos:])
        if (part1 + part2) ** 2 == int(number):
            return True
    # number is not torn because none of the combinations were valid
    return False
    # read number and determine whether or not it is torn
negation = '' if torn(input()) else 'not'
print(f'{negation}torn')

#The Ghent University prime number
# read frequently occurring characters
characters = input()
# read image row by row until unique character has been found
row = 0
found = False
while not found:
    # read next row
    row += 1
    line = input()
    # check all characters on the row one by one
    col = 0
    while not found and col < len(line):
        # check if unique character has been found
        if line[col] not in characters:
            found = True
        # goto next column
        col += 1
print(f"character '{line[col - 1]}' only occurs at row {row} and column {col}")

#Suskewiet
# read the number of songs
songs = int(input())
# count the number of valid songs
valid = 0
for _ in range(songs):
    # read the next song
    song = input()
    # cleanup song: convert to lowercase and only retain letters
    song = ''.join(letter for letter in song.lower() if letter.isalpha())
    # determine whether song is valid
    if song[-9:] == 'suskewiet' and all(l in 'ktreu' for l in song[:-9]):
        valid += 1
# mark a line for each of valid song
songs = '||||| ' * (valid // 5) + '|' * (valid % 5)
print(songs.rstrip())

#Bible codes
# read instructions to find the secret message
start = int(input()) - 1 # position of first letter of the message
step = int(input()) # step size to find the next letter
length = int(input()) # length of the secret message
# read entire text fragment and only retain its letters
fragment = '' # initialize letters in text fragment
line = input() # read first line of text fragment
while line: # continue as long as line contains letters
    for letter in line: # traverse all characters on the line
        if letter.isalpha(): # only retain letters
            fragment += letter # append letter at the end of the fragment
    line = input() # read next line
# use instructions to read the secret word from the text fragment, either until
# all letters are read or until an end of the fragment is exceeded
word = ''
while len(word) < length and 0 <= start < len(fragment):
    word += fragment[start]
    start += step
# complete word with extra question marks until it has the requested length
word += '?' * (length - len(word))
# output the secret message
print(word)
