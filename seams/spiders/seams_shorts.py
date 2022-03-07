import scrapy


class SeamsShortsSpider(scrapy.Spider):
    name = 'seams_shorts'
    allowed_domains = ['in.seamsfriendly.com']
    start_urls = ['http://in.seamsfriendly.com/collections/shorts']

    def parse(self, response):
        products=response.css('.ProductItem')
       
        for product in products:
            title=product.xpath("descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' ProductItem__Title ')]/descendant-or-self::*/a/text()").get()
            price=product.xpath("descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' ProductItem__Price ')]/text()").get()
            image_urls=product.xpath("descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' ProductItem__Image ')]/@data-src").getall()
            # colors=product.xpath("")
            
            yield{
                'Title':title,
                'Price':price[1:],
                'image_urls':["https:"+img for img in image_urls],
            }
            