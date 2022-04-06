# Offensive Whacker

Offensive Whacker (OW!) is created as part of an ICT2206 Assignment 1. This is an offensive tool created to automate Cross-Site Scripting (XSS) attacks as well as scan for vulnerabilities. The purpose of the creation of this tool is to allow users to use an all in one tool to perform their XSS attacks without the need of switching programs as well as to allow users who are less experienced to use our pre-made XSS code which reduces the time spent on researching and creating payload as this component continuously scans the site’s URL field and injects a large list of pre-written XSS codes into it.

## Installation

Offensive Whacker (OW!) requires a few prerequisites to get the program working. It has to run strictly on a Windows environment. Additionally, you would need the following packages below.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these packages.

```shell
pip install PyQT5
pip install PyQT5-WebEngine
pip install selenium
pip install requests
pip install pyperclip
pip install fpdf
```
## Usage

Offensive Whacker (OW!) can be run in an IDE or a windows command-line environment to start you will have to call the main python file as follows:

```shell
python main.py
```

## Features

There are five main features to our program. These five features perform various different kinds of functions and a demonstration of it can be viewed here: https://youtu.be/IHVmZyp67wk

## XSS Vulnerability Scanner

To run this feature, users will be greeted with the XSS Vulnerability Scan tab after running main.py. Users can proceed to click Scan. After that, there would five options to choose from: Scan URL (Full HTML Scan), Scan URL (Fast HTML Scan), Scan URL (Full without HTML Scan) and Scan URL (Fast without HTML Scan). The user would then be prompted to enter the URL that they wish to scan. Once the scan has been completed, users can view the vulnerability payload of the website that they have stated earlier and export the results as a PDF if they wish. 

## Fuzz Scanning

To run this feature, users will be greeted with the Fuzz Scanning tab after running main.py. Users will then input a domain name, for example; singaporetech.edu.sg to generate fuzzed URLs. Upon the generation of the fuzzed URLs, users may choose to export the results as a PDF file. These outputs can then be used alongside the Manual XSS Attack tab to concurrently inject payloads and be able to try to get an XSS URL attack to potentially work.

## DOM Scanner

For this DOM scanning feature, users can scan for DOM-based vulnerabilities on a website. Users are greeted with the DOM Scan tab upon the execution of main.py file. 
Users then can input the URL with the proper parameters. The scan function then outputs the payloads that are available for the user to choose in the DOM attack, it also shows the efficiency and confidence level of the payloads, and users would be able to gauge the chances of the payload to be working as intended. Upon the generation of the DOM-based payloads, users may choose to export the results as a PDF file. Users may choose to attack the URL using the specified payload that is generated. 

## Automatic XSS Attack

For this Automatic XSS Attack feature, users can scan for DOM-based vulnerabilities on a website. Users are greeted with the Automatic XSS tab upon the execution of main.py file. Users can then input the URL that they wish to attack automatically and then click on Start Attack. It automatically launches the Chrome web browser and starts the attack. In addition, it will also automatically launch multiple instances of the web browser to inject the code onto the URL.

## Manual XSS Attack 

For Manual XSS Attacks feature, it provides users with 2 Attack Formats: Website Input Fields and URL. The steps needed to run the attack are as follows: Firstly, the user would enter the target website’s URL in the topmost field. Secondly, he/she would need to choose any of the three XSS Type checkboxes: Basic, Advanced, and Filter, in any combination according to their preference. Thirdly, is the choice of the XSS Payload user would like to perform. Thereafter, the chosen payloads will be displayed in the Craft XSS Payload section. Lastly, before the user could inspect and edit the text in the Craft XSS Payload section and click on the attack button, he/she would need to select the Attack Format: Website Input Fields or URL. After the attack button is pressed, Selenium would be triggered to automate the attack on the chrome browser, based on the attack format: Website Input Fields or URL. After executing the attack, the browser would close automatically after some time. Users would be able to monitor the logs to find out what has exactly happened during the attack. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
