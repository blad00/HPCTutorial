#ISBN
def isISBN(code):
    """
    Return True if the argument is a string that contains a valid ISBN-10 code,
    False otherwise.
    >>> isISBN('9971502100')
    True
    >>> isISBN('9971502108')
    False
    >>> isISBN('53WKEFF2C')
    False
    >>> isISBN(4378580136)
    False
        """
    # note: isinstance is a Python built-in function that returns a Boolean
    # value that indicates whether the first argument is an object that
    # has a data type equal to the second argument
    if not (
        isinstance(code, str) and # code must be a string
        len(code) == 10 and # code must contain 10 characters
        code[:9].isdigit() # first nine characters must be digits
    ):
        return False
    # check the check digit
    return checkdigit(code) == code[-1]

def checkdigit(code):
    """
    Computes the check digit for a given string that contains the first nine
    digits of an ISBN-10 code.
    >>> checkdigit('997150210')
    '0'
    >>> checkdigit('938389293')
    '5'
    """
    # compute check digit
    check = sum((i + 1) * int(code[i]) for i in range(9)) % 11
    # convert check digit into string representation
    return 'X' if check == 10 else str(check)
if __name__ == '__main__':
    import doctest
    doctest.testmod()


#Table talk

def chemifyWord(word):
    """
    >>> chemifyWord('California')
    'Californium'
    >>> chemifyWord('BERKELEY')
    'BERKELium'
    >>> chemifyWord('of')
    'ofium'
    >>> chemifyWord('Belgium')
    'Belgium'
    """

    # determine word stem by removing all vowels at the end of the word
    word = word.rstrip('aeiouyAEIOUY')
    """
    # alternative implementation
    while word and word[-1].lower() in 'aeiouy':
        word = word[:-1]
    """
    # append suffix -ium to word stem (if this is not already the case)
    if not word.endswith('ium'):
        word += 'ium'
    # return modified word
    return word

def chemify(sentence):
    """
    >>> chemify('University of California, Berkeley')
    'Universitium ofium Californium, Berkelium'
    >>> chemify('Ghent University, Belgium')
    'Ghentium Universitium, Belgium'
    >>> chemify('Cooking is chemistry, really.')
    'Cookingium isium chemistrium, reallium.'
    >>> chemify('To think is to practice brain chemistry.')
    'Tium thinkium isium tium practicium brainium chemistrium.'
    >>> chemify('I guess chemistry is just another word for love.')
    'ium guessium chemistrium isium justium anotherium wordium forium lovium.'
    """

    # process separate words in sentence, using the definition that a word is a
    # longest possible sequence of consecutive letters
    modified = ''
    word = ''
    for character in sentence:
        if character.isalpha():
            word += character
        else:
            if word:
                modified += chemifyWord(word)
                word = ''
            modified += character
    # process last word if unprocessed (happens when sentence ends in a letter)
    if word:
        modified += chemifyWord(word)

    # return modified sentence
    return modified

    """
    # alternative implementation that uses regular expressions
    # replace all words by their chemified version
    import re
    return re.sub(
        '[a-z]+',
        lambda word: chemifyWord(word.group(0)),
        sentence,
        flags=re.IGNORECASE
    )
    """


#Stop codons
def isStopCodon(codon):
    """
    >>> isStopCodon('TAA')
    True
    >>> isStopCodon('tag')
    True
    >>> isStopCodon('ATC')
    False
    """
    return codon.upper() in {'TAA', 'TAG', 'TGA'}

def reverseComplement(seq):
    """
    >>> reverseComplement('AAGTC')
    'GACTT'
    >>> reverseComplement('agcttcgt')
    'ACGAAGCT'
    >>> reverseComplement('AGTCTTACGCTTA')
    'TAAGCGTAAGACT'
    """
    complement = dict(zip('ACGT', 'TGCA'))
    return ''.join(complement[base] for base in seq[::-1].upper())

def stopCodons(seq, frame):
    """
    >>> seq = 'TTTACTATAGTGATAGCCGGTAACATAGCTCCTAGAATAAAGGCAACGCAATACCCCTAGG'
    >>> stopCodons(seq, +1)
    1
    >>> stopCodons(seq, +2)
    5
    >>> stopCodons(seq, +3)
    2
    >>> stopCodons(seq, -1)
    3
    >>> stopCodons(seq, -2)
    0
    >>> stopCodons(seq, -3)
    1
    """
    if frame < 0:
        frame, seq = -frame, reverseComplement(seq)
    return sum(isStopCodon(seq[i:i + 3]) for i in range(frame - 1, len(seq), 3))

