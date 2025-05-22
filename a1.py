from selenium import webdriver
import time
driver = webdriver.Edge()

driver.get("https://qums.quantumuniversity.edu.in/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("id","UserName").send_keys(" 22120086")     #Enter your Qid
driver.find_element("xpath",'//input[@type="password"]').send_keys("Your Password")        #Enter your password
time.sleep(10)
driver.find_element("xpath",'//input[@placeholder="Enter Captcha"]').click()
time.sleep(10)
driver.find_element("xpath",'//button[@type="submit"]').click()
driver.find_element("xpath",'//a[@id="lnkDashboard"]/img[@title="Dashboard"]').click()
#
time.sleep(5)
element = driver.find_element("xpath",'//button[@id="btnAttendanceToday"]')
element.click()
driver.execute_script("arguments[0].scrollIntoView();", element)

time.sleep(100)