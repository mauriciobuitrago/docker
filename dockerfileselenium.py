from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time       
    
capabilities = {
    "browserName": "chrome",
    "browserVersion": "89.0",
    "selenoid:options": {
        "enableVNC": True
    }
}

driver = webdriver.Remote(
    command_executor="http://selenoid:4444/wd/hub",
    desired_capabilities=capabilities)

driver.get("https://www.google.com")
time.sleep(5)
search_bar = driver.find_element(By.NAME, "q")
time.sleep(5)
search_bar.send_keys("Wikipedia")
time.sleep(5)
search_bar.send_keys(Keys.ENTER)
all_cookies = driver.get_cookies()
print(all_cookies)


driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a").click()
