from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
name=input('Enter your search query: ')
driver=webdriver.Chrome(options=options)
driver.get('https://www.google.com/')
search=driver.find_element(By.CLASS_NAME,'gLFyf')
search.send_keys(name)
search.send_keys(Keys.ENTER)
