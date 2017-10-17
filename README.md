# Epoca Cosméticos Web Crawler


<p>Library to crawl the website epocacosmeticos.com.br and list all product's name, title and url in a csv</p>

<h2>Requirements</h2>

Have python 3.6 or higher installed

<h2>Build</h2>

<p>Go to directory epoca_cosmeticos_web_crawler</p>
<p>Run command to generate the distribution</p>

	$ cd epoca_cosmeticos_web_crawler
	$ python3 setup.py sdist
*** the distribution file (Epoca Cosmeticos Web Crawler-0.1.tar.gz) is alredy built in dist directory ***

<h2>Install in your python enviroment</h2>

Copy the file 'Epoca_Cosmeticos_Web_Crawler-0.1.tar.gz' to an directory and unzip it.

Go to directory Epoca_Cosmeticos_Web_Crawler-0.1

Run command to install it

	$ tar -zxvf Epoca_Cosmeticos_Web_Crawler-0.1.tar.gz 
	$ cd Epoca_Cosmeticos_Web_Crawler-0.1
	$ python3 setup.py install

<h2>Usage</h2>

<h3>Command Line Interface</h3>

    $ python3 -m epoca_cosmeticos_web_crawler.tool
    'The file products.csv was saved in this folder with success'

<h3>Python Library</h3>


	$ python3
	>>> from epoca_cosmeticos_web_crawler.run import main
	>>> main()
    'The file products.csv was saved in this folder with success'
	
 <h2>TESTS</h2>

<h3>Run tests</h3>

<p>In the directory of the project epoca_cosmeticos_web_crawler, run the unittests</p>

	$ python3 -m unittest -v tests.web_crawler_test

  
      
