from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get('http://uitestingplayground.com/textinput')
control = browser.find_element(By.CLASS_NAME, 'form-control')
control.send_keys("SkyPro")

button = browser.find_element(By.CLASS_NAME, 'btn-primary')

button.click()
usd = browser.find_element(By.CLASS_NAME, 'form-control')
txt = usd.text 

print(txt)




browser.quit()

