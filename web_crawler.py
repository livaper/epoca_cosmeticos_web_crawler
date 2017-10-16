# Recupera os links das postagens (requests)
# Extrai os dados (beautifulsoup)
# Gerando saida (csv)
# Execução


# to connect to internet
import requests
# inspect the page
from bs4 import BeautifulSoup
import csv
from functools import reduce
from product import Product

perfums_url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000001%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
hair_url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000037%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
makeup_url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000004%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
dermocosmetics_url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000130%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
treatments_url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000089%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
body_bath_url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000070%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
nails_url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000013%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
discounts_url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=H%3a377&O=OrderByBestDiscountDESC&PS=48&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
releases_url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=H%3a136&O=OrderByNameDESC&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber='
gifts_url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000199%2f&PS=16&sl=3d564047-8ff1-4aa8-bacd-f11730c3fce6&cc=4&sm=0&PageNumber='



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
        if product_title != None:
            product_title = product_title.title.string
    for product_name in parser.findAll('div', {'class': 'productName'}):
        if product_name != None:
            product_name = product_name.string
    return Product(product_url, product_title, product_name)


"""
crawl through all products over a given category

input: category url base

output: Set of Products from a category 
"""


def category_crawler(url):
    page = 1
    parser = _get_parser(url + str(page))
    product_set = set()

    try:
        while parser.find('div', {'class': 'shelf-default'}) != None:
            for link in parser.findAll('a', {'class': 'shelf-default__product-name'}):
                product_url = link.get('href')
                product = get_product(product_url)
                product_set.add(product)

                # retirar!
                print('Page '+ str(page))

            page += 1
            parser = _get_parser(url + str(page))
    except Exception as exception:
        print(" Exception {} ocurred when trying to crawl page {}".format(exception, url + str(page)))

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
                csvfile.write(product.title)
                csvfile.write(', ')
                csvfile.write(product.name)
                csvfile.write(', ')
                csvfile.write(product.url)
                csvfile.write('\n')

        csvfile.close()

    except Exception:
        print("Could not save file")


def main():
    list_of_set_of_products_possibly_with_repetition = get_products_posibly_with_repetition()

    # counter = list_of_set_of_products_possibly_with_repetition[0].__len__() + \
    # list_of_set_of_products_possibly_with_repetition[1].__len__() + \
    # list_of_set_of_products_possibly_with_repetition[2].__len__() + \
    # list_of_set_of_products_possibly_with_repetition[3].__len__() + \
    # list_of_set_of_products_possibly_with_repetition[4].__len__() + \
    # list_of_set_of_products_possibly_with_repetition[5].__len__() + \
    # list_of_set_of_products_possibly_with_repetition[6].__len__() + \
    # list_of_set_of_products_possibly_with_repetition[7].__len__() + \
    # list_of_set_of_products_possibly_with_repetition[8].__len__() + \
    # list_of_set_of_products_possibly_with_repetition[9].__len__()
    #
    # print('Tamanho lista com possivel repeticao ' + str(counter))
    #
    list_of_products_without_repetition = join_sets_of_products(list_of_set_of_products_possibly_with_repetition)
    print('Tamanho lista sem repeticao ' + str(list_of_products_without_repetition.__len__()))

    save_csv(list_of_products_without_repetition)


def get_products_posibly_with_repetition():
    list_of_set_of_products_possibly_with_repetition = list()
    # ok 800 list_of_set_of_products_possibly_with_repetition.append(category_crawler(perfums_url))
    #ok 800 list_of_set_of_products_possibly_with_repetition.append(category_crawler(hair_url))
    list_of_set_of_products_possibly_with_repetition.append(category_crawler(makeup_url))
    # list_of_set_of_products_possibly_with_repetition.append(category_crawler(dermocosmetics_url))
    # list_of_set_of_products_possibly_with_repetition.append(category_crawler(treatments_url))
    # list_of_set_of_products_possibly_with_repetition.append(category_crawler(body_bath_url))
    # list_of_set_of_products_possibly_with_repetition.append(category_crawler(nails_url))
    # list_of_set_of_products_possibly_with_repetition.append(category_crawler(discounts_url))
    # list_of_set_of_products_possibly_with_repetition.append(category_crawler(releases_url))
    # list_of_set_of_products_possibly_with_repetition.append(category_crawler(gifts_url))
    return list_of_set_of_products_possibly_with_repetition


main()
