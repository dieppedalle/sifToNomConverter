





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

def eval(x):
    if not isinstance(x, list):
        #print(x)
        return x
    else:
        proc = eval(x[0])
        args = [eval(arg) for arg in x[1:]]
        #print proc
        #print args

def main():
    stringFile = convertFileToString('input.sif')
    tokens = tokenize(stringFile)
    arrayFile = parse(tokens)
    print(arrayFile)
    eval(arrayFile)



main()
#print file.read()
#stackFunctions = list()
