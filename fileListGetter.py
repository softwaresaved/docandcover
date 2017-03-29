import os

def fileListGetter(directory):
    """
    Function to get list of files and language types 
    Inputs:  directory: Stirng containing path to search for files in.
    Outputs:  List of Lists.  Lists are of format, [filename, language type]
    """
    fileLists = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_extention = filename.split(".")[-1]
            languageType = getLanguageType(file_extention)

            fileLists.append([filename, languageType])

    return fileLists

def getLanguageType(file_extention):
    """
    Function to assign language type based on file extention.
    Input: file_extention: String that lists file type.
    Output: languageType: string listsing identified language type.
    """

    if file_extention == 'py':
        return 'python'
    else:
        return 'Unknown'

def printFileLists(fileLists):
    """
    Function to print out the contents of fileLists
    Main use is debugging
    """

    for fileList in fileLists:
        print fileList
    
