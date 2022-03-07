from turtle import title
import scrapy


class SeamsShortsSpider(scrapy.Spider):
    name = 'seams_shorts'
    allowed_domains = ['in.seamsfriendly.com']
    start_urls = ['http://in.seamsfriendly.com/collections/shorts']
    main_url=['http://in.seamsfriendly.com']

    def parse(self, response):
        
        product_url =[self.main_url[0] + url for url in response.css('.ProductItem').xpath('.//div/a/@href').extract()]
        for product in product_url:
            yield scrapy.Request(product,callback=self.product_extrat)
       
        
    def product_extrat(self,product):
        title=product.xpath(".//div[@class='Product__Info ']/div/div/div/h1/text()").extract_first()
        price =product.xpath(".//div[@class='Product__Info ']/div/div/div/div/div/span/text()").extract_first() 
        description=product.xpath('.//div[@class="ProductMeta__Description"]/div/p[2]/text()').extract_first()
        images=product.xpath(".//div[@class='Product__SlideshowNavScroller']/a/img/@src").extract()
       
        yield{

            "Title":title.strip(),
            "Price":price[1:],
            "Description":description,
            
            "Images_URLs":[" https:"+image for image in images],
        }


            