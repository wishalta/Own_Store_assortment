from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from Barbora_shop import barbora_shop

def initGathering():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    return driver, wait

def Execute_gathering():
    driver, wait = initGathering()
    barbora = barbora_shop(driver, "https://www.barbora.lt/bakaleja/kruopos/grikiai")
    barbora.functions_activation()

Execute_gathering()