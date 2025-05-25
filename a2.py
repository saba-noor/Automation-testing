from selenium import webdriver
import time

driver = webdriver.Chrome()


#Nevigate to google - open URL

driver.get("https://www.google.com")
time.sleep(2)

#Nevigate to youtube - open URL

driver.get("https://www.youtube.com")
time.sleep(2)

#Go Back to google
driver.back()

#Go forward to youtube
driver.forward()

#refresh the current page
driver.refresh()
#close the browser windows
driver.quit()