def codons(seq, frame):
    """
    >>> seq = 'TTTACTATAGTGATAGCCGGTAACATAGCTCCTAGAATAAAGGCAACGCAATACCCCTAGG'
    >>> codons(seq, +1)
    'TTT-ACT-ATA-GTG-ATA-GCC-GGT-AAC-ATA-GCT-CCT-AGA-ATA-AAG-GCA-ACG-CAA-TAC-CCC-TAG-G'
    >>> codons(seq, +2)
    'T-TTA-CTA-TAG-TGA-TAG-CCG-GTA-ACA-TAG-CTC-CTA-GAA-TAA-AGG-CAA-CGC-AAT-ACC-CCT-AGG'
    >>> codons(seq, +3)
    'TT-TAC-TAT-AGT-GAT-AGC-CGG-TAA-CAT-AGC-TCC-TAG-AAT-AAA-GGC-AAC-GCA-ATA-CCC-CTA-GG'
    17
    >>> codons(seq, -1)
    'CCT-AGG-GGT-ATT-GCG-TTG-CCT-TTA-TTC-TAG-GAG-CTA-TGT-TAC-CGG-CTA-TCA-CTA-TAG-TAA-A'
    >>> codons(seq, -2)
    'C-CTA-GGG-GTA-TTG-CGT-TGC-CTT-TAT-TCT-AGG-AGC-TAT-GTT-ACC-GGC-TAT-CAC-TAT-AGT-AAA'
    >>> codons(seq, -3)
    'CC-TAG-GGG-TAT-TGC-GTT-GCC-TTT-ATT-CTA-GGA-GCT-ATG-TTA-CCG-GCT-ATC-ACT-ATA-GTA-AA'
    """
    if frame < 0:
        frame, seq = -frame, reverseComplement(seq)

    frame = {1: 0, 2: -2, 3: -1}[frame]
    return '-'.join(
        seq[max(i, 0):i + 3]
        for i in range(frame, len(seq), 3)
    )

if __name__ == '__main__':
    import doctest
    doctest.testmod()

#Reversals
def abecedarian(word, alphabet):
    """
    >>> abecedarian('Aegilops', 'abcdefghijklmnopqrstuvwxyz')
    True
    >>> abecedarian('billowy', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    True
    >>> abecedarian('spoon-feed', 'abcdefghijklmnopqrstuvwxyz')
    False
    >>> abecedarian('spoon-feed', 'zyxwvutsrqponmlkjihgfedcba')
    True
    """
    # convert word to lowercase and remove all characters that are not letters
    word = ''.join(c for c in word.lower() if c.isalpha())
    # convert alphabet to lowercase
    alphabet = alphabet.lower()
    # check if all letters are in the same order as in the second string
    return all(
        alphabet.find(word[i]) <= alphabet.find(word[i + 1])
        for i in range(len(word) - 1)
    )

def reversal(word):
    """
    >>> reversal('Marshall')
    'Llahsram'
    >>> reversal('BeAn')
    'NaEb'
    >>> reversal('Aegilops')
    'Spoligea'
    """
    # reverse order of letters but retain uppercase and lowercase
    return ''.join(
        c1.lower() if c2.islower() else c1.upper()
        for c1, c2 in zip(word[::-1], word)
    )
def doubleReversal(sentence):
    """
    >>> doubleReversal('Marshall Bean')
    'Naeb Llahsram'
    >>> doubleReversal('Barak Obama')
    'Amabo Karab'
    >>> doubleReversal('Yitzhak Rabin')
    'Nibar Kahztiy'
    >>> doubleReversal('Jar Jar Binks')
    'Sknib Raj Raj'
    >>> doubleReversal('Klat Rehctub')
    'Butcher Talk'
    """
    # reverse word order and reverse order of letters but retain uppercase and
    # lowercase
    return ' '.join(reversal(name) for name in reversed(sentence.split()))
    if __name__ == '__main__':
        import doctest
    doctest.testmod()

#Pangrammatic window

def pangram(sentence):
    """
    >>> pangram("The quick brown fox jumps over the lazy dog.")
    True
    >>> pangram("The quick brown fox jumped over the lazy dog.")
    False
    >>> pangram("AbCdEfGhIjKlMnOpQrStUvWxYz")
    True
    """

    # convert all letters into lower case
    sentence = sentence.lower()
    # check whether if there is a letter of the alphabet missing in the sentence
    import string
    for letter in string.ascii_lowercase:
        if letter not in sentence:
            # letter found that does not occur in the sentence
            return False
    # all letters occur in the sentence
    return True

