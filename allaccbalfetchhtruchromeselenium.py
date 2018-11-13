import os
import re
import time
import datetime
#fl= open('../output/sbibalances.txt','w')
credentials=('sbiusername1','sbipassword1','SBI','sbiusername2','sbipassword2','SBI','sbiusername3','sbipassword3','SBI','iciciusername1','icicipassword1','ICI');

#credentials=('username1','password1','username2','password2','usernameUPtoNth','passwordUPtoNth'); #username and password till N users
N=int(0.334*len(credentials))
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

'''
#For invisible chrome
options = webdriver.ChromeOptions()
options.add_argument("headless")
chrm = webdriver.Chrome(chrome_options=options)
#Above three lines can be commented if you need to see the visible chrome
'''
chrm = webdriver.Chrome()
#This is for visible chrome
chrm.implicitly_wait(10)
chrm.maximize_window()
currentDT = datetime.datetime.now()

def balfetchsbi(i):
    username=credentials[i*3]
    paswrd=credentials[(i*3)+1]
    chrm.get("https://retail.onlinesbi.com/retail/login.htm")
    chrm.find_element_by_xpath("//div[@class='continue_btn']").click()
    chrm.find_element_by_name("userName").send_keys(username) #myusername
    chrm.find_element_by_name("password").send_keys(paswrd) #mypassword
    chrm.find_element_by_id("Button2").click()
    chrm.implicitly_wait(1)
    chrm.find_element_by_xpath("//a[contains(@href,'getAccBalCSS')]").click()
    chrm.implicitly_wait(1)
    a=(chrm.find_element_by_xpath("//a[contains(@href,'getAccBalCSS')]").get_attribute("innerHTML"))
    ab=((a[10:16])+'Res'+(a[16:33]))
    time.sleep(1)
    chrm.implicitly_wait(1)
    chrm.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    chrm.implicitly_wait(1)
    print ('Balance in',a[22:33],' is',chrm.find_element_by_xpath("//span[contains(@id,'"+ab+"')]").get_attribute("innerHTML"))
    print('\n','Balance in account',a[22:33],' is',chrm.find_element_by_xpath("//span[contains(@id,'"+ab+"')]").get_attribute("innerHTML"), file=f)
    chrm.get("https://retail.onlinesbi.com/retail/logout.htm")

def balfetchici(i):
    usernamei=credentials[i*3]
    paswrdi=credentials[(i*3)+1]
    chrm.get("https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=ICI&_ga=2.249687814.1221146693.1525521426-2024232703.1424878671")
    chrm.implicitly_wait(1)
    chrm.find_element_by_name("AuthenticationFG.USER_PRINCIPAL").send_keys(usernamei) #myusername
    chrm.find_element_by_name("AuthenticationFG.ACCESS_CODE").send_keys(paswrdi) #mypassword
    chrm.find_element_by_name("Action.VALIDATE_CREDENTIALS").click()
    chrm.implicitly_wait(1)
    chrm.find_element_by_id("MY_ACCOUNTS").click()
    chrm.find_element_by_id("Bank-Accounts").click()
    iciacc=(chrm.find_element_by_id("HREF_actNoOutput[0]").get_attribute("innerHTML"))
    icibal=(chrm.find_element_by_id("HREF_actBalOutput[0]").get_attribute("innerHTML"))
    print('Balance in',iciacc,'is INR ',icibal)
    print('\n','Balance in account',iciacc,'is INR ',icibal, file=f)
    chrm.find_element_by_id("HREF_Logout").click()
    time.sleep(1)
##
f = open('balances.txt','a')
print ('\n','YYYY-MM-DD HH:MM:SS',currentDT.strftime("%Y-%m-%d %H:%M:%S"), file=f)
##
for i in range(N):
    if credentials[(i*3)+2] is 'SBI':
        balfetchsbi(i)
    else:
        balfetchici(i)
quit
time.sleep(1)

chrm.quit()


#chrm.find_element_by_xpath("//div[text()='Dashboard']").click()
#chrm.find_element_by_xpath("/html[1]/body[1]/form[1]/div[3]/div[1]/div[1]/p[6]/span[2]/span[1]/span[1]/div[1]/div[2]/ul[1]/li[3]").click()
