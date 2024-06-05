from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# browser setting
options = Options()
options.add_experimental_option("detach", True)

# webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# authentication page in google
driver.get("https://accounts.google.com/signin")

# email
email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'identifier')))
email_input.send_keys('your email')
email_input.send_keys(Keys.RETURN)

# password
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
password_input.send_keys('your password')
password_input.send_keys(Keys.RETURN)

# 2FA if it on
try:
    code_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, 'totpPin'))
    )
    auth_code = input("Input 2FA password: ")
    code_input.send_keys(auth_code)
    code_input.send_keys(Keys.RETURN)
except:
    pass  # if it off
