file = open('input/input.sif', 'r')

#print file.read()
stackFunctions = list()

for line in file:
    arrayLine = line.split()
    print arrayLine
    for word in line:
        if word[0] == '(':
            currentFunction = word[1:]
            stackFunctions.append(currentFunction)
        else:
            currentWord = word
