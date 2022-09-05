from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('useAutomationExtension', False)
print("Sample test case started")
s = Service(r"C:\Users\delwa\PycharmProjects\SeleniumTest\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("javatpoint")
time.sleep(3)
driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
time.sleep(3)

button = driver.find_element(By.CLASS_NAME, u"infoDismiss")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(button).click(button).perform()

driver.close()
print("sample test case successfully completed")
