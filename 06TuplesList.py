def lineup(*people):
    lineRed = []
    lineBlue = []
    for name, color in people:
        if color == 'red':
            lineRed.append(name)
        else:
            lineBlue.insert(0,name)

    lineRed.append(lineBlue)

    #for name in lineRed:
    print(lineRed)

lineup(['Alice','R'], ['Bob','B'], ['Claire','R'], ['Dave','R'], ['Elsa','B'])

lineup(('Sparkle', 'R'), ('Rolf', 'R'), ('Eileen', 'R'), ('Madie', 'R'))
