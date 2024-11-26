from selenium.webdriver.common.by import By


class barbora_search():
    def __init__(self, driver):
        self.driver = driver

    def search_title(self):
        return self.driver.find_element(By.CLASS_NAME, 'b-product-info--title').text

    def search_size(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/h1').text