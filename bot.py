from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options= Options()
# options.add_argument("--headless")
options.add_argument("start-maximized")
# options.add_argument("--disable-blink-features")
# options.add_argument("--disable-blink-features=AutomationControlled")

LOGIN_PAGE="https://partner.outsourceaccelerator.com/login"
ACCOUNT="partner.wingassistant@outsourceaccelerator.com"
PASSWORD="Os@!!hgrj3138"
LEAD_PAGE="https://partner.outsourceaccelerator.com/partner/leads"

driver=webdriver.Chrome('chromedriver', options=options)
# driver=webdriver.Chrome('chromedriver')

wait=WebDriverWait(driver, 30)

#Login with account and password
driver.get(LOGIN_PAGE)
wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys(ACCOUNT)
wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(PASSWORD)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Log in"]'))).click()

#Load the leader page
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Inbound inquiries"]'))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/partner/leads"]'))).click()

#loop for each lead and view

#Click view button for each lead
# wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="row-0"]//button[text()="View"]'))).click()
view_buttons = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="row"]//button[text()="View"]')))
# for index in range(len(view_buttons)):
#     # print(index)
#     wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="row-%d"]//button[text()="View"]'%index))).click()
#     # wait.until(EC.element_located_to_be_selected((By.XPATH, '//div[@id="row-%d"]//button[text()="View"]'%index))).click()
    
#     # view.click()
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()
    
count=0
for view in view_buttons:
    count=count+1
    print(count)
    view.click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()


#Cancel the view
# wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()


time.sleep(30)

