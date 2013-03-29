#! /bin/python
 
# A pythom utility to rename files of a particular type to a similar naming pattern 
import glob, os

def rename(dir, pattern, titlePattern):
    count = 0 
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, 
                  os.path.join(dir, titlePattern % count + ext))
        count = count + 1


def main():
    patt = os.getcwd()
    pat = raw_input("enter re for type of file to change\t")
    rempat = raw_input("Enter the filename you need\t")

    
    
    rename(patt, pat , rempat)


if __name__ == "__main__":
    main()
