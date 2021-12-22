import server
import os
try:
    os.mkdir(server.Start()[1])
except:
    pass

os.system('echo. > index.html')
f = open (server.Start()[1]+'/index.html', 'w')
f.write(server.Start()[0])
a = ''
if (server.Start()[1] == '.'):
    a = ''
else:
    a = server.Start()[1]


