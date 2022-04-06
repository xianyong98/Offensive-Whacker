import os
import pyperclip as pc
try:
    os.system("start /b python gui_helper_scan_xss.py -u {} && start /b python gui_helper_scan_xss.py -u {} > test.txt".format(pc.paste(),pc.paste()))
except:
    print("Command could not run")
    
