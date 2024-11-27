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
        # print(corrected_uppercase_words)
        if corrected_uppercase_words == "":
            corrected_uppercase_words = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[3]/div/dl[2]/dd[3]').text
            # print(f'|{corrected_uppercase_words}|')
            if corrected_uppercase_words == "":
                return False
        return corrected_uppercase_words

    def search_quantity(self):
        # -----------------------------------VEIKIA-------------------------------------------
        if True:
            title1 = self.driver.find_element(By.CLASS_NAME, 'b-product-info--title').text
            dl_element = self.driver.find_element(By.CLASS_NAME, "b-dl-align-left")
            info_dict = {}
            I_need = 'Grynasis kiekis'
            dt_elements = dl_element.find_elements(By.TAG_NAME, "dt")
            dd_elements = dl_element.find_elements(By.TAG_NAME, "dd")
            for dt, dd in zip(dt_elements, dd_elements):
                key = dt.text.strip()
                value = dd.text.strip()
                info_dict[key] = value
            print(info_dict)
            if info_dict.get('Grynasis kiekis (g/ml):') is not None:
                return info_dict.get('Grynasis kiekis (g/ml):')
            else:
                # return 'Nebera'
                quantity = re.findall(r'\b\d+\b|\b[a-zA-Z]\b', title1)
                quantity_answer = ' '.join(quantity)
                return quantity_answer

        # title1 = self.driver.find_element(By.CLASS_NAME, 'b-product-info--title').text
        # else:
        #     quantity = re.findall(r'\b\d+\b|\b[a-zA-Z]\b', title1)
            # quantity_answer = ' '.join(quantity)
            # return quantity_answer

    def search_price(self):
        price = []
        price = self.driver.find_element(By.XPATH, '//*[@id="fti-product-price--0"]/div[1]/div[1]').text
        corrected_price = re.sub(r'\s+', '', price).strip()
        # print(corrected_price)
        return corrected_price









# uppercase = re.findall(r'\b[A-ZĄČĘĖĮŠŲŪŽ]{3,}\b', title1)
