fileLists = [['fileListGetter.py', 'python']]

import re

def functionDetailGetter(fileLists):
    """
    Function to get list of fuctions in file and associated outputs.
    Input: fileLists : List of Lists. Lists are a pair of strings, format
    filename, language type.

        Output is functionDetails:
    [
    string: docandcover.py, # file
    string: fileSearch, # function name
    string: [ filename, filetype], # list of inputs
    string: [ my_output], # list of outputs
    string: snippet # documention or comments
    ]
    """
    functionDetails = []
    
    for fileList in fileLists:
        filename = fileList[0]
        languageType = fileList[1]

        if languageType == 'python':
            pythonFunctionDetailsGetter(filename, functionDetails)
        else:
            continue
        
    return functionDetails


def pythonFunctionDetailsGetter(filename, functionDetails):
    """ 
    Function to search through python files and extract functions, inputs,
    outputs and comments.  These are appened to the list passed to it
    Input: filename (and path) as string, functionDetails as list
    OUtput: none, modifies input.

    functionDetails layout:
    [
    string: docandcover.py, # file
    string: fileSearch, # function name
    string: [ filename, filetype], # list of inputs
    string: [ my_output], # list of outputs
    string: snippet # documention or comments
    ]
    """
    functionName = ''
    functionInputs = ''
    #    file = open(filename)
    f = open(filename, 'r')
    lineContainingFunction = ''
    linesIncludingComments  = ''
    for line in f.read().split('\n'):
        if re.search('\s*def\ ', line):
            lineContainingFunction = line
            cleanedLine = re.sub('.*def\ ','', lineContainingFunction)
            #            if cleanedLine:
            functionNameMatch = re.search('([a-zA-Z0-9_]+)\(', cleanedLine)
            functionName = functionNameMatch.group(1)
                
            functionInputsMatch = re.search('\((.+)\)', cleanedLine)
            if functionInputsMatch:
                functionInputs = [parameter.strip() for parameter in (functionInputsMatch.group(1)).split(',')]
            else:
                functionInputs = []
            
            linesIncludingComments = ''
        linesIncludingComments += line

        if re.search('\"\"\".*\"\"\"', linesIncludingComments) and functionName:
            #We are at the end of a comment, process and clean data
     
            functionDetail = [filename, functionName, functionInputs, [], linesIncludingComments]
            functionDetails.append(functionDetail)
            linesIncludingComments = ''

    f.close()

    return

def bar():
    return 1


print functionDetailGetter(fileLists)
