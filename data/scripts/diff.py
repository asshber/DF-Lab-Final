from ast import And, arg
import os
import hashlib
import argparse

dir1=[]
dir2=[]
hash1=[]
hash2=[]
def calculate_hash(contents):
    sha256=hashlib.sha256()
    sha256.update(contents)
    my_hash=sha256.hexdigest()
    del sha256
    return my_hash

def list_populator(basepath,list,test):
    with os.scandir(basepath) as files:
        for file in files:
            if file.is_dir():
                list_populator(basepath+file.name+"/",list,test+file.name+"/")
            else:
                list.append(test+file.name)

parser= argparse.ArgumentParser()
parser.add_argument('dir1')
parser.add_argument('dir2')
args=parser.parse_args()

list_populator(args.dir1,dir1,"")
list_populator(args.dir2,dir2,"")
dir1.sort()
dir2.sort()

diff_list=list(set(dir1) ^ set(dir2))
if diff_list:
    for i in diff_list:
        if i in dir1:
            print("{} is missing in {}".format(i,args.dir2))
        else:
            print("{} is missing in {}".format(i,args.dir2))
    exit()
else:
    for i in dir1:
        file=open(args.dir1+i,'rb')
        hash1.append(calculate_hash(file.read()))
    
    for i in dir2:
        file=open(args.dir2+i,'rb')
        hash2.append(calculate_hash(file.read()))
    flag=-1
    for i in range(len(hash1)):
        if hash1[i]!= hash2[i]:
            print("{} is different from {} ".format(args.dir1+dir1[i],args.dir2+dir2[i]))
            flag=1
    if flag==-1:
        print("Both Directories are same.")