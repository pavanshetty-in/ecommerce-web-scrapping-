import scrapy


class SeamsShortsSpider(scrapy.Spider):
    name = 'seams_shorts'
    allowed_domains = ['in.seamsfriendly.com']
    start_urls = ['http://in.seamsfriendly.com/collections/shorts']

    def parse(self, response):
        # title=response.css('.ProductItem__Title a::text').extract()
        # image_url=response.css('.ProductItem__Image').xpath('@src').getall()
        # price=response.css('.ProductItem__Price::text').extract()

        # for item in zip(title,price):
        #     scraped_info ={
        #         'title':item[0],
        #         'price':item[1],
        #     }

        # yield scraped_info
        products=response.css('.ProductItem')
        title=response.css('.ProductItem__Title a::text').extract()
        price=response.css('.ProductItem__Price::text').extract()
        image_url=response.css('.ProductItem__Image').xpath('@src').getall()
        
        for i in range(len(products)):
            
            yield{
                'Title':title[i],
                'Price':price[i][1:],
            }
            