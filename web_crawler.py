# Recupera os links das postagens (requests)
# Extrai os dados (beautifulsoup)
# Gerando saida (csv)
# Execução


# to connect to internet
import requests
# inspect the page
from bs4 import BeautifulSoup
import csv
from product import Product

perfumes = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000001%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
cabelos = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000037%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
maquiagem = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000004%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
dermocosmeticos = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000130%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
tratamentos = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000089%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
corpo_banho = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000070%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
unhas = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000013%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
descontos = 'http://www.epocacosmeticos.com.br/buscapagina?fq=H%3a377&O=OrderByBestDiscountDESC&PS=48&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
lancamentos = 'http://www.epocacosmeticos.com.br/buscapagina?fq=H%3a136&O=OrderByNameDESC&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
brindes = 'http://www.epocacosmeticos.com.br/ganhe-brindes#'



"""
Instantiate and return a parser from a given url

input: url

output: BeautifulSoup parser instantiated
"""


def get_parser(url):
    source_code = requests.get(url)
    html = source_code.text
    return BeautifulSoup(html)


"""
Navigate through the item and get the product title and name

input: item's url

output: tuple containing product name and title 
"""


def get_product_name_and_title(item_url):
    parser = get_parser(item_url)
    for product_title in parser.findAll('head'):
        product_title = product_title.title.string
    for product_name in parser.findAll('div', {'class': 'productName'}):
        product_name = product_name.string
    return (product_name, product_title)


"""
crawl through all products over a given category

input: category url base

output: Set of Products from a category 
"""


def category_crawler(url):
    page = 1
    parser = get_parser(url + str(page))
    product_set = set()

    #while parser.find('div', {'class': 'shelf-default'}) != None:
    for link in parser.findAll('a', {'class': 'shelf-default__product-name'}):
        product_url = link.get('href')
        (product_name, product_title) = get_product_name_and_title(product_url)
        product = Product(product_url, product_name, product_title)
        product_set.add(product)

        #   page += 1
        #  parser = get_parser(url + str(page))
    return product_set


"""
Unify all sets of products

input: sets of products from diferent categories

output: a set containing all products from epocacosmeticos.com.br
"""


def join_sets_of_products(products):

# print the Set whith all Products in a csv
# i = 0
# while i < products.size():


"""
Save all products in products.csv

input: Set of all products

output: --
"""


def save_csv(products):

    try:
        with open('products.csv', 'w', encoding="utf-8") as csvfile:
            csvfile.write('Título, Nome, URL \n')
            for product in products:
                csvfile.write(product.title)
                csvfile.write(', ')
                csvfile.write(product.name)
                csvfile.write(', ')
                csvfile.write(product.url)
                csvfile.write('\n')

        csvfile.close()

    except Exception:
        print("Could not save file")


perfum_set = category_crawler(perfumes)
save_csv(perfum_set)
