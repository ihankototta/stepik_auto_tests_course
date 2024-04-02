from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()



try: 
    
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    
    
    x = browser.find_element(By.ID, "input_value").text
    total = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(total)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()