import re
import argparse

parser=argparse.ArgumentParser(description='match any regex rule against a file')
parser.add_argument('file',help='the file to run regex against')
parser.add_argument('-r',help='a single regex rule to match for')
arg=parser.parse_args()
content=open(arg.file,'r').read()
regex=re.compile(arg.r)
print(regex.findall(content))
