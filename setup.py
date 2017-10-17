from setuptools import setup

setup(
    name = "Epoca_Cosmeticos_Web_Crawler",
    version = "0.1",
    packages = ['epoca_cosmeticos_web_crawler', 'tests'],

    # metadata
    author = "Livia Costa Pereira",
    author_email = "livaper@gmail.com",
    description = "Library to crawl the website epocacosmeticos.com.br"
                  "and list all product's name, title and url in a csv",
)