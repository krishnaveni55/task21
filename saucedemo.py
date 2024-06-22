import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
paths = r"C:\Users\HP\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.saucedemo.com/")
time.sleep(3)
print("Cookies before login:")
cookies_before_login = driver.get_cookies()
for cookie in cookies_before_login:
    print(cookie)
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()
time.sleep(3)
print("\nCookies after login:")
cookies_after_login = driver.get_cookies()
for cookie in cookies_after_login:
    print(cookie)
menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
menu_button.click()
time.sleep(2)
logout_link = driver.find_element(By.ID, "logout_sidebar_link")
logout_link.click()
time.sleep(3)
print("\nCookies after logout:")
cookies_after_logout = driver.get_cookies()
for cookie in cookies_after_logout:
    print(cookie)
time.sleep(3)
driver.quit()