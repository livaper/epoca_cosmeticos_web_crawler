r"""Command-line tool to to crawl the website epocacosmeticos.com.br and list all product's name,
    title and url in a csv

Usage::
    $ python3 -m epoca_cosmeticos_web_crawler.tool
    'The file products.csv was saved in this folder with success'
"""

from epoca_cosmeticos_web_crawler.run import main


def main():

    print(main())
    print('The file products.csv was saved in this folder with success!')

if __name__ == '__main__':
    main()