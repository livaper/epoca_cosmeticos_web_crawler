r"""Command-line tool to to crawl the website epocacosmeticos.com.br and list all product's name,
    title and url in a csv

Usage::
    $ python3 -m epoca_cosmeticos_web_crawler.tool
    'The file products.csv was saved in this folder with success'
"""
import sys
from epoca_cosmeticos_web_crawler.run import main as main_crawler


def main():
    try:
        main_crawler()
        print('The file products.csv was saved in this folder with success!')

    except Exception:
        print('Error to crawl www.epocacosmeticos.com.br . Please, contact the administrator!')
        sys.exit(1)


if __name__ == '__main__':
    main()