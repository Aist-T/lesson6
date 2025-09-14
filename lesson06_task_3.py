from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

try:
    
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

   
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Done")
    )

    
    images = browser.find_elements(By.TAG_NAME, "img")
    assert len(images) == 4, f"Загружено только {len(images)} картинок"
    third_image_src = images[2].get_attribute("src")

finally:
    
    browser.quit()

