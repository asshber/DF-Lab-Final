import sys
import argparse
import os
parser = argparse.ArgumentParser(description='backup a device into an image')
parser.add_argument('--pids',nargs="+", help='the device to use')
os.system('mkdir /var/log/dumps')
arg=parser.parse_args()
x=str(arg.pids[0])
test=[]
for line in x.split("\n"):
    if(line!="PID"):
        test.append(line)    
print(test)
for pid in test:
    map_file = f"/proc/{pid}/maps"
    mem_file = f"/proc/{pid}/mem"
    out_file = f"{pid}.dump"
    out_file = f"{pid}.map"
    mapf=open(map_file, 'r')
    memf=open(mem_file, 'rb')
    outf=open('/var/log/dumps/{0}'.format(pid), 'wb')
    for line in mapf.readlines():
        section=line.split(' ')
        if section[1][0]=='r':
            addresses=section[0].split('-')
            start=int(addresses[0],16)
            end=int(addresses[1],16)
            memf.seek(int(addresses[0],16))
            try:
                outf.write(memf.read(end-start))
            except OSError:
                print(hex(start), '-', hex(end), '[error,skipped]', file=sys.stderr)
