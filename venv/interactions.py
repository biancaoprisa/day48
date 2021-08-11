from selenium import webdriver

chrome_driver_path = "/Users/biancaoprisa/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

# articles = driver.find_element_by_css_selector("#articlecount a")
# print(articles.text)

button = driver.find_element_by_class_name("btn")
fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
fname.send_keys("Bianca")
lname.send_keys("Ishere")
email.send_keys("biancaishere@mail.com")
button.click()
