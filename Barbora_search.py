import time
from traceback import print_tb

from selenium.webdriver.common.by import By
import re


class barbora_search():
    def __init__(self, driver):
        self.driver = driver

    def search_title(self):
        title1 = self.driver.find_element(By.CLASS_NAME, 'b-product-info--title').text
        lowercase = re.findall(r'\b[a-ząčęėįšųūž]{2,}\b|\b[A-ZĄČĘĖĮŠŲŪŽ][a-ząčęėįšųūž]+\b|\.', title1)
        corrected_lowercase_words = ' '.join(lowercase)
        # print(corrected_lowercase_words)
        return corrected_lowercase_words


    def search_seller(self):
        title1 = self.driver.find_element(By.CLASS_NAME, 'b-product-info--title').text
        uppercase = re.findall(r'\b[A-ZĄČĘĖĮŠŲŪŽ]{2,}\b', title1)
        corrected_uppercase_words = ' '.join(uppercase)
        print(corrected_uppercase_words)
        if corrected_uppercase_words == "":
            corrected_uppercase_words = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[3]/div/dl[2]/dd[3]').text
            print(f'|{corrected_uppercase_words}|')
            if corrected_uppercase_words == "":
                return False
        return corrected_uppercase_words





# uppercase = re.findall(r'\b[A-ZĄČĘĖĮŠŲŪŽ]{3,}\b', title1)
