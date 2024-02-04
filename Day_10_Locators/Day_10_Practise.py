import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
driver = webdriver.Chrome(service=service)

# Maximize the Window
# driver.maximize_window()

# Navigate to URL
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Input Name
driver.find_element(By.NAME, 'name').send_keys("Suresh Reddy")

# Input Email
driver.find_element(By.NAME, 'email').send_keys("bagisuresh411@gmail.com")

# Input Password
driver.find_element(By.ID,'exampleInputPassword1').send_keys("Sujana@411")

# Click Checkbox
driver.find_element(By.ID, 'exampleCheck1').click()

# Select Radio button
driver.find_element(By.ID, "inlineRadio1").click()

time.sleep(2)

# Select Radio button by CSS
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()

time.sleep(2)

driver.find_element(By.XPATH,'//input[@type="submit"]').click()

success_text = driver.find_element(By.CLASS_NAME,"alert-success").text

if "Success" in success_text:
    print("Form has been successfully submitted")
else:
    print("Form submission failed")
# Wait for 5 sec
time.sleep(2)

# Close the Driver
driver.close()
