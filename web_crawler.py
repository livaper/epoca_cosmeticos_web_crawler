# Recupera os links das postagens (requests)
# Extrai os dados (beautifulsoup)
# Gerando saida (csv)
# Execução

# to wait load the properly page
import time

# to connect to internet
import requests

# inspect the page
from bs4 import BeautifulSoup

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    for item_name in soup.findAll('div', {'class': 'product__floating-info--brand'}):
        print(item_name.string)

def trade_spider(max_pages):
    page = 50
    while page <= max_pages:
        url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=C%3a%2f1000001%2f&PS=16&sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber=' + str(page)
        print('url : ' + url)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        if soup.find('div', {'class': 'shelf-default'}) == None:
            print("Tá vazio!")
            break

        for link in soup.findAll('a', {'class': 'shelf-default__product-name'}):
            href = link.get('href')
            product = link.string
            print(href)
            print(product)
            get_single_item_data(href)
        page += 1

trade_spider(53)


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    for item_name in soup.findAll('div', {'class': 'product__floating-info--brand'}):
        print(item_name.string)