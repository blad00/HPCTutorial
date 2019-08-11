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

