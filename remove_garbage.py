#delete empty folders 
#deleting empty folders throw permission error.
#workaround: move empty folders to del directory and then manually delete the folder
#remove unwanted files (change regex expression accordingly. Line 11)

import os, re
 
PATH = 'D:\media\TV Series'  #change this
DEL = os.path.join(PATH,'del')
 
for (dirpath, dirnames, filenames) in os.walk(PATH):
    for filename in filenames:
        if re.match(r'^.*\.(jpg|png|dat|txt)$', filename): #change regex expression
            os.remove(os.path.join(dirpath, filename))
            
i=0
for (dirpath, dirnames, filenames) in os.walk(PATH):
    for dirname in dirnames:
        if len(os.listdir(os.path.join(dirpath,dirname))) == 0:
            try:
                os.renames(os.path.join(dirpath,dirname),os.path.join(DEL,dirname+str(i)))
                i+=1
            except FileExistsError:
                print(os.path.join(dirpath,dirname))
