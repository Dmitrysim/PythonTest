from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try : 
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    print(x)
    print(y)
    sum = int(x) + int(y)
    print(sum)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum)) 
    button = browser.find_element_by_css_selector(".btn[type = 'submit']")
    button.click()

finally :
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
