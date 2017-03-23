#!/usr/bin/env python
from __future__ import print_function
# https://github.com/zeroby0/lms-stalker
# Aravind Reddy V


import requests
from bs4 import BeautifulSoup
import warnings
import datetime, time, os, json

warnings.filterwarnings("ignore")



class stlk:
        def pack_db(self): # too lazy to find python commands
                os.system("cat " + self.DB_FILE + " | python -mjson.tool > ./public/db.pack.json")
                os.system("cd ./public && zip db.pack.json.zip db.pack.json") # cd ing to avoid unpacking to folder
                os.system("cd ./public && tar -czf db.pack.json.tar.gz db.pack.json")
                # os.system("cp -r ./public/. /var/www/stalk/") # serving files with nginx

        def set_db(self):
                with open( self.DB_FILE, 'w') as f:
                        json.dump(  self.DB , f)

        def get_db(self):
                with open( self.DB_FILE ) as dbase_file:    
                        dbase = json.load(dbase_file)
                        return dbase

        def create_db(self):
                if not os.path.exists( self.DB_FILE ):
                        template = {}
                        with open( self.DB_FILE, 'w') as f:
                                json.dump(template, f)


        def __init__(self,username, password,DB_FILE = "./db.json"):

                self.username = username
                self.password = password
                self.DB_FILE = DB_FILE
                self.create_db()
                self.DB = self.get_db()





        def log_user(self, id):
                if not self.DB.has_key(id):
                        self.DB[id] = {"time_array": []}

                self.DB[id]["time_array"].append( "{:%d %m, %Y, %H %M %S}".format(datetime.datetime.now()) )



        def scan(self):
                payload = {
                        'username': self.username,
                        'password': self.password
                }
                self.DB["0nline"] = [{"Last checked at" : "{:%d %m, %Y, %H %M %S}".format(datetime.datetime.now()) }]
                with requests.Session() as s:
                        p = s.post('https://lms.iiitb.ac.in/moodle/login/index.php', data=payload,verify=False)
                        r = s.get('https://lms.iiitb.ac.in/moodle/my/',verify=False)
                        soup=BeautifulSoup(r.text)
                        g_data=soup.find_all("div",{"class":"user"})
                        print("\n[")
                        for i in g_data:
                                if i.text in [ "imt2015524 Voggu Aravind Reddy"]: continue # Put your ID here
                                print("    " + i.text + ",")
                                self.log_user(i.text)
                                self.DB["0nline"].append(i.text)
                                self.set_db()
                                # self.pack_db()
                                # current_list[i.text] = datetime.datetime.now()
                                # ,i.find_all("a")[0]['title'] // for time

        def stalk(self):
                while True:
                        try:

                                self.scan()
                                print("]")
                                self.pack_db()
                                print("____________________________________________________");
                                time.sleep(60)
                        except:
                                print("Error occured, retrying")




stk = stlk("Roll Number", "Password")
stk.stalk()




