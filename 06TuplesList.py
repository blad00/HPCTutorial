#ISBN
def isISBN(code):
    """
    Checks whether the given ISBN-10 code is valid.
    >>> isISBN("9-9715-0210-0")
    True
    >>> isISBN("997-150-210-0")
    False
    >>> isISBN("9-9715-0210-8")
    False
    """
    # check if the given code is a string
    if not isinstance(code, str):
        return False
    # check whether dashes are at the correct positions and whether each group
    # has the correct number of digits
    groups = code.split("-")
    if tuple(len(e) for e in groups) != (1, 4, 4, 1):
        return False
    # remove dashes from the given code
    code = "".join(groups)
    # check whether or all characters (except the final one) are digits
    if not code[:-1].isdigit():
        return False
    # check the check digit of the given code
    return checkdigit(code) == code[-1]

def checkdigit(code):
    """
    >>> checkdigit("997150210")
    "0"
    >>> checkdigit("938389293")
    "5"
    """
    # compute check digit
    check = sum((i + 1) * int(code[i]) for i in range(9)) % 11
    # convert check digit into its string representation
    return "X" if check == 10 else str(check)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Lineup
def lineup(persons):
    """
    >>> lineup([("Alice", "R"), ("Bob", "B"), ("Claire", "R"), ("Dave", "R"), ("Elsa", "B")])
    ["Alice", "Claire", "Dave", "Elsa", "Bob"]
    >>> lineup([("Sparkle", "R"), ("Rolf", "R"), ("Eileen", "R"), ("Madie", "R")])
    ["Sparkle", "Rolf", "Eileen", "Madie"]
    >>> lineup((("Brian", "B"), ("Margot", "B"), ("Hans", "B"), ("Lucinda", "B")))
    ["Lucinda", "Hans", "Margot", "Brian"]
    """
    # start with an empty line
    line = []
    # initialize break point (this is the position where the next person will be
    # inserted in the line; it points to the position between the persons
    # wearing a red hat and persons wearing a blue hat and corresponds to the
    # number of persons wearing a red hat that are before the break point)
    breakpoint = 0
    # insert next person at the break point and shift the break point one
    # position to the right in case the person wears a red hat (one more person
    # with a red hat before the break point)
    for name, color in persons:
        line.insert(breakpoint, name)
        if color == "R":
            breakpoint += 1
    # return the names of the person as they have finally lined up
    return line

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#Recoupling
def divide(word, groups):
    """
    >>> divide("accost", 3)
    ["ac", "co", "st"]
    >>> divide("COMMIT", 3)
    ["CO", "MM", "IT"]
    >>> divide("accolade", 4)
    ["ac", "co", "la", "de"]
    >>> divide("COMMUNED", 4)
    ["CO", "MM", "UN", "ED"]
    >>> divide("programming", 5)
    Traceback (most recent call last):
    AssertionError: invalid division
    """
    # check if word length is a multiple of the number of groups
    assert not len(word) % groups, "invalid division"
    # determine length of each group
    lengte = len(word) // groups
    # divide word into groups of equal length
    return [
        word[group * lengte:(group + 1) * lengte] # not clear
        for group in range(groups)
    ]
def recouple(words, groups):
    """
    >>> recouple(["ACcoST", "COmmIT", "LAunCH", "DEedED"], 3)
    ["ACCOLADE", "communed", "STITCHED"]
    >>> recouple(("ACCOLADE", "communed", "STITCHED"), 4)
    ["ACcoST", "COmmIT", "LAunCH", "DEedED"]
    >>> recouple("cane laws mica tost user".split(), 2)
    ["calamitous", "newscaster"]
    >>> recouple("INDIVIDUAL CHALLENGES".split(), 5)
    ["INCH", "DIAL", "VILE", "DUNG", "ALES"]
    >>> recouple("programming computer games".split(), 5)
    Traceback (most recent call last):
    AssertionError: invalid division
    """
    # NOTE: not all words should have equal length, but we must be able to divide
    #       all words in the same number of groups
    return [
        "".join(parts)
        for parts in zip(*(divide(word, groups) for word in words))# not clear
    ]
