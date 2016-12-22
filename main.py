





def convertFileToString(filename):
    with open('input/' + filename, 'r') as myfile:
        data=myfile.read()#.replace('\n', '')
    return data

def tokenize(chars):
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()




stringFile = convertFileToString('input.sif')
arrayFile = tokenize(stringFile)
print(arrayFile)

#print file.read()
stackFunctions = list()
