from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_path = "C:\Users\BALL IS LIFE\Documents\IEDriverServer.exe"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("website.html")

button = driver.find_element(By.ID, "button1")
button.click()

input_field = driver.find_element(By.NAME, "email1")
input_field.send_keys("my email")

form = driver.find_element(By.ID, "form_id")
form.submit()
driver.quit()