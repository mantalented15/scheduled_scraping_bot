from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import config

def get_leads_data():
    options= Options()
    # options.add_argument("--headless")
    # options.add_argument("start-maximized")
    # options.add_argument("--disable-blink-features")
    # options.add_argument("--disable-blink-features=AutomationControlled")

    driver=webdriver.Chrome('chromedriver', options=options)
    # driver=webdriver.Chrome('chromedriver')

    # options.binary_location=r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
    # driver=webdriver.Firefox(executable_path="geckodriver", options=options)

    driver.maximize_window()

    wait=WebDriverWait(driver, 30)

    #Login with account and password
    driver.get(config.login_page)
    wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys(config.account)
    wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(config.password)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Log in"]'))).click()

    #Load the leader page
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Inbound inquiries"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/partner/leads"]'))).click()

    #get the number of leads per page
    number_per_page = int(wait.until(EC.visibility_of_element_located((By.XPATH, '//select//option[@selected]'))).get_attribute("value"))

    # get the number of total leads and the number of leads of last page
    caption_leads_number = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'of')]"))).text
    leads_number = int(caption_leads_number[caption_leads_number.find('of')+2:])
    leads_number_last_page = leads_number % number_per_page

    # calcuate the number of pages
    pages_number = int(leads_number/number_per_page) + 1

    #calculate the scroll step
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    # scroll_step = int(scroll_height/(number_per_page))
    scroll_step = 100

    #click the view buttons of leads and get the data into dataframe
    df_lead_data=pd.DataFrame()

    for page_index in range(pages_number):
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)

        if page_index == pages_number-1:
            number_in_page = leads_number_last_page
        else:
            number_in_page = number_per_page

        for lead_index in range(number_in_page):
            print(lead_index)
            if lead_index > 0:
                driver.execute_script("window.scrollTo(0, arguments[0]);", scroll_step*lead_index)
                time.sleep(0.5)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='row-{}' and @role='row']//button".format(lead_index)))).click()

            #get the data under lead
            divs = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'dl > div')))

            columns=['Lead score', 'Email address', 'Phone number', 'Timezone', 'Country', 'Device', 'Sector', 'Company size', 'Role to outsource', 'Number of staff to oursource', 'Key question', 'Comment', 'Data added']
            dict_lead_data={}
            for index in range(len(divs)):
                dict_lead_data[columns[index]]=divs[index].find_element(By.TAG_NAME, 'dd').text

            #append data dictionary into panda dataframe
            df_lead_data = pd.concat([df_lead_data, pd.DataFrame([dict_lead_data])], ignore_index=True)

            #Cancel the view
            wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()

        #go over the next page
        if page_index!=pages_number-1:  # go over next page if not last page
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Next Page']"))).click()
            time.sleep(3)

    print(df_lead_data)
    df_lead_data.to_csv('leads_data.csv', index=False)

def main():
    get_leads_data()

if __name__ == "__main__":
    main()
