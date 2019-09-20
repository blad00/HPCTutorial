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