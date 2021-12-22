# BasicPyServer
A basic, but very easy to use Python web server for one page sites. Offers basic protection, such as full protection against people accessing the filesystem.

## Requirements:
Python 3.8+

No packages required

## Usage:
edit Server.py to edit content and location of website

start Server.bat to start the server.

after stopping, please run Stop.py

## Server.py examples

Very basic server:

<code>
    
def Start():
    
    return ['oi mate', '.']<br><br>
    
</code>

https://localhost/


<code>
    
def Start():
    
    return ['oi mate', 'hello']<br><br>
    
</code>

https://localhost/hello

(https://localhost/ will be blank, and other pages will display 404)


<code><br><br>
    
content = open ('path.html', 'r')<br><br>
    
content = content.read()<br><br>
    
def Start():<br><br>
    
    return [content, 'wherever you want']<br><br>
    
</code>

(note - you cannot have your html file in the project folder, you must place it in a diffrent folder.)

<code><br><br>
--> base<br><br>
    
--> index.html<br><br>
    
    --> BasicPyServer<br><br>
    
</code>

this should work great.

just make sure to use "../index.html", or wherever your file is stored.

When the server is stopped, remember to run stop.py, otherwise the cache wont be cleared and it will be impossible to choose a new server route.



