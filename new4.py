from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

# Prompt user for input
post_option = input("Do you want to post on your own timeline or in group link list? Type 'timeline' or 'grouplist': ")

# Load Facebook homepage
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://www.facebook.com/")

# Login
email_input = input("Enter your email:")
password_input = input("Enter your password:")
driver.find_element(By.ID, "email").send_keys(email_input)
driver.find_element(By.ID, "pass").send_keys(password_input)

login_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Log in'])[1]")
login_button.click()

time.sleep(20)
if post_option == "timeline":
    # Post on your own timeline
    # post_text = input("What do you want to post on your timeline? ")
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div").click()
    time.sleep(10)
    post_input = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
    post_text = input("What do you want to post on your timeline? ")
    post_input.send_keys(post_text)
    # post_input.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.find_element(By.XPATH, "(//img[@class='x1b0d499 xl1xv1r'])[1]").click()
    time.sleep(10)
    # st_image.click()
    driver.find_element(By.XPATH, "(//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x1iyjqo2 x2lwn1j xl56j7k'])[1]").click()

    # driver.find_element(By.XPATH, "//div[@aria-label='Photo/video']//div//div//div[@class='x4k7w5x x1h91t0o x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1jfb8zj x1beo9mf x3igimt xarpa2k x1n2onr6 x1qrby5j']").click()
    time.sleep(25)

    # driver.find_element(By.XPATH, "//*[contains(text(), 'Add photos/videosor drag and drop')]").send_keys("D:/PycharmProjects/Social-media-bot/uri.jpg")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//div[@aria-label='Photo/video']//div//div//div[@class='x4k7w5x x1h91t0o x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1jfb8zj x1beo9mf x3igimt xarpa2k x1n2onr6 x1qrby5j']").send_keys("D:/PycharmProjects/Social-media-bot/uri.jpg")

    # time.sleep(5)
    post_publish_btn = driver.find_element(By.XPATH, "(//div[@class='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67'])[2]")
    post_publish_btn.click()

    time.sleep(5)
    print("Post successful!")

elif post_option == "grouplist":
    # Load group links from CSV file
    df = pd.read_csv('groups-link.csv')
    groups_links_list = df['links'].tolist()

    # Loop through group links and post
    post_text = input("What do you want to post in the groups? ")
    for group_link in groups_links_list:
        driver.get(group_link)
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        post_button = driver.find_element(By.XPATH, "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']")
        post_button.click()
        time.sleep(5)
        post_input = driver.find_element(By.XPATH, "(//div[@class='_1mf _1mj'])[1]")
        post_input.send_keys(post_text)
        time.sleep(2)
        post_input.send_keys(Keys.RETURN)
        time.sleep(5)
        postbutton = driver.find_element(By.XPATH, "//div[@aria-label='Post']//div[@class='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67']")
        time.sleep(10)
        postbutton.click()
        time.sleep(20)
    print("Posts successful!")

else:
    print("Invalid input. Please type 'timeline' or 'grouplist'.")
