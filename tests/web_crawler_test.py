import csv
import unittest

import requests
import requests_mock

from epoca_cosmeticos_web_crawler.web_crawler import category_crawler, get_product, join_sets_of_products, save_csv
from epoca_cosmeticos_web_crawler.product import Product


class WebCrawlerTest(unittest.TestCase):

    def mock_products(self):
        product1 = Product(
            url='http://www.epocacosmeticos.com.br/good-girl-eau-de-parfum-carolina-herrera-perfume-feminino/p',
            title='Perfume Good Girl Carolina Herrera Feminino - Época Cosméticos',
            name='Good Girl Carolina Herrera - Perfume Feminino - Eau de Parfum')
        product2 = Product(
            url='http://www.epocacosmeticos.com.br/good-girl-eau-de-parfum-carolina-herrera-perfume-feminino/p',
            title='Perfume 212 VIP Rosé Carolina Herrera Feminino - Época Cosméticos',
            name='212 VIP Rosé Carolina Herrera - Perfume Feminino - Eau de Parfum')
        product3 = Product(
            url='http://www.epocacosmeticos.com.br/la-vie-est-belle-eau-de-parfum-lancome-perfume-feminino/p',
            title='Perfume La Vie Est Belle Lancôme - Época Cosméticos',
            name='La Vie Est Belle Lancôme - Perfume Feminino - Eau de Parfum')
        product4 = Product(
            url='http://www.epocacosmeticos.com.br/1-million-eau-de-toilette-paco-rabanne-perfume-masculino/p',
            title='Perfume 1 Million Paco Rabanne Masculino - Época Cosméticos',
            name='1 Million Paco Rabanne - Perfume Masculino - Eau de Toilette')
        product5 = Product(
            url='http://www.epocacosmeticos.com.br/amor-amor-eau-de-toilette-cacharel-perfume-feminino/p',
            title='Perfume Amor Amor Cacharel Feminino - Época Cosméticos',
            name='Amor Amor Cacharel - Perfume Feminino - Eau de Toilette')
        product6 = Product(
            url='http://www.epocacosmeticos.com.br/polo-eau-de-toilette-ralph-lauren-perfume-masculino/p',
            title='Perfume Polo Ralph Lauren Masculino - Época Cosméticos',
            name='Polo Ralph Lauren - Perfume Masculino - Eau de Toilette')

        list_of_products = list()
        list_of_products.append(product1)
        list_of_products.append(product2)
        list_of_products.append(product3)
        list_of_products.append(product4)
        list_of_products.append(product5)
        list_of_products.append(product6)

        return list_of_products

    def mock_list_of_product_sets_setup(self):
        products = self.mock_products()

        mock_set1 = set()
        mock_set1.add(products[0])
        mock_set1.add(products[1])
        mock_set1.add(products[2])

        mock_set2 = set()
        mock_set2.add(products[1])
        mock_set2.add(products[2])
        mock_set2.add(products[3])

        mock_set3 = set()
        mock_set3.add(products[3])
        mock_set3.add(products[4])
        mock_set3.add(products[5])

        mock_set_list = list()
        mock_set_list.append(mock_set1)
        mock_set_list.append(mock_set2)
        mock_set_list.append(mock_set3)

        return mock_set_list

    def test_extract_title_and_name_from_product(self):
        url = 'http://www.epocacosmeticos.com.br/polo-red-eau-de-toilette-ralph-lauren-perfume-masculino/p'

        with open('./mock_files/polo-red-ralph-lauren.html', 'r', encoding='utf-8') as html:
            data = html.read().replace('\n', '')

        with requests_mock.mock() as m:
            m.get(url, text=data)
            r = requests.get(url)
            actual = get_product(url)

        expected = Product(
            url=url,
            title='Perfume Polo Red Ralph Lauren Masculino - Época Cosméticos',
            name='Polo Red Ralph Lauren - Perfume Masculino - Eau de Toilette')

        self.assertEqual(actual, expected)

    def test_join_sets_of_products(self):
        mock_list_of_product_sets = self.mock_list_of_product_sets_setup()

        actual_list_of_sets = join_sets_of_products(mock_list_of_product_sets)

        self.assertEqual(len(actual_list_of_sets), 6)

    def test_save_csv(self):
        list_of_products = self.mock_products()
        save_csv(list_of_products)

        with open('products.csv', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            actual_csv = [row for row in csvreader]

        with open('./mock_files/expected_csv.csv', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            expected_csv = [row for row in csvreader]

        self.assertEqual(actual_csv, expected_csv)