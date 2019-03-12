from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.watten.org/meinspiel")
wait = WebDriverWait(driver, 600)
def anmelden(name):
	login = driver.find_element_by_class_name("link1").click()
	username = driver.find_element_by_id("login_u_name").send_keys(name)
	time.sleep(1)
	anmelden = driver.find_element_by_xpath('//*[@id="login_popup"]/div[4]/a[2]').click()
	

anmelden("bottingisfun")
