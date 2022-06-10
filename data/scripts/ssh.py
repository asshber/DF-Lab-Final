###############
#  H  I  N  T #
###############
import fabric
import requests
import os
c=fabric.Connection("{username}@{address}:{port}".format(username='username',address='example.com',port='22',),connect_kwargs={"password":'password123'})
#execute commands
c.run('echo "HelloWorld"')
#copy files to the remote container from local
c.put('/some/local/path','/some/remote/path')
#OR
os.system("sshpass -p 'password' scp -r /some/local/path user@example.com:/some/remote/path")
#copy files/directories to local from remote container
os.system("sshpass -p 'password' scp -r user@example.com:/some/remote/path /some/local/path")
#sending a get request
response=requests.get('http://google.com:8080')
print(response.text)
