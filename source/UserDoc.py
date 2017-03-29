import fileinput
import re

lists = [['fileListGetter.py', 'fileListGetter', ['directory', '_nsns'], [], 'def fileListGetter(directory, _nsns):    """    Function to get list of files and language types     Inputs:  directory: Stirng containing path to search for files in.    Outputs:  List of Lists.  Lists are of format, [filename, language type]    """'], ['fileListGetter.py', 'getLanguageType', ['file_extention'], [], 'def getLanguageType(file_extention):    """    Function to assign language type based on file extention.    Input: file_extention: String that lists file type.    Output: languageType: string listsing identified language type.    """'], ['fileListGetter.py', 'printFileLists', ['fileLists'], [], 'def printFileLists(fileLists):    """    Function to print out the contents of fileLists    Main use is debugging    """']]
comments = ""
comment = ""

# for each #2 list item in input
functions = []
newitem =""
for i in lists: 
    newitem = i[1]
    functions.append(newitem)
    
combined = "(" + "|".join(functions) + ")"

comments = comments + "# Functions\n"
for function in functions:
    comments = comments + "\n##"+ (function) + "\n"
    with open("readme.md") as openfile:
        # search for function name, for each instance
        for line in openfile:
            comment = ""
            # if comma-nated
            match = re.search(combined + ", " + "\\b"+re.escape(function)+"\\b",line)
            if match==None:
                match = re.search("\\b"+re.escape(function)+"\\b" + ", " + combined,line)
                if match==None:
                    # if new line
                    match = re.search("^" + "\\b"+re.escape(function)+"\\b" + "[,\" :-]*[*]*[,\" :-]*(.*)",line)
                    if match: 
                        comment = match.group(1) + "\n"
                    else:                    
                        # if not new line or comma-nated
                        match = re.search("\\b"+re.escape(function)+"\\b" + "[,\" :-]*[*]*[,\" :-]*(.*)",line)
                        if match: 
                            comment = match.group(1) + "\n"
            comments = comments + comment
    comments = comments + "\n"

output = str("externaldocresults.md")
text_file = open(output, "w")
text_file.write(comments)
text_file.close()
