import sys

outputFile = open(sys.argv[2], 'w+')
totalCharacters = 0
with open(sys.argv[1], 'r') as f:
    foundChar = False
    while True:
        totalCharacters = totalCharacters + 1
        char = f.read(1)
        if char == '':
            print('End of file!')
            break
        if char == '[':
            if not foundChar:
                print('found [')
            foundChar = True
        if foundChar:
            outputFile.write(char)
        if totalCharacters % 1000000 == 0:
            print('Next million done! Total: ' + totalCharacters)