def window(sentence):
    """
    >>> window("The quick brown fox jumps over the lazy dog.")
    "quick brown fox jumps over the lazy dog"
    >>> window("The quick brown fox jumped over the lazy dog.")
    >>> window("I sang, and thought I sang very well; but he just looked up into my face with a very quizzical expression, and said, How long have you been singing, Mademoiselle")
    "g very well; but he just looked up into my face with a very quizzical ex"
    >>> window("We are all from Xanth," Cube said quickly. "Just visiting Phaze. We just want to find the dragon.")
    "from Xanth," Cube said quickly. "Just visiting Phaze. W"
    """
    # if sentence is itself not a pangram, it cannot contain a pangrammatic
    # substring
    if not pangram(sentence):
        return None
    # shortest pangrammatic substring is initialized to the entire sentence
    window = sentence
    # traverse all possible start positions: we take into account that the
    # window needs bridge at least 26 characters
    for start in range(len(sentence) - 26):
        # traverse all possible stop positions: we take into account that
        # windows needs to bridge at least 26 characters and that they need to
        # be shorter than the shortest pangrammatic substring found so far
        length, isPangram = 26, False
        while (
            length < len(window) and
            # must be < shortest found so far
            start + length <= len(sentence) and # don"t go beyond end of sentence
            not isPangram # stop if pangram found
        ):
            # check if substring is a pangram in case the last character of the
            # substring is a letter; can not be a pangram if the last character
            # is not a letter, otherwise the previous substring would also have
            # been a (shorter) pangram
            if sentence[start + length - 1].isalpha():
                substring = sentence[start:start + length]
                if pangram(substring):
                    window = substring
                    isPangram = True
            length += 1
    return window
if __name__ == "__main__":
    import doctest
    doctest.testmod()

#Rövarspråket

def encode(text):
    """
    >>> encode("robber language")
    "rorobbobberor lolangonguagoge"
    >>> encode("Kalle Blomkvist")
    "Kokallolle Bloblomkvomkvistost"
    >>> encode("Astrid Lindgren")
    "Astrostridod Lolindgrondgrenon"
    """
    # define vowels
    vowels = "aeiou"
    decoded, consonants = "", ""
    for character in text:
        if character.isalpha() and character.lower() not in vowels:
            # add character to group of consecutive vowels
            consonants += character
        else:
            # if a group of consecutive vowels was formed, add the group to
            # the decoded text, followed by the letter o and a lowercase
            # repetition of the group of vowels; after this a new group of
            # vowels can be started
            if consonants:
                decoded += consonants + "o" + consonants.lower()
                consonants = ""
            # add the non-consonant to the decoded text
            decoded += character

        # if a group of vowels was formed at the end of the text, that group
        # still needs to be added to the decoded text, followed by the letter o and
        # a lowercase repetition of the group of vowels
        if consonants:
            decoded += consonants + "o" + consonants.lower()
        # return decoded text
    return decoded

def decode(text):
    """
    >>> decode("rorobbobberor lolangonguagoge")
    "robber language"
    >>> decode("Kokallolle Bloblomkvomkvistost")
    "Kalle Blomkvist"
    >>> decode("Astrostridod Lolindgrondgrenon")
    "Astrid Lindgren"
    """

    # define vowels
    vowels = "aeiou"
    # plaintext is initialize as the empty string
    plaintext = ""

    # traverse characters of decoded text from left to right, and remember the
    # length of the group of consecutive vowels that is currently seen
    index, consonants = 0, 0
    while index < len(text):
        if text[index].isalpha() and text[index].lower() not in vowels:
            # consonant in first repetition of group of vowels is added in
            # its current form (uppercase or lowercase) to the plaintext
            plaintext += text[index]
            # remember that we have seen another consonant in the current group
            # of consecutive vowels
            consonants += 1
        elif consonants:
            # after the first repetition of a group of consecutive vowels
            # has been seen, we can skip the letter o and the repetition of
            # that group
            index += consonants # skip repetition of second repetition
            consonants = 0 # prepare to see another group of consonants
        else:
            # add non-consonant that has not been skipped to plaintext
            plaintext += text[index]
        # prepare to process the next character
        index += 1
    # return the plaintext
    return plaintext
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()