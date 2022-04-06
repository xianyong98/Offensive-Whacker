from selenium import webdriver
import os
import pyperclip as pc
driver = webdriver.Chrome(executable_path="2.exe")
driver.maximize_window()
driver.get("{}<ScRiPt>alert(1)</sCriPt>".format(pc.paste()))
