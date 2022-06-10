import time
import tarfile
import hashlib
import argparse

parser = argparse.ArgumentParser(description='backup a device into an image')
parser.add_argument('device', help='the device to use')
parser.add_argument('-b',type=int,default=512,help='reading blocksize')
arg=parser.parse_args()
source=open(arg.device,'rb')
tm=str(time.time())
bytes=b'x00'
evidence=open('evidence__'+tm+'.dd','wb')
hash_algo=hashlib.sha256()
while bytes:
	bytes=source.read(arg.b)
	evidence.write(bytes)
	hash_algo.update(bytes)
hash_algo.update(tm.encode())
hash_algo.hexdigest()
source.close()
evidence.close()
compressed=tarfile.open('evidence__'+tm+'.tar','w:xz')
compressed.add('evidence__'+tm+'.dd')
compressed.close()
