from scrapy import Request, Spider
import re

class AppleSpider(Spider):
    name = 'apple_store_spider'
    start_urls = ['https://www.apple.com/uk/search/eating-disorder?src=serp']

    def parse(self, response):
        LINK_SELECTOR = '.as-links-name ::attr(href)'
        urls = response.css(LINK_SELECTOR).extract()
        print(type(urls))
        for url in urls:
            yield Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        app = {}

        url_parts = re.search('app/([\w-]+)/id([0-9]+)',response.url)
        app['url_name'] = url_parts.group(1)
        app['id'] = url_parts.group(2)

        name = response.css('.product-header__title ::text').extract_first().strip()
        app['name'] = name

        rating_and_number = response.css('.we-rating-count ::text').extract_first().split(' • ')
        rating = rating_and_number[0]
        num_ratings = rating_and_number[1].split()[0]
        app['rating'] = rating
        app['num_ratings'] = num_ratings
        
        description = response.css('.section__description').xpath('string(.)').extract_first()
        description = description.strip().replace('Description','').strip()
        app['description'] = description

        genre = response.xpath('//a[starts-with(@href,"https://itunes.apple.com/gb/genre/")]/text()')
                        .extract()[0]
                        .strip()
        app['genre'] = genre

        yield app