import by as By
import driver as driver
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://www.facebook.com")
driver.maximize_window()
sleep(5)

# accept cookies
# cookies = WebDriverWait(driver, 30).until(EC.element_to_be_clickable())

driver.find_element(By.XPATH, "//input[@id='email']").send_keys("khuzaimaqa-1@yopmail.com")
driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("987654321@aA")
sleep(1)
driver.find_element(By.XPATH, "(//button[normalize-space()='Log in'])[1]").click()
sleep(5)

groups_links_list = ["https://www.facebook.com/groups/965236094073316/", "https://www.facebook.com/groups/172477266511488/", "https://www.facebook.com/groups/freepromoads"
                     ]
for group in groups_links_list:
    driver.get(group)
    chrome_options.add_argument("__disable-notifications")
    sleep(5)
    driver.execute_script("window.scrollTo(0, 200)")
    postbox = driver.find_element(By.XPATH, "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']")
    postbox.click()
    sleep(5)

    element = driver.find_element(By.XPATH, "//div[@class='_1mf _1mj']")
    element.send_keys("this is hey message")
    sleep(2)

    postbutton = driver.find_element(By.XPATH, "//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft'][normalize-space()='Post']")
    sleep(3)
    postbutton.click()
    sleep(10)
    wait = WebDriverWait(driver, 10)
    # new_url = wait.until(EC.url_changes(driver.current_url))

# driver.find_element(By.XPATH, "(//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8'])[1]").send_keys("sdda")
# sleep(10)
# driver.find_element(By.XPATH, "//div[@aria-label='Photo/video']//div//div//img[@class='x1b0d499 xl1xv1r']").click()
driver.implicitly_wait(30)
sleep(20)
driver.quit()
