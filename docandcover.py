from fileListGetter import fileListGetter
from functionDetailGetter import functionDetailGetter

#fileLists = fileListGetter('../snippets/tmp-repo/')
fileLists = fileListGetter('.')

for i in functionDetailGetter(fileLists):
    print i

#printFileLists(fileLists)
