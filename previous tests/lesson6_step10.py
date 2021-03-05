from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try :

    browser = webdriver.Chrome()
    browser.get(link)
    
    element = browser.find_element_by_id("treasure")
    x_element = element.get_attribute("valuex")
    print(x_element)
    x = x_element
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    
    option2 = browser.find_element_by_css_selector("[value = 'robots']")
    option2.click()
    
    button = browser.find_element_by_css_selector(".btn[type = 'submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()