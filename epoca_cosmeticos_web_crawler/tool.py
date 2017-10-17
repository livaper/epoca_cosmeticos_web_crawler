r"""Command-line tool to to crawl the website epocacosmeticos.com.br and list all product's name,
    title and url in a csv

Usage::
    $ python3 -m epoca_cosmeticos_web_crawler.tool
    'The file products.csv was saved in this folder with sucsess'
"""

from epoca_cosmeticos_web_crawler.run import main


def main():
    import sys


    try:
        print(main())
        print('The file products.csv was saved in this folder with success!')
    except Exception as e:
        print('There was an error trying to crawl Epoca Cosmeticos Website. Please call the administrator')
        sys.exit(1)


if __name__ == '__main__':
    main()