# Create a chrome instance
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# # With Absolute Driver Path
service = Service("C:\\Users\\Sures\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

# # With Relative Driver Path
service_2 = Service("../Drivers/chromedriver.exe")

# # serviceManager
service_3 = Service()
driver = webdriver.Chrome(service=service)


firefox_service = Service()
driver = webdriver.Firefox(service=firefox_service)

driver.get("https://www.google.co.in")
