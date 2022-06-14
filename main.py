from selenium import webdriver
from selenium.webdriver.common.by import By
import info
import time
from tkinter import *

window = Tk()
window.title("Instagram bot")
window.minsize(300, 100)
window.maxsize(300, 100)

def start():
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/")
    login(driver)
    

def login(driver):
    # Allow essential and optional cookies
    btn_cookie = driver.find_element(By.XPATH, "// button[contains(text(),'Allow essential and optional cookies')]")
    if btn_cookie:
        btn_cookie.click()
        time.sleep(10)
    username = info.username
    password = info.password
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(username)
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)
    btn_login = driver.find_element(By.XPATH, "// div[contains(text(),'Log In')]")
    btn_login.click()
    time.sleep(10)
    print(".........................................")
    btn_not_now = driver.find_element(By.XPATH, "// button[contains(text(),'Not Now')]")
    if btn_not_now:
        btn_not_now.click()
    # time.sleep(10)
    # print("notification")
    # btn_notification = driver.find_element(By.XPATH, "// button[contains(text(),'Not Now')]")
    # if btn_notification:
    #     btn_notification.click()
    link = input_link.get()
    driver.get(link)
    time.sleep(10)
    like_post(driver)


def like_post(driver):
    btn_like = driver.find_element(By.CSS_SELECTOR, "span._aamw")
    btn_like.click()


lbl_link = Label(window, text="Link", width=15)
lbl_link.grid(row=0, column=0)

input_link = Entry(window)
input_link.grid(row=0, column=1)


btn_start = Button(window, text="START", command=start)
btn_start.grid(row=1)

window.mainloop()