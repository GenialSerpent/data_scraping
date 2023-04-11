from requests import get
from bs4 import BeautifulSoup
from mysql.connector import connect

BASE_URL = "https://hotline.ua"
URL = f"{BASE_URL}/ua/office/proektory/"
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
page = get(URL, headers=HEADERS)
soup = BeautifulSoup(page.content,  "html.parser")

def open_spider(self, spider):
    self.connection = connect(
        host="localhost",
        user="root",
        password=""
    )
    self.cursor = self.connection.cursor()

    self.cursor.execute("CREATE DATABASE IF NOT EXISTS scrapy;")
    self.cursor.execute("USE scrapy;")
    self.cursor.execute("""CREATE TABLE IF NOT EXISTS
        items (
            id INT AUTO_INCREMENT,
            PRIMARY KEY (id),
            title VARCHAR(50) NOT NULL,
            specifications VARCHAR(50) NOT NULL,
            between VARCHAR(50) NOT NULL,
            price FLOAT DEFAULT 0,
        );""")

items = soup.find(name="div", class_="list-body__content").find_all(class_="list-item")

for item in items:
    title = item.find(name="a", class_="list-item__title").find(string=True, recursive=False).strip() # Назва
    specifications = item.find(class_="list-item__specifications-text").find(string=True, recursive=False).strip() # Опис
    between = item.find(class_="text-sm").find(string=True, recursive=False).strip() # Ціна від і до
    price = item.find(class_="price__value").find(string=True, recursive=False) # Ціна

    def process_item(self, item, spider):
        self.cursor.execute

        ("INSERT INTO items (title, specifications, bbetween, price) VALUES (%s, %s, %s, %s);",
        [item.get("title"), item.get("specifications"), item.get("between"), item.get("price")])

        self.connection.commit()
        return item

def close_spider(self, spider):
    self.connection.close()

