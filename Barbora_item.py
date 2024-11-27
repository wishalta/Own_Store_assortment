from Barbora_search import barbora_search
from Open_db import open_db


class barbora_item():
    def __init__(self, driver):
        self.driver = driver

    def insert_data(self):
        self.db = open_db()
        query = (f"INSERT INTO `product_info`(`id`, `product_name`, `seller`, `quantity`, `price`) VALUES (%s, %s, %s, %s, %s)")
        self.db.conn.cursor().execute(query, (0, self.title, self.seller, self.quantity, self.price))
        self.db.conn.commit()
        self.db.close()

    def fill(self):
        bs = barbora_search(self.driver)
        self.title = bs.search_title()
        self.seller = bs.search_seller()
        self.quantity = bs.search_quantity()
        self.price = bs.search_price()