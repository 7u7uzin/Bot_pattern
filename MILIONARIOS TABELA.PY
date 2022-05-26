import time
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import requests

browser = webdriver.Chrome()

browser.get("https://milionariotips.com.br/Home/Horarios")

time.sleep(15)

#login
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("Password")

username.send_keys("luan0910")
password.send_keys("123456789")

time.sleep(5)

submit = browser.find_element_by_id('submit-login')
submit.click()

time.sleep(5)
#teste se o captcha foi concluido


# salvando a tabela =============================================================================
# schedule = open("bot\\BOT\\tabela.txt", "a")
content = browser.find_element_by_xpath("/html/body/div[3]/section/div/div[2]/table/tbody")
# schedule.write(content)
# schedule.close()
# ===============================================================================================

# browser.close()

#conferindo resultados===========================================================================

if "1x1" in content.text:
  print("true")

