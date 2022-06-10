import os
import re
import argparse



def dir_iterator(basepath):
    with os.scandir(basepath) as files:
        for file in files:
            if file.is_dir():
                dir_iterator(basepath+file.name+"/")
            else:
                content=open(basepath+file.name,'r')
                matchthis=content.read()
                if regex.search(matchthis):
                    print("{} matched with -> Expression \"{}\"".format(basepath+file.name,arg.r))
                    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='Add the path you want the exp to match')
    parser.add_argument('-r',help='regex exp here.')
    arg = parser.parse_args()
    testing=arg.path
    regex=re.compile(arg.r)
    dir_iterator(testing)

