listMeshes = list()

def convertFileToString(filename):
    with open('input/' + filename, 'r') as myfile:
        data=myfile.read()#.replace('\n', '')
    return data

def tokenize(chars):
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(tokens):
    if (len(tokens)==0):
        raise SyntaxError("File is empty")
    currentToken = tokens.pop(0)

    if currentToken == '(':
        currentList = list()
        while tokens[0] != ')':
            currentList.append(parse(tokens))
        tokens.pop(0)
        return currentList
    elif currentToken == ')':
        raise SyntaxError("Missing opening parenthesis")
    else:
        return currentToken

def eval(x, outputFile):

    if not isinstance(x, list):
        #print(x)
        return x
    elif x[0] == "vertices":
        numberVertices = int(x[1])
        currentVertex = 0
        print numberVertices
        for i in range(numberVertices):
            outputFile.write("point v" + str(i) + " (" + x[(2+i)][1] + " " + x[(2+i)][2] + " " + x[(2+i)][3] + ") endpoint\n")
        outputFile.write("\n")
    elif x[0] == "triangles":
        numberTriangles = int(x[1])
        currentTriangle = 0
        print numberTriangles
        meshName = "SIFmesh" + str(len(listMeshes))
        listMeshes.append(meshName)

        outputFile.write("mesh " + meshName + "\n")
        for i in range(numberTriangles):
            outputFile.write("face f" + str(i) + " (")

            for i, vertex in enumerate(x[(2+i)][1:]):
                if i != 0:
                    outputFile.write(" ")
                outputFile.write(vertex)
            outputFile.write(") endface\n")
        outputFile.write("endmesh\n\n")
    else:
        proc = eval(x[0], outputFile)
        args = [eval(arg, outputFile) for arg in x[1:]]

def createMeshes(outputFile):
    for i, mesh in enumerate(listMeshes):
        outputFile.write("instance  mesh" + str(i) + " " + mesh + " scale (1 1 1)  endinstance\n")

def createOutputFile():
    outputFile = open("output.nom", "w")
    outputFile.write("####  CONVERTED FROME A SIF  FILE  ####\n\n")
    return outputFile

import re
def removeComments(stringFile):
    stringFile=stringFile.replace('\n', ' ')
    return (re.sub("(\(\*).*?(\*\))", "", stringFile))
    #print(stringFile)

def main():
    stringFile = convertFileToString('input.sif')
    removeComments(stringFile)
    tokens = tokenize(stringFile)
    arrayFile = parse(tokens)
    #print(arrayFile)
    outputFile = createOutputFile()

    eval(arrayFile, outputFile)
    createMeshes(outputFile)



main()
#print file.read()
#stackFunctions = list()
