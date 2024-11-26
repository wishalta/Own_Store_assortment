from Barbora_search import barbora_search
from Open_db import open_db


class barbora_item():
    def __init__(self, driver):
        self.driver = driver

    def insert_data(self):
        self.db = open_db()
        query = (f"INSERT INTO `start_info` (`id`, `title`, `quantity`) VALUES (%s, %s, %s)")
        self.db.conn.cursor().execute(query, (0, self.title, self.size))
        self.db.conn.commit()
        self.db.close()

    def fill(self):
        bs = barbora_search(self.driver)
        self.title = bs.search_title()
        self.size = bs.search_size()