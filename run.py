from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://sas.selleramp.com/site/login")

assert 'Login' in driver.title
actions = ActionChains(driver)

elem = driver.find_element(By.ID, 'loginform-email') 
actions.send_keys_to_element(elem, '').perform()
elem = driver.find_element(By.ID, 'loginform-password')
actions.send_keys_to_element(elem, '').perform()
elem = driver.find_element(By.NAME, 'login-button')
actions.move_to_element(elem).click(elem).perform()
print(driver.title)


# start selinum driver
# xvfb-run java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone.jar  -debug 
# headless start
# chromedriver --url-base=/wd/ hub
