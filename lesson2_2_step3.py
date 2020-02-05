from selenium import webdriver
import time
import math

try:
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	x_element = browser.find_element_by_id("num1")
	y_element = browser.find_element_by_id("num2")
	x = x_element.text
	y = y_element.text
	sum = int(x) + int(y)
	sum_str = str(sum)
	
	from selenium.webdriver.support.ui import Select
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(sum_str)
	
	button = browser.find_element_by_css_selector("[type='submit']")
	button.click()
	
	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
