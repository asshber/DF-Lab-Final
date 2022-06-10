import os
import yara
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path',help='Add the path you want the rules to match')
parser.add_argument('-r',help='yara rule here.')
arg = parser.parse_args()
testing = arg.path
rules=yara.compile(filepath=arg.r)


def dir_iterator(basepath):
    with os.scandir(basepath) as files:
        for file in files:
            if file.is_dir():
                dir_iterator(basepath+file.name+"/")
            else:
                if rules.match(basepath+file.name):
                    print(rules.match(basepath+file.name))
                    print(basepath+file.name)


dir_iterator(testing)

