from selenium import webdriver
import os
import pyperclip as pc
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("{}<script>alert()</script>".format(pc.paste()))
