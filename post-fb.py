from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--headless")
# driver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.google.com")
# driver = webdriver.Chrome(executable_path="C:\Users\DELL\Desktop\ALANFI-TESTCASES")
driver.implicitly_wait(10)
# URL of the visiting site
driver.get("https://www.facebook.com/")
# AUTH Credentials
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("khuzaimaqa-1@yopmail.com")
driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("987654321@aA")
sleep(2)
# alert = driver.switch_to_alert()
# alert.dismiss()

driver.find_element(By.XPATH, "(//button[normalize-space()='Log in'])[1]").click()
sleep(10)
# Switch to the alert dialog box
# driver.execute_script("window.Notification.requestPermission().then(function(permission) {console.log(permission)})")

driver.find_element(By.XPATH, "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']").click()
driver.find_element(By.XPATH, "(//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8'])[1]").send_keys("sdda")
sleep(10)
driver.find_element(By.XPATH, "//div[@aria-label='Photo/video']//div//div//img[@class='x1b0d499 xl1xv1r']").click()
sleep(5)
# driver.find_element(By.XPATH, '//form[contains(@method, "POST")]//input[contains(@accept, "video")]').send_keys('C:/Users/hp/OneDrive/Pictures/Screenshots/Screenshot (1).jpg')
# file_path = 'C:/Users/hp/OneDrive/Pictures/Screenshots/Screenshot (1).jpg'

sleep(20)
# upload = driver.find_element(By.XPATH, "//*[contains(text(), 'Add photos/videos')]")
# driver.find_element(By.XPATH, "(//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8'])[1]").send_keys("C:/Users/hp/OneDrive/Pictures/Screenshots/Screenshot (1).jpg")
# upload.send_keys("C:/Users/hp/OneDrive/Pictures/Screenshots/Screenshot (1).jpg")

# .send_keys('C:/Users/hp/OneDrive/Pictures/Screenshots/Screenshot (1).jpg')
# driver.find_element(By.XPATH, "(//div[@class='x6s0dn4 x78zum5 x5yr21d xl56j7k x1n2onr6 xh8yej3'])[2]").send_keys('C:/Users/hp/OneDrive/Pictures/Screenshots/Screenshot (1).jpg')

# Locate the file input element on the page
# file_input = driver.find_element(By.XPATH, "//div[@aria-label='Photo/video']//div//div//img[@class='x1b0d499 xl1xv1r']")
sleep(15)
# Set the local file path of the photo to be uploaded
# photo_path = 'C:/Users/hp/OneDrive/Pictures/Screenshots/Screenshot (1).jpg'
# file_input.send_keys(photo_path)
driver.find_element(By.XPATH, "//*[contains(text(), 'Post')]").click()
sleep(5)

