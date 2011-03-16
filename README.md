#PMPH_Server / (Portable Micro Python HTTP Server)

###PMPH is a small httpd that I wrote to use on dev boxes and laptops with limited space.

Supported on all OS's that I've tested thus far (Vista, GNU/Linux, MacOSX)
As with any server, run only on available ports, this means if you have apache or IIS running on standard 80, you need to change the port number to the available port ranges (49152-65535), I like 8000 or 9000 myself...

###Supports GET content types: html, css, xml, images, json, js, png, gif, and jpg.

#Try it!
##Go to demo/ and run the demo.py script to see it in action, it will tell you the local ip of the machine it's running on if you'd like to use it remotely
##Server runs on 0.0.0.0 for remote access and listens on port 80, you can change this if you have apache or something going on that port.

