"""
This spider was written to find all the urls of muslim girls on hamariweb.com
and exporting it to a csv. Doing this helps our next spider called boys_name_data
Author: Muhammad Owais
Date: 27-12-2022
"""
import scrapy
import string

class namelinks(scrapy.Spider):
    name = "girl_links"
    start_urls=[]

    ### make a list of start urls, the names are divided as per starting character
    for character in string.ascii_lowercase:
        start_urls.append(f"https://hamariweb.com/names/muslim-girl-names-starting-with-{character}/page-1")


    def parse(self, response):

        ### This will iterate all the name_links found on each page, 1 page has 30 links
        ### accquired data is stored in dict
        for link in response.xpath('//td/a/@href').getall():
            item = ['https://hamariweb.com' + link]
            yield {
                "links" : item
            }

        ### the below codes find the next button on page and iterates the algo to the next link
        ### if it is the last page of each character is returns none and crawler moves to next character
        pagination_links = response.xpath("//div/nav/a/@href").getall()

        if len(pagination_links) >= 7:
            next_link = "https://hamariweb.com" + pagination_links[-2]
        else:
            next_link = None
        
        if next_link is not None:
            yield response.follow(next_link, callback=self.parse)
    