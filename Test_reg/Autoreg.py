from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://shop.synctoskill.com")
driver.maximize_window()
driver.find_elements("xpath", "//a[@class='nav-link text-dark']")[1].click()
driver.find_element("xpath", "//input[@name='FullName']").send_keys("Mike")
driver.find_element("xpath", "//input[@name='Email']").send_keys("jgokdb@mail.com")
driver.find_element("xpath", "//input[@name='Password']").send_keys("Qwerty12345")
driver.find_element("xpath", "//input[@name='PasswordConfirmation']").send_keys("Qwerty12345")
driver.find_element("xpath", "//input[@name='Phone']").send_keys("1(111)111-11-11")
driver.find_element("xpath", "//input[@name='Address']").send_keys("Moscow")
driver.find_element("xpath", "//input[@name='BirthDate']").send_keys("12.12.2012")
driver.find_element("xpath", "//input[@value='Sign Up']").click()
time.sleep(10)