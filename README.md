# lms-stalker
Logs online users every 60 seconds and logs into a JSON file

Dependencies:
requests, BeautifulSoup

Usage:  
If you'd like to run forever on a server, use `screen`  
make a folder called public in the same dir as this script. this is where beautified json and archives are kept  
To make the files publicly accessible, you can run a simple HTTP server in python, do that in `public` folder

Screen Cheatsheet (for me):  
screen -ls # show processes  
screen -r ID  
ctrl a + d # detach  

sample output to json:
 ``` JSON
{
	"imt201X5X3 Vinay Chandrasekhar K": {
        "time_array": [
            "31 02, 2025, 19 49 48",
            "31 02, 2025, 19 50 51",
            "31 02, 2025, 19 51 54",
            "31 02, 2025, 19 52 56",
            "31 02, 2025, 19 53 59",
        ]
    },
}
 ```

 License: MIT





