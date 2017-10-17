# Recupera os links das postagens (requests)
# Extrai os dados (beautifulsoup)
# Gerando saida (csv)
# Execução


from functools import reduce

# to connect to internet
import requests
# inspect the page
from bs4 import BeautifulSoup

from epoca_cosmeticos_web_crawler.product import Product

"""
Instantiate and return a parser from a given url

input: url

output: BeautifulSoup parser instantiated
"""


def _get_parser(url):
    source_code = requests.get(url)
    html = source_code.text
    return BeautifulSoup(html)


"""
Navigate through the item and get the product title and name

input: item's url

output: tuple containing product name and title 
"""


def get_product(product_url):
    parser = _get_parser(product_url)
    for product_title in parser.findAll('head'):
        if product_title:
            product_title = product_title.title.string
    for product_name in parser.findAll('div', {'class': 'productName'}):
        if product_name:
            product_name = product_name.string
    return Product(product_url, product_title, product_name)


"""
crawl through all products over a given category

input: category url base

output: Set of Products from a category 
"""


def category_crawler(url, page=1):
    parser = _get_parser(url + str(page))
    product_set = set()

    if parser.find('div', {'class': 'shelf-default'}) and page <= 2 :
        for link in parser.findAll('a', {'class': 'shelf-default__product-name'}):
            product_url = link.get('href')
            product = get_product(product_url)
            product_set.add(product)

        # retirar!
        print('Page '+ str(page))
        page += 1
        product_set.update(category_crawler(url, page))
    return product_set


"""
Unify all sets of products in one set, assuring there is no repetition in the end, before printing in the csv

input: list of sets of products from different categories

output: a set containing all products from epocacosmeticos.com.br
"""


def join_sets_of_products(products):
    return reduce((lambda x, y: x.union(y)), products)


"""
Save all products in products.csv

input: Set of all products

output: --
"""


def save_csv(products):
    try:
        with open('products.csv', 'w', encoding="utf-8") as csvfile:
            csvfile.write('Título, Nome, URL\n')
            for product in products:
                product_line = ", ".join([product.title, product.name, product.url])
                csvfile.write("{}\n".format(product_line))

        csvfile.close()
        print('The file products.csv was saved in this folder with sucsess')

    except Exception:
        print("Could not save file")

