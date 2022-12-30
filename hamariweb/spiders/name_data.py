"""
This crawler is writter to scrape data regarding each muslim name from hamariweb.com
There are a total of 15534 muslim boys names. This crawler will visit each url provided from
the csv file and scrape the data such as name, meaning, origin, gender.
Author: Muhammad Owais
Date: 27-12-2022
"""

import scrapy
import csv


class boys_name_data(scrapy.Spider):
    name = "name_data"
    filename = "links_girl.csv"
    start_urls = []

    ### read urls from csv file provided and append to start_urls
    with open(filename,"r") as f:
        reader = csv.DictReader(f)
        start_urls = [item["links"] for item in reader]


    ### parse data from each page and store relavent information as dict
    def parse(self, response):

        final_data = {}
        name_head = response.css("th::text").getall()
        name_data = response.css("td::text").getall()
        for i in range(len(name_head)):
            final_data.update({name_head[i] : name_data[i]})

        yield final_data
        