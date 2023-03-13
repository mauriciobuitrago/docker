from selenium import webdriver
import time       
    
capabilities = {
    "browserName": "chrome",
    "browserVersion": "89.0",
    "selenoid:options": {
        "enableVideo": False
    }
}

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)

driver.get("https://www.w3schools.com/html/default.asp")
time.sleep(5)
all_cookies = driver.get_cookies()
print(all_cookies)