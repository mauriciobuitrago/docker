from selenium import webdriver
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
all_cookies = driver.get_cookies()
print(all_cookies)