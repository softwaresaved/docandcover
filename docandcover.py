#input_var='https://github.com/softwaresaved/docandcover/'
input_var='https://github.com/Axelrod-Python/Axelrod'

import os
import shutil
from pygit2 import clone_repository
try:
    shutil.rmtree('tmp-repo')
except:
    pass

try:
    repo = clone_repository(input_var,'tmp-repo')
except:
    pass


from fileListGetter import fileListGetter
from functionDetailGetter import functionDetailGetter

#fileLists = fileListGetter('../snippets/tmp-repo/')
fileLists = fileListGetter('tmp-repo')

for i in functionDetailGetter(fileLists):
    print i

#printFileLists(fileLists)
