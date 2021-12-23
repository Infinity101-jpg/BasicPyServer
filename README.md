#### • BasicPyServer
A basic, but very easy to use Python web server for one page sites. Offers basic protection, such as full protection against people accessing the filesystem. As of yet, no external CSS or Javascript files can be used.
~
##### • Requirements
Python 3.8+

No libraries required

~
##### • Usage
Edit `server.py` to change the content and location of the site.

Start `server.bat` to start up the server.

After stopping the server, please run `stop.py`.

~
##### • Examples
Very basic server:
```
def Start():
    return ['oi mate', '.']
```
^ Runs on "localhost"
<br>
```
def Start():
    return ['oi mate', 'hello']
```

^ Runs on "localhost/hello" ("localhost" will be blank, and all other pages will display "404")
```
content = open ('path.html', 'r')
content = content.read()

def Start():
    return ['content', 'wherever you want']
```
(note - you cannot have your html file in the project folder, you must place it in a diffrent folder.)
```
-->base
-->index.html
   -->BasicPyServer
```
this should work great.

just make sure to use "../index.html", or wherever your file is stored.

When the server is stopped, remember to run `stop.py`, otherwise the cache wont be cleared and it will be impossible to choose a new server route.






