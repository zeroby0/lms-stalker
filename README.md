# lms-stalker
Logs online users every 60 seconds and logs into a JSON file

dependencies:
requests, BeautifulSoup

Usage:
If you'd like to run forever on a server, use `screen`  
make a folder called public in the same dir as this script. this is where beautified json and archives are kept  
To make the files publicly accessible, you can run a simple HTTP server in python, do that in `public` folder

screen cheatsheet (for me):
screen -ls # show processes
screen -r ID
ctrl a + d # detach




