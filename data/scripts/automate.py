import os
import fabric
import json

#pehli baar script normally chalay gi lekin kuch output nhi aye ga dusri baar line 20 comment hogi aur phir files banay gi.

# To connect 
# mysql -u {username} -p'{password}' \
#     -h {remote server ip or name} -P {port} \
#     -D {DB name}

f=json.load(open("instances.json",'r'))
ip="192.168.0.104"
for machine in f:
    os.system('mkdir {0}'.format(machine))
    for services in f[machine]:
            if(services=="ssh"):
                c=fabric.Connection("{0}@{1}:{2}".format(f[machine]["ssh"]["username"],ip,f[machine]["ssh"]["port"]),connect_kwargs={"password":'{0}'.format(f[machine]["ssh"]["password"])})
                os.system('sshpass -p {4} scp -r -P {0} ./my_dump_mem root@localhost:/'.format(f[machine][services]["port"],f[machine][services]["username"],ip,machine,f[machine][services]["password"]))
                c.run('python3 /my_dump_mem.py --pids "$(ps -aux | awk \'{print $2}\')"') #command here
                os.system('sshpass -p {4} scp -r -P {0} {1}@{2}:/var/log ./{3}'.format(f[machine][services]["port"],f[machine][services]["username"],ip,machine,f[machine][services]["password"]))
            if(services=="db"):
                os.system('sshpass -p {4} scp -P {0} {1}@{2}:/var/log/db.log ./{3}'.format(f[machine][services]["port"],f[machine][services]["username"],ip,machine,f[machine][services]["password"]))
            if(services=="http"):
                os.system('sshpass -p {4} scp -r -P {0} {1}@{2}:/etc/ ./{3}'.format(f[machine][services]["port"],f[machine][services]["username"],ip,machine,f[machine][services]["password"]))
            if(machine==""): #edit the machine name here 
                c.run('ps -aux') #command here
            print("{0} done".format(machine))
