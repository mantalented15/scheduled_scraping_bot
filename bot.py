from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
# import requests

# chrome_options= Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("--disable-blink-features")
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")

LOGIN_PAGE="https://partner.outsourceaccelerator.com/login"
ACCOUNT="partner.wingassistant@outsourceaccelerator.com"
PASSWORD="Os@!!hgrj3138"

# driver=webdriver.Chrome('chromedriver', chrome_options=chrome_options)
driver=webdriver.Chrome('chromedriver')

wait=WebDriverWait(driver, 30)
driver.get(LOGIN_PAGE)
wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys(ACCOUNT)
wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(PASSWORD)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))).click()

time.sleep(30)
# a = driver.find_elements_by_xpath('//li[@data-testid="list-item-8"]//div[@class="ant-space-item"]')
# a = driver.find_elements_by_xpath('//li[@data-testid="list-item-8"]')
# a = driver.find_element(By.XPATH, '//div[@class="ant-space-item"]/a')
# a = driver.find_element(By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')

# WebDriverWait(driver,240).until(EC.element_to_be_clickable((By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')))
# a = driver.find_element(By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')
# try:
    # a = WebDriverWait(driver,180).until(EC.presence_of_element_located((By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')))
    # a = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')))
    
    # a = WebDriverWait(driver,180).until(EC.presence_of_all_elements_located((By.XPATH, '//ul[@data-testid="list-items"]//a')))

    # href = a.get_attribute('href')
    # a = WebDriverWait(driver,180).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="ant-space-item"]/a')))
    # ul = WebDriverWait(driver,240).until(EC.presence_of_all_elements_located((By.XPATH, '//ul[@class="ant-list-items"]')))
    # a = ul.find_elements_by_xpath('//a')
# except:
#     print("Timed out waiting for page to load")

# for a_i in a:
#     print(a_i)

# # a_list = []
# for i in range(len(a)):
#     print(a[i].get_Attribute('href'))

# print(a.text)
# print(a.get_attribute("href"))
# print(a_list)
# print(requests.get(href).text)
