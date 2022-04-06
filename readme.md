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

 <ins>Figure 1</ins>

Users can proceed to click Scan; the following output will be shown in the command line as seen in Figure 2.  There are five options to choose from: Scan URL (Full HTML Scan), Scan URL (Fast HTML Scan), Scan URL (Full without HTML Scan) and Scan URL (Fast without HTML Scan). 

![image](https://user-images.githubusercontent.com/71886838/161992736-bae97807-276f-43f6-a609-a7d3105c4761.png)

<ins>Figure 2</ins>

The user would then be prompted to enter the URL that they wish to scan as seen in Figure 3.

![image](https://user-images.githubusercontent.com/71886838/161992777-555b44ea-1091-46a6-b682-0dfd40b453e1.png)

<ins>Figure 3</ins>
 
Thereafter, users would be able to choose if they would wish to add a cookie string to the URL, stop at the first vulnerability found, and store the results into a JSON file as seen in Figure 4.

![image](https://user-images.githubusercontent.com/71886838/161992817-908a6c01-c24e-4ec9-b468-3284a71e7097.png)

<ins>Figure 4</ins>

Once the scan has been completed, users can view the vulnerability payload of the website that they have stated earlier in Figure. An example of a vulnerability would be as seen in Figure 5: 

![image](https://user-images.githubusercontent.com/71886838/161992852-ddfe756d-b532-4304-bce3-a649165666e4.png)

<ins>Figure 5</ins>

Once the result has been generated, users may wish to choose to export the results as a PDF. A snippet taken from the PDF output in Figure 6 shows the payload and the exact URL needed to launch the XSS attack.

![image](https://user-images.githubusercontent.com/71886838/161992889-04d7579a-164d-41fd-9790-dcbf1c174ec7.png) 

<ins>Figure 6</ins>

## Fuzz Scanning

To run this feature, users will be greeted with the Fuzz Scanning tab after running main.py as seen in Figure 7. 

![image](https://user-images.githubusercontent.com/71886838/161993320-eeb3dbf5-2800-4e5f-9bb2-e1d048de08dc.png)
 
<ins>Figure 7</ins>

Users will then input a domain name, for example, we will be using singaporetech.edu.sg to generate our fuzzed URLs. After clicking on start fuzzing, this would be the output of the scan. 

![image](https://user-images.githubusercontent.com/71886838/161993358-ee9a652c-1ea4-4ad1-9214-a6f678e08f12.png)
 
<ins>Figure 8</ins>

Upon the generation of the fuzzed URLs, users may choose to export the results as a PDF file. A snippet of the PDF output can be seen in Figure 9. 

![image](https://user-images.githubusercontent.com/71886838/161993384-3b7d8140-4891-4707-a3d7-b2eb2794a1de.png)

![image](https://user-images.githubusercontent.com/71886838/161993404-70558745-1d65-4c85-9e18-9e1633af3e75.png)

<ins>Figure 9</ins>

These outputs can then be used alongside the Manual XSS Attack tab to concurrently inject payloads and be able to try to get an XSS URL attack to potentially work.

## DOM Scanner

For this DOM scanning feature, users can scan for DOM-based vulnerabilities on a website. Users are greeted with the DOM Scan tab upon the execution of main.py file as seen in Figure 10. 

![image](https://user-images.githubusercontent.com/71886838/161993820-96d4c44d-0bac-42d0-93c1-489bd82fc967.png)

<ins>Figure 10</ins>

Users then can input the URL with the proper parameters. For example, I will be using the website https://sudo.co.il/xss/level0.php?=email. As seen in Figure 11, the scan function then outputs the payloads that are available for the user to choose in the DOM attack, it also shows the efficiency and confidence level of the payloads, and users would be able to gauge the chances of the payload to be working as intended. 

![image](https://user-images.githubusercontent.com/71886838/161993859-4baed219-bd86-4301-a6b3-b729de320abb.png)
 
<ins>Figure 11</ins>

Upon the generation of the DOM-based payloads, users may choose to export the results as a PDF file. A snippet of the PDF output can be seen in Figure 12. 

![image](https://user-images.githubusercontent.com/71886838/161993901-95228052-ecb8-420f-bd60-041129a3091e.png)

<ins>Figure 12</ins>

Users may choose to attack the URL using the specified payload that is generated. 

## Automatic XSS Attack

For this Automatic XSS Attack feature, users can scan for DOM-based vulnerabilities on a website. Users are greeted with the Automatic XSS tab upon the execution of main.py file as seen in Figure 13.

![image](https://user-images.githubusercontent.com/71886838/161994045-234fa819-8024-4f80-a8f4-56257f8f3be6.png)
 
<ins>Figure 13</ins>

Users can then input the URL that they wish to attack automatically and then click on Start Attack. As seen in Figure 14, it automatically launches the Chrome web browser and starts the attack. It will automatically launch multiple instances of the web browser to inject the code onto the URL.

![image](https://user-images.githubusercontent.com/71886838/161994076-8e86494f-6758-4830-9caa-a8c4aea11d41.png)
 
<ins>Figure 14</ins>


## Manual XSS Attack 

For Manual XXS Attacks feature, it provides users with 2 Attack Formats: Website Input Fields and URL. The steps needed to run the attack are as follows: Firstly, the user would enter the target website’s URL in the topmost field. Secondly, he/she would need to choose any of the three XSS Type checkboxes: Basic, Advanced, and Filter, in any combination according to their preference. Thirdly, is the choice of the XXS Payload user would like to perform. Thereafter, the chosen payloads will be displayed in the Craft XXS Payload section. Lastly, before the user could inspect and edit the text in the Craft XXS Payload section and click on the attack button, he/she would need to select the Attack Format: Website Input Fields or URL. Figure 15 shows the UI for Manual XXS Attacks.


![image](https://user-images.githubusercontent.com/71886838/161994181-c6140025-574d-4a33-b584-44c2efccb722.png)
 
<ins>Figure 15</ins>

After the attack button is pressed, Selenium would be triggered to automate the attack on the chrome browser, based on the attack format: Website Input Fields or URL, the result could be either shown in Figure 16 and Figure 17 one after another or only in Figure 17 respectively.

![image](https://user-images.githubusercontent.com/71886838/161994251-ef911702-e185-40c0-8451-624799797b27.png)

<ins>Figure 16</ins>
                        
![image](https://user-images.githubusercontent.com/71886838/161994290-35595a1b-6202-4879-b876-34f55934401f.png)

<ins>Figure 17</ins>
  
After executing the attack, the browser would close automatically after some time. Users would be able to monitor the logs to find out what has exactly happened during the attack. For example: after the executing the Website Input Fields attack, the HTML class of the button that has been clicked would be shown in the logs. Figure 18 shows the logging for URL Attack.

![image](https://user-images.githubusercontent.com/71886838/161994348-6325c6fc-e8c2-4b91-be23-3ecd4e7a8880.png)

<ins>Figure 18</ins>

## License
[MIT](https://choosealicense.com/licenses/mit/)
