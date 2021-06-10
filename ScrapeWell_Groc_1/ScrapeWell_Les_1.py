import requests
import bs4
from bs4 import BeautifulSoup

page_url = "https://www.wholefoodsmarket.com/sales-flyer?store-id=10005"

page_sourced = requests.get(page_url).content 

html_content = BeautifulSoup(page_sourced, "html.parser")
sale_items = html_content.findAll('h4', class_="w-sales-tile__product")
sale_item_titles = [i.text for i in sale_items]
print(sale_item_titles)


#we need to make this a function - one line in future



