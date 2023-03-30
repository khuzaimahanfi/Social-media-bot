from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# import time
from time import sleep
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--enable-notifications")
# chrome_options.add_argument("--headless")
# driver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.google.com")
# driver = webdriver.Chrome(executable_path="C:\Users\DELL\Desktop\ALANFI-TESTCASES")
driver.implicitly_wait(10)
# URL of the visiting site
driver.get("https://www.linkedin.com/")
# AUTH Credentials
driver.find_element(By.XPATH, "//input[@id='session_key']").send_keys("hanfi.kh99@gmail.com")
driver.find_element(By.XPATH, "//input[@id='session_password']").send_keys("Hanfi12345kh")
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
sleep(10)
# POST CREATION
# driver.find_element(By.ID, "ember323").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Start a post']").click()
sleep(5)
driver.find_element(By.XPATH, "//div[@aria-label='Text editor for creating content']").send_keys("xyz testing")
driver.find_element(By.XPATH, "//li-icon[@type='image']//*[name()='svg']//*[name()='path' and contains(@d,'M19 4H5a3 ')]").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Done']").send_keys("C:/Users/hp/OneDrive/Pictures/Screenshots")
driver.find_element(By.XPATH, "//span[normalize-space()='Done']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Post']").click()
