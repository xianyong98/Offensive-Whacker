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

There are five main features to our program. These five features perform various different kinds of functions and a demonstration of it can be viewed here:

## XSS Vulnerability Scanner

To run this feature, users will be greeted with the XSS Vulnerability Scan tab after running main.py as seen in Figure 1.

![image](https://user-images.githubusercontent.com/71886838/161992523-340e9561-4b41-48ae-a623-9e313b3b0a83.png)

Figure 1

Users can proceed to click Scan; the following output will be shown in the command line as seen in Figure 2.  There are five options to choose from: Scan URL (Full HTML Scan), Scan URL (Fast HTML Scan), Scan URL (Full without HTML Scan) and Scan URL (Fast without HTML Scan). 

![image](https://user-images.githubusercontent.com/71886838/161992736-bae97807-276f-43f6-a609-a7d3105c4761.png)

Figure 2

The user would then be prompted to enter the URL that they wish to scan as seen in Figure 3.

![image](https://user-images.githubusercontent.com/71886838/161992777-555b44ea-1091-46a6-b682-0dfd40b453e1.png)

Figure 3
 
Thereafter, users would be able to choose if they would wish to add a cookie string to the URL, stop at the first vulnerability found, and store the results into a JSON file as seen in Figure 4.

![image](https://user-images.githubusercontent.com/71886838/161992817-908a6c01-c24e-4ec9-b468-3284a71e7097.png)

Figure 4

Once the scan has been completed, users can view the vulnerability payload of the website that they have stated earlier in Figure. An example of a vulnerability would be as seen in Figure 5: 

![image](https://user-images.githubusercontent.com/71886838/161992852-ddfe756d-b532-4304-bce3-a649165666e4.png)

Figure 5

Once the result has been generated, users may wish to choose to export the results as a PDF. A snippet taken from the PDF output in Figure 6 shows the payload and the exact URL needed to launch the XSS attack.

![image](https://user-images.githubusercontent.com/71886838/161992889-04d7579a-164d-41fd-9790-dcbf1c174ec7.png) 

Figure 6


## DOM Scanner

**Insert desc here* *

## Fuzz Scanning

**Insert desc here* *

## Automatic XSS Attack

**Insert desc here* *

## Manual XSS Attack 


## License
[MIT](https://choosealicense.com/licenses/mit/)
