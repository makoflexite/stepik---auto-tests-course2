from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)

    field1 = browser.find_element_by_css_selector("label>span:nth-child(2)")
    x = field1.text
    y = calc(x)

    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)

    button = browser.find_element_by_class_name("btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

