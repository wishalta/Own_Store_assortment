from time import sleep
import time

from selenium.webdriver.common.by import By


class barbora_shop():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def functions_activation(self):
        self.cookies_accept()
        items = self.products_url_gathering()


    def cookies_accept(self):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"]').click()
        time.sleep(400)

    def products_url_gathering(self):
        items = []
        for i in range(1, 20):
            self.driver.get(f'{self.url}?_gl={i}')
            item = self.driver.find_element(By.XPATH, '//*[@id="category-page-results-placeholder"]/div/ul')
            tag = item.find_elements(By.TAG_NAME, 'li')
            print(len(tag))
            if len(tag) == 0:
                break
            for a in tag:
                href = a.find_element(By.TAG_NAME, 'a').get_attribute("href")
                items.append(href)
                # print('atejo')
        print(items)
        return items

# //*[@id="category-page-results-placeholder"]/div/ul/li[1]
#  ?page=