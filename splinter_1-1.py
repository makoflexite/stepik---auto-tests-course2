from splinter import Browser
from selenium import webdriver
import time

browser = Browser() # defaults to firefox
browser.visit('http://suninjuly.github.io/wait2.html')
browser.find_by_id("verify").click()


#browser.fill('q', 'splinter - python acceptance testing for web applications')
#browser.find_by_name('btnK').click()

if browser.is_element_present_by_id('verify_message'):
    print("Yes, the official website was found!")
else:
    print("No, it wasn't found... We need to improve our SEO techniques")

browser.quit()
