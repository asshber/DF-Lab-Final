import sys
pid=205142
map_file = f"/proc/{pid}/maps"
mem_file = f"/proc/{pid}/mem"
out_file = f"{pid}.dump"
out_file = f"{pid}.map"
mapf=open(map_file, 'r')
memf=open(mem_file, 'rb')
outf=open('ww', 'wb')
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
