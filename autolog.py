from selenium import webdriver
from getpass import getpass
from selenium.webdriver import ChromeOptions, Chrome
import time
opts = ChromeOptions()
opts.add_experimental_option("detach", True)



username = input("Enter in your username: ")
password = getpass("Enter your password: ")

driver = webdriver.Chrome("C:/Users/Lenewvaa/Downloads/chromedriver.exe")
driver.get("https://github.com/login")

username_textbox = driver.find_element_by_id("login_field")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]")
login_button.submit()

time.sleep(400000)
