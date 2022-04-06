import os
import pyperclip as pc
try:
    os.system("start /b python spider.py -d {} -o file.txt ".format(pc.paste()))
except:
    print("Command could not run")
    
