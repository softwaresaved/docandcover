## Functions

def search_for_files

## FileLists
**List all files we think are source code**
*(file,languageType)*  
[  
[docandcover.py,python],  
]  
	
 ^2nd string dictionary needed for future proofing!
 
## FunctionDetails
**List of functions/classes**

*(file, functionName, parameters, returns, doc snippet)*    
[  
string: docandcover.py, # file  
string: fileSearch, # function name  
string: [ filename, filetype], # list of inputs  
string: [ my_output], # list of outputs  
string: snippet # documention or comments  
]  

## DocSnippet
**Parse docSnippet**

+ Mentioned Function Boolean
+ Mentioned Parameter Boolean
+ Mentioned Return Boolean
+ Char in comments

## UserDoc
**Parse user-reader documentation**

+ Mentioned Function Boolean
+ Mentioned Parameter Boolean
+ Mentioned Return Boolean
+ Coverage (typographical hints)
	
## DocStatistics
**Run statistics on parser results**

+ Char in comments
	+ Min
	+ Mode
	+ Max

## Doc and Cover Return
% of functions that are documented
% of each function that is documented
