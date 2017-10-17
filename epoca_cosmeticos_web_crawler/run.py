from epoca_cosmeticos_web_crawler.web_crawler import category_crawler, join_sets_of_products, save_csv

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


def main():
    list_of_set_of_products_possibly_with_repetition = list()
    categories_urls = []
    categories_urls.append(perfums_url)
    categories_urls.append(hair_url)
    categories_urls.append(makeup_url)
    categories_urls.append(dermocosmetics_url)
    categories_urls.append(treatments_url)
    categories_urls.append(body_bath_url)
    categories_urls.append(nails_url)
    categories_urls.append(discounts_url)
    categories_urls.append(releases_url)
    categories_urls.append(gifts_url)

    for category_url in categories_urls:
        category_products = category_crawler(category_url)
        list_of_set_of_products_possibly_with_repetition.append(category_products)

    list_of_products_unique = join_sets_of_products(list_of_set_of_products_possibly_with_repetition)

    save_csv(list_of_products_unique)