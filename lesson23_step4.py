from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()



try: 
    
    browser.get(link)


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x = browser.find_element(By.ID, "input_value").text
    total = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(total)

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()