if __name__ == "__main__":
    import doctest
    doctest.testmod()

#Doomsday clock

def clock(minutes):
    """
    >>> clock(0)
    "00:00"
    >>> clock(7)
    "23:53"
    >>> clock(123)
    "21:57"
    """
    # convert minutes before midnight into minutes since midnight
    minutes = 24 * 60 - int(minutes)
    # convert minutes since midnight into hours and minutes on 24-hour clock
    hours, minutes = (minutes // 60) % 24, minutes % 60
    # representation on 24-hour clock in format hh:mm
    return f"{hours:02d}:{minutes:02d}"

def progress(adjustments):
    """
    >>> adjustments = "1947 7,1949 3,1953 2,1960 7,1963 12,1968 7,1969 10,1972 12,1974 9,1980 7,1981 4,1983 3,1984 3"
    >>> progress(adjustments)
        ((1947, "23:53"), (1949, "23:57"), (1953, "23:58"), (1960, "23:53"), (1963, "23:48"),
        (1968, "23:53"), (1969, "23:50"), (1972, "23:48"), (1974, "23:51"), (1980, "23:53"),
        (1981, "23:56"), (1983, "23:57"), (1984, "23:57"))
    """
    # intialize list
    progress = []
    # split string into list of adjustments and process individual adjustments
    for adjustment in adjustments.split(","):
        # split adjustment into year and number of minutes before midnight
        year, minutes = adjustment.split()
        # append year and representation on 24-hour clock to list
        progress.append((int(year), clock(int(minutes))))

    # convert list into tuple
    return tuple(progress)

def threat(year, clock):
    """
    >>> adjustments = "1947 7,1949 3,1953 2,1960 7,1963 12,1968 7,1969 10,1972 12,1974 9,1980 7,1981 4,1983 3,1984 3"
    >>> doomsdayclock = progress(adjustments)
    >>> threat(1974, doomsdayclock)
    "23:51"
    >>> threat(1950, doomsdayclock)
    "23:57"
    >>> threat(1965, doomsdayclock)
    "23:48"
    """
    # find latest adjustment preceding or equal to the given year
    index = -1
    while clock[index][0] > year:
        index -= 1
    # return time set at latest adjustment
    return clock[index][1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#Columnar transposition
def reduce(key):
    """
    >>> reduce("BANANARAMA")
    "BANRM"
    >>> reduce("overnumerousnesses")
    "OVERNUMS"
    >>> reduce("Mississippi")
    "MISP"
    """
    # convert key to uppercase and only keep first occurrence of each letter
    letters = []
    for letter in key.upper():
        if letter not in letters:
            letters.append(letter)
    return "".join(letters)

def column_indexing(key):
    """
    >>> column_indexing("BANANARAMA")
    (1,0, 3, 4, 2)
    >>> column_indexing("overnumerousnesses")
    (3,7, 0, 4, 2, 6, 1, 5)
    >>> column_indexing("Mississippi")
    (1,0, 3, 2)
    """
    # reduce key to first occurrence of letters
    key = reduce(key)
    # determine alphabetic position of each letter in reduced key
    position = {letter: position for position, letter in enumerate(sorted(key))}
    # return alphabetic position of columns
    return tuple(position[letter] for letter in key)

def column_order(key):
    """
    >>>column_order("BANANARAMA")
    (1,0, 4, 2, 3)
    >>>column_order("overnumerousnesses")
    (2,6, 4, 0, 3, 7, 5, 1)
    >>>column_order("Mississippi")
    (1,0, 3, 2)
    """
    # determine alphabetic positions of columns
    indexing = column_indexing(key)
    # sort columns by alphabetic position
    columns = [None] * len(indexing)
    for column, index in enumerate(indexing):
        columns[index] = column
        # return columns sorted by alphabetic position
    return tuple(columns)

def encode(message, key):
    """
    >>> encode("It Ain't What You Do...", "BANANARAMA")
    "t'au.Inho.iWYo? tt .A D?"
    >>> encode("lacks ascenders, descenders, and dots in lower case", "overnumerousnesses")
    "cnesooeasnni ?sec se?lc e akds,tw?s,ddnc? rea r?aedrdls"
    >>> encode("One-Mississippi, two-Mississippi", "Mississippi")
    "nisptMipOMip -si-si,ossiessiwisp"
    """
    # determine columns sorted by alphabetic position
    columns = column_order(key)
    # determine number of rows and columns in the grid
    cols = len(columns)
    rows = len(message) // cols
    # fill message with question marks
    if len(message) % cols:
        message += "?" * (cols - (len(message) % cols))
        rows += 1
    # traverse columns in alphabetic order and read rows top to bottom
    return "".join(message[r * cols + c] for c in columns for r in range(rows))

def decode(message, key):
    """
    >>> decode("t’au.Inho.iWYo? tt .A D?", "BANANARAMA")
    "It Ain’t What You Do...??"
    >>> decode("cnesooeasnni ?sec se?lc e akds,tw?s,ddnc? rea r?aedrdls", "overnumerousnesses")
    "lacks ascenders, descenders, and dots in lower case?????"
    >>> decode("nisptMipOMip -si-si,ossiessiwisp", "Mississippi")
    "One-Mississippi, two-Mississippi"
    """
    # determine positions of columns in alphabetic order
    indexing = column_indexing(key)
    # determine number of rows and columns in the grid
    cols = len(indexing)
    assert not len(message) % cols, "invalid message"
    rows = len(message) // cols
    # read rows top to bottom and traverse columns in alphabetic order
    return "".join(message[c * rows + r] for r in range(rows) for c in indexing)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#Queens, knights and pawns

def chessboard(rows, cols, pieces):
    """
    >>> chessboard(4, 4, ((’K’, 0, 1), (’Q’, 0, 3), (’P’, 1, 2), (’Q’, 1, 3)))
    [[’’, ’K’, ’’, ’Q’], [’’, ’’, ’P’, ’Q’], [’’, ’’, ’’, ’’], [’’, ’’, ’’, ’’]]
    >>> chessboard(2, 3, ((’Q’, 0, 1), (’K’, 0, 0)))
    [[’K’, ’Q’, ’’], [’’, ’’, ’’]]
    >>> chessboard(8, 8, ((’Q’, 4, 3), ))
    [[’’, ’’, ’’, ’’, ’’, ’’, ’’, ’’], [’’, ’’, ’’, ’’, ’’, ’’, ’’, ’’], [’’, ’’, ’’, ’’, ’’,
    ’’, ’’, ’’], [’’, ’’, ’’, ’’, ’’, ’’, ’’, ’’], [’’, ’’, ’’, ’Q’, ’’, ’’, ’’, ’’], [’’,
    ’’, ’’, ’’, ’’, ’’, ’’, ’’], [’’, ’’, ’’, ’’, ’’, ’’, ’’, ’’], [’’, ’’, ’’, ’’, ’’,
    ’’, ’’, ’’]]
    >>> chessboard(8, 8, ((’K’, 4, 3), (’K’, 7, 7)))
    [[’’, ’’, ’’, ’’, ’’, ’’, ’’, ’’], [’’, ’’, ’’, ’’, ’’, ’’, ’’, ’’], [’’, ’’, ’’, ’’, ’’,
    ’’, ’’, ’’], [’’, ’’, ’’, ’’, ’’, ’’, ’’, ’’], [’’, ’’, ’’, ’K’, ’’, ’’, ’’, ’’], [’’,
    ’’, ’’, ’’, ’’, ’’, ’’, ’’], [’’, ’’, ’’, ’’, ’’, ’’, ’’, ’’], [’’, ’’, ’’, ’’, ’’,
    ’’, ’’, ’K’]]
    """
# initialize chessboard
    chessboard = [[""] * cols for _ in range(rows)]
    # put pieces on the chessboard
    for piece, row, col in pieces:
        chessboard[row][col] = piece
    return chessboard

def unsafe_squares(rows, cols, pieces):
    """
    >>> unsafe_squares(4, 4, (("K", 0, 1), ("Q", 0, 3), ("P", 1, 2), ("Q", 1, 3)))
    [["", "K", "*’, ’Q’], [’’, ’’, ’P’, ’Q’], [’*’, ’’, ’*’, ’*’], [’’, ’*’, ’’, ’*’]]
    >>> unsafe_squares(2, 3, (("Q", 0, 1), ("K", 0, 0)))
    [[’K’, ’Q’, ’*’], [’*’, ’*’, ’*’]]
    >>> unsafe_squares(8, 8, (("Q", 4, 3), ))
    [[’’, ’’, ’’, ’*’, ’’, ’’, ’’, ’*’], [’*’, ’’, ’’, ’*’, ’’, ’’, ’*’, ’’], [’’, ’*’, ’’,
    ’*’, ’’, ’*’, ’’, ’’], [’’, ’’, ’*’, ’*’, ’*’, ’’, ’’, ’’], [’*’, ’*’, ’*’, ’Q’, ’*’,
    ’*’, ’*’, ’*’], [’’, ’’, ’*’, ’*’, ’*’, ’’, ’’, ’’], [’’, ’*’, ’’, ’*’, ’’, ’*’, ’’,
    ’’], [’*’, ’’, ’’, ’*’, ’’, ’’, ’*’, ’’]]
    >>> unsafe_squares(8, 8, (("K", 4, 3), ("K", 7, 7)))
    [[’’, ’’, ’’, ’’, ’’, ’’, ’’, ’’], [’’, ’’, ’’, ’’, ’’, ’’, ’’, ’’], [’’, ’’, ’*’, ’’,
    ’*’, ’’, ’’, ’’], [’’, ’*’, ’’, ’’, ’’, ’*’, ’’, ’’], [’’, ’’, ’’, ’K’, ’’, ’’, ’’,
    ’’], [’’, ’*’, ’’, ’’, ’’, ’*’, ’*’, ’’], [’’, ’’, ’*’, ’’, ’*’, ’*’, ’’, ’’], [’’,
    ’’, ’’, ’’, ’’, ’’, ’’, ’K’]]
    """
    # initialize chessboard
    board = chessboard(rows, cols, pieces)
    unsafe = "*"
    # define movement directions of queens
    queen = tuple(
        (dr, dc) for dr in range(-1, 2) for dc in range(-1, 2)
        if (dr, dc) != (0, 0)
    )
    # define movement directions of knights
    knight = tuple(
        (dr, dc) for dr in range(-2, 3) for dc in range(-2, 3)
        if abs(dr) + abs(dc) == 3
    )

    # set unsafe positions
    for piece, row, col in pieces:
        if piece == "Q":
            # move in each possible direction until queen hits another piece or
            # falls of the chess board
            for dr, dc in queen:
                r, c = row + dr, col + dc
                while (
                    0 <= r < rows and
                    0 <= c < cols and
                    board[r][c] in ("", unsafe)
                ):
                    board[r][c] = unsafe
                    r += dr
                    c += dc
        elif piece == "K":
            # each possible jump of the knight becomes unsafe
            for dr, dc in knight:
                r, c = row + dr, col + dc
                if (
                    0 <= r < rows and
                    0 <= c < cols and
                    board[r][c] in ("", unsafe)
                ):
                    board[r][c] = unsafe
    return board

def safe_squares(rows, cols, pieces):
    """
    >>> safe_squares(4, 4, (("K", 0, 1), ("Q", 0, 3), ("P", 1, 2), ("Q", 1, 3)))
    6
    >>> safe_squares(2, 3, (("Q", 0, 1), ("K", 0, 0)))
    0
    >>> safe_squares(8, 8, (("Q", 4, 3), ))
    36
    >>> safe_squares(8, 8, (("K", 4, 3), ("K", 7, 7)))
    52
    """
    # count number of safe positions
    return sum(
        sum(piece == "" for piece in row)
        for row in unsafe_squares(rows, cols, pieces)
    )
    """
    alternative:
    # count number of safe positions
    safe = 0
    for row in unsafe_squares(rows, cols, pieces):
        for piece in row:
            if not piece:
                safe += 1
    return safe
    """
if __name__ == "__main__":
    import doctest
    doctest.testmod()