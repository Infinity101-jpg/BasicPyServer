import os
import server

os.remove(server.Start()[1]+'/index.html')
os.rmdir(server.Start()[1])
os.remove('index.html')
