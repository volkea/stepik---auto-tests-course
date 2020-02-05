from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	button1 = browser.find_element_by_tag_name("button")
	button1.click()
	
	confirm = browser.switch_to.alert
	confirm.accept()
	
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)
	#option1 = browser.find_element_by_id("robotCheckbox")
	#option1.click()
	#button = browser.find_element_by_css_selector("[type='submit']")
	#browser.execute_script("window.scrollBy(0, 100);")
	#option2 = browser.find_element_by_css_selector("[id='robotsRule']")
	#option2.click()
	button2 = browser.find_element_by_css_selector("[type='submit']")
	button2.click()
	
	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
