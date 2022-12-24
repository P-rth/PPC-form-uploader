#pip install pillow
#pip install requests
#pip install selenium
#pip install webdriver-manager
#pip install re
from pathlib import Path
import re

from PIL import Image
import requests
import os
import re

class_val = int(input("Enter class:"))


os.system('cls||clear')
loc = "links.txt"
try:
    f = open(loc)
except:
    print("links.txt not found please enter location:")
    print("Go to file > right click while holding shift > copy as path > paste here")
    path = input("--> ")
    path = path.replace('"','')
    f = open(path)

links = f.read()
a = links.split(", ")
z = 0


while True:
    start=int(input("Enter Start location (0 to "+str(len(a))+") :" ))
    if start < 0 or start > len(a):
        print("Invalid Value Try again")
    else:
        break


 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time




options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--log-level=3")





browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),chrome_options=options)
browser.get("https://innovateindia.mygov.in/ppc-2023/student-through-teacher/")
os.system('cls||clear')
input("Log in and press enter")
#login





def fillform(imgurl):
    browser.get("https://innovateindia.mygov.in/ppc-2023/student-through-teacher/")
    time.sleep(0.5)

    while True:
        try:
            school_name = browser.find_element(By.ID, "school_name")
            school_name.send_keys("NEW ERA PUBLIC SCHOOL")
            
            school_address = browser.find_element(By.ID, "school_address")
            school_address.send_keys("H-17, Mayapuri Rd, Mayapuri, New Delhi, Delhi 110064")
            
            pincode = browser.find_element(By.ID, "pincode")
            pincode.send_keys("110064")
            
            link = browser.find_element(By.ID, "theme_activity")
            link.send_keys(imgurl)
            
            grade = Select(browser.find_element(By.ID, "class"))
            grade.select_by_value(str(class_val))
            
            board = Select(browser.find_element(By.ID, "board"))
            board.select_by_value('CBSE-Private Schools')
            
            state = Select(browser.find_element(By.ID, "state"))
            state.select_by_value('30')
            
            time.sleep(1)
            
            district = Select(browser.find_element(By.ID, "district"))
            district.select_by_value('West')
            break
        except:
            os.system('cls||clear')
            print("cant find some form details ignore/retry (i/r)" )
            if input("--> ") == "r":
                continue
            else:
                break
                   

    
    

for i in range(start,len(a)):
    k = a[i]
    fileid = k.split("/")[5]
    imgurl = "https://drive.google.com/uc?export=view&id="+fileid
    
    im_req = requests.get(imgurl, stream=True).raw
    im_header = im_req.headers['content-disposition']
    fname = re.findall("filename=(.+)", im_header)[0]
    
    if fname.endswith('.pdf'):
        ispdf = 1
        os.system("start "+a[i])
    else:
        ispdf = 0
        im = Image.open(a[i])
        im.show()
        
    
    os.system('cls||clear')
    print("*********************")
    print(str(i)+") "+imgurl)
    print("*********************")
    fillform(imgurl)
    


        
    input("When done press enter ")
    
    if ispdf == 0:
        os.system('taskkill /f /im dllhost.exe >nul 2>&1')
    elif ispdf == 1:
        os.system('taskkill /f /im Acrobat.exe >nul 2>&1')
    
        


    
