from selenium import webdriver

def openBrowser(browserType, driverPath):
    if browserType == 'chrome':
        return webdriver.Chrome(driverPath)
    elif browserType == 'firefox':
        return webdriver.Firefox(driverPath)

def navigateTo(driver, url, waitTime):
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(waitTime)
    
def killBrowser(driver):
    driver.quit()
    
def xstr(s):
    return '' if s is None else str(s)

def buttonId(s):
    return s.lower().replace(" ","-")