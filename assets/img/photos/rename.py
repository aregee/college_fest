#! /bin/python
 
# A pythong script to rename files * image files to a similar scheme for better usage

import glob, os

def rename(dir, pattern, titlePattern):
    count = 0 
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, 
                  os.path.join(dir, titlePattern % count + ext))
        count = count + 1
