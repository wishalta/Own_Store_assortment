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
        links = self.groats_url_gathering()
        # suki cikla pro kateogirjas
        hrefs = self.products_url_gathering(links)
        print(hrefs)
        self.each_data_collect(hrefs)


    def cookies_accept(self):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"]').click()

    def groats_url_gathering(self):
        # time.sleep(100)
        # links = []
        # for x in range(1):
        #     item = self.driver.find_element(By. CLASS_NAME, f'b-category-children--item')
        #     elements =  item.find_elements(By.CLASS_NAME, 'b-category-children')
        #     print(elements)
        #     for something in elements   :
        #         categories = something.find_elements(By. TAG_NAME, 'li')
        #         print(f'sukasi')
        #         print(categories)
        #         for y in categories:
        #             link = y.find_element(By.TAG_NAME, 'a').get_attribute("href")
        #             links.append(link)
        #             print(f'cia:{links}')
        #     return links

        links = []
        for x in range(1):
            # item = self.driver.find_element(By. CLASS_NAME, f'b-category-children--item')
            elements =  self.driver.find_elements(By.CLASS_NAME, 'b-category-children--li')
            print(elements)
            # for something in elements   :
            #     categories = something.find_elements(By. TAG_NAME, 'a')
            #     print(f'sukasi')
            #     print(categories)
            for y in elements:
                link = y.find_element(By.TAG_NAME, 'a').get_attribute("href")
                links.append(link)
                print(f'cia:{links}')
        return links

    def products_url_gathering(self, links):
        hrefs = []
        for link in links:
            counter = 0

            self.driver.get(link)
            for i in range(100):
                counter += 1
                self.driver.get(f'{link}?page={counter}')
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
            # print(link)
            self.driver.get(link)
            item = barbora_item(self.driver)
            item.fill()
            item.insert_data()
# //*[@id="category-page-results-placeholder"]/div/ul/li[1]
#  ?page=