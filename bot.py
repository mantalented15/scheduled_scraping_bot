from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd


def get_leads_data():
    options= Options()
    # options.add_argument("--headless")
    # options.add_argument("start-maximized")
    # options.add_argument("--disable-blink-features")
    # options.add_argument("--disable-blink-features=AutomationControlled")

    LOGIN_PAGE="https://partner.outsourceaccelerator.com/login"
    ACCOUNT="partner.wingassistant@outsourceaccelerator.com"
    PASSWORD="Os@!!hgrj3138"

    driver=webdriver.Chrome('chromedriver', options=options)
    # driver=webdriver.Chrome('chromedriver')

    # options.binary_location=r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
    # driver=webdriver.Firefox(executable_path="geckodriver", options=options)

    driver.maximize_window()

    wait=WebDriverWait(driver, 30)

    #Login with account and password
    driver.get(LOGIN_PAGE)
    wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys(ACCOUNT)
    wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(PASSWORD)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Log in"]'))).click()

    #Load the leader page
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Inbound inquiries"]'))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/partner/leads"]'))).click()


    #click the view0
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="row-0" and @role="row"]//button'))).click()

    #get the data under lead
    divs = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'dl > div')))

    columns=['Lead score', 'Email address', 'Phone number', 'Timezone', 'Country', 'Device', 'Sector', 'Company size', 'Role to outsource', 'Number of staff to oursource', 'Key question', 'Comment', 'Data added']
    dict_lead_data={}
    leads_data=[]
    for index in range(len(divs)):
        dict_lead_data[columns[index]]=divs[index].find_element(By.TAG_NAME, 'dd').text
    leads_data.append(dict_lead_data)

    #convert leads_data into panda dataframe
    df_lead_data=pd.DataFrame(leads_data)

    # print(df_lead_data)

    time.sleep(3)
    #Cancel the view
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()


    #view1
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="row-1" and @role="row"]//button'))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()

    #test lead
            # last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, 150);")
    time.sleep(5)
    # element = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="row-2" and @role="row"]//button')))
    element=driver.find_element(By.XPATH, "//div[@id='row-2' and @role='row']//button")
    print(element)
    action=ActionChains(driver)
    action.move_to_element(element).perform()
    time.sleep(1)
    element.click()
 
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()


    #test lead
            # last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, 150);")
    time.sleep(5)
    # element = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="row-2" and @role="row"]//button')))
    element=driver.find_element(By.XPATH, "//div[@id='row-2' and @role='row']//button")
    print(element)
    action=ActionChains(driver)
    action.move_to_element(element).perform()
    time.sleep(1)
    element.click()
 
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()

    #test lead
            # last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, 200);")
    time.sleep(5)
    # element = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="row-2" and @role="row"]//button')))
    element=driver.find_element(By.XPATH, "//div[@id='row-3' and @role='row']//button")
    print(element)
    action=ActionChains(driver)
    action.move_to_element(element).perform()
    time.sleep(1)
    element.click()
 
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()

    #test lead
            # last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, 400);")
    time.sleep(5)
    # element = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="row-2" and @role="row"]//button')))
    element=driver.find_element(By.XPATH, "//div[@id='row-4' and @role='row']//button")
    print(element)
    action=ActionChains(driver)
    action.move_to_element(element).perform()
    time.sleep(1)
    element.click()
 
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()



    time.sleep(30)


def main():
    get_leads_data()

if __name__ == "__main__":
    main()
