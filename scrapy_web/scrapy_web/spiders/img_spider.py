import scrapy
from scrapy_web.items import ImgSpiderItem

class img_spider(scrapy.Spider):
    name = 'img_spider'
   
  
    start_urls  = [ 
        'https://www.mm131.net/'
        ]
    baseUrl = start_urls[0]

    count = 1
        
    def parse(self,response):
        
        result = response.xpath('//div[@class="main"] //img/@src').extract() 
        if(len(result)<1):
            return
       
        imgItem = ImgSpiderItem()
        imgItem['ImgUrl'] = result
      
        yield imgItem

