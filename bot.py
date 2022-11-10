from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
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

    # view_buttons = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="row"]//button[text()="View"]')))

    # for index in range(len(view_buttons)):
    #     # print(index)
    #     wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="row-%d"]//button[text()="View"]'%index))).click()
    #     # wait.until(EC.element_located_to_be_selected((By.XPATH, '//div[@id="row-%d"]//button[text()="View"]'%index))).click()

    #     # view.click()
    #     wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()

    #javascript execution for zoom in to fix unexpected errors
    # script= "document.body.style.zoom='30%'"
    # driver.execute_script(script)
    # time.sleep(3)
    # time.sleep(8)
    # element=driver.find_element(By.XPATH, "//div[@id='row-4' and @role='row']//button")
    # driver.execute_script("arguments[0].scrollIntoView();", element)
    # element.location_once_scrolled_into_view
    # element.click()

    # element=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="row-4" and @role="row"]//button')))
    # print(element)
    # action=ActionChains(driver)
    # action.move_to_element(element).click().perform()

    # wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="row-0" and @role="row"]//button'))).click()



    # count=0
    # for view in view_buttons:
    #     count=count+1
    #     print(count)
    #     print(view)
    #     view.click()
    #     wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()
    #     time.sleep(3)
time.sleep(20)

#view the lead
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="row-0" and @role="row"]//button'))).click()

#get the data under lead
divs = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'dl > div')))

for div in divs:
    lead_score=div.find_element(By.TAG_NAME, 'dd').text
    print(lead_score)
# lead_score

time.sleep(20)
#Cancel the view
wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Close panel"]/ancestor::button'))).click()


time.sleep(30)

