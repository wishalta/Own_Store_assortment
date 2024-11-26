from time import sleep
import time

from selenium.webdriver.common.by import By

from Barbora_item import barbora_item


class barbora_shop():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def functions_activation(self):
        self.cookies_accept()
        hrefs = self.products_url_gathering()
        self.each_data_collect(hrefs)


    def cookies_accept(self):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"]').click()

    def products_url_gathering(self):
        hrefs = []
        for i in range(1, 20):
            self.driver.get(f'{self.url}?page={i}')
            item = self.driver.find_element(By.XPATH, '//*[@id="category-page-results-placeholder"]/div/ul')
            tag = item.find_elements(By.TAG_NAME, 'li')
            print(len(tag))
            if len(tag) == 0:
                break
            for a in tag:
                href = a.find_element(By.TAG_NAME, 'a').get_attribute("href")
                hrefs.append(href)
                # time.sleep(500)
        return hrefs

    def each_data_collect(self, hrefs):
        for link in hrefs:
            print(link)
            self.driver.get(link)
            item = barbora_item(self.driver)
            item.fill()
            item.insert_data()
# //*[@id="category-page-results-placeholder"]/div/ul/li[1]
#  ?page=