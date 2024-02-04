# Using methods as Title, URL and close for selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Create webdriver instance
service = Service()
driver = webdriver.Chrome(service=service)

# Maximize the driver
driver.maximize_window()

# Navigate to rahulshetty academy page
driver.get("https://rahulshettyacademy.com/")

# Print title of the navigated page
print(f"Title of the page is :: {driver.title}")

# Print the url of the navigated page
print(f"Current URL of the page is :: {driver.current_url}")

# Go to Other URL
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Print the details
print(f"Title of the page is :: {driver.title}")
print(f"Current URL of the page is :: {driver.current_url}")

# Go backward
driver.back()

# Print the details
print(f"Title of the page is :: {driver.title}")
print(f"Current URL of the page is :: {driver.current_url}")

# Go Forward
driver.forward()

# Print the details
print(f"Title of the page is :: {driver.title}")
print(f"Current URL of the page is :: {driver.current_url}")

# Refresh the page
driver.refresh()

# Close the driver
driver.close()
