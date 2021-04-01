# github-bitbucket-gitlab

The code was developed in window 10 and has 4 requirements:

1- mysql installation;
2- Presence of the pymysql package that can be obtained through: pip install pymysql;
3- Presence of the sqlalchemy package that can be obtained through: pip install sqlalchemy or pip install web_scrapy/requirment.text;
4- Install Scrapy : pip install scrapy;

##Using this scrapy project In the folder of your choice, make a copy of the directory on github: git clone

##This routine is capable of extracting url, title, price, e-comerce name, number of ratings and ratings.
## web scraping consumed 2:30h

##Goals:
1- Use of xpath when searching for links -> Ok;
2- Persistence of information(MYSQL)-> Ok;
3-Pipelene -> Ok;

##Execution:
1-database configuration in the settings file: CONNECTION_STRING; 
2- run: scrapy crawl ws;

