from selenium import webdriver
import time

chrome_driver_path = "/Users/biancaoprisa/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
game_is_on = True

timeout = time.time() + 5
while game_is_on:
    cookie.click()
    if time.time() > timeout:
        break

money = driver.find_element_by_id("money").text
print(money)

grandma = driver.find_element_by_id("buyGrandma")
factory = driver.find_element_by_id("buyFactory")

def game():
    game_is_on = True
    timeout = time.time() + 5
    while game_is_on:
        cookie.click()
        if time.time() > timeout:
            if int(money) > 500:
                factory.click()
            elif int(money) > 100:
                grandma.click()
            break
    game()

game()

