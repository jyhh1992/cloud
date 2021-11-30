
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(3)
driver.close()