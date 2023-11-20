# BROWSER AUTOMATION USING SELENIUM

'''
when you request using requests module, it doesn't run the javascript code
it has to be run on a browser or another javascript engine
'''

'''
if there were javascript code the page woudn't work as expected,
chrome fixes that but gives a slower-running programme
'''

'''
cannot use requests module to interact with drop down inside the page
we would be able to see that there is a drop down but won't be able to click 
on it and make a change
'''

# WAITS - when javascript code takes longer to run tahn our code

# Explicit waits
import time
time.sleep(5)
 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

WebDriverWait(browser, 10).until(
    expected_conditions.presence_of_all_elements_located(
        (By.CSS_SELECTOR, QuotesPageLocators.TAG_DROPDOWN_VALUE_OPTION)
    )
)

# Implicit waits
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10)
