import scrapy

class test(scrapy.Spider):
    name = 'bz_spider'
   
    # http://www.bangzhuanpingtai.com/yuehui1/
    #result = response.xpath('//table //a[@role="button"]').xpath('@href').extract();    取所有城市的地址
    #arr = response.xpath('//table[1] //p[1]/text()').extract()
    # http://www.bangzhuanpingtai.com/Yuehui1/home/info?city=%E5%B9%BF%E5%B7%9E&page=4
    # start_urls  = [ 
    #     'http://www.bangzhuanpingtai.com/Yuehui1/home/info?city=%E5%B9%BF%E5%B7%9E',
    #     'http://www.bangzhuanpingtai.com/Yuehui1/home/info?city=%E5%B9%BF%E5%B7%9E&page=2',
    #     'http://www.bangzhuanpingtai.com/Yuehui1/home/info?city=%E5%B9%BF%E5%B7%9E&page=3',
    #     'http://www.bangzhuanpingtai.com/Yuehui1/home/info?city=%E5%B9%BF%E5%B7%9E&page=4',
    #     'http://www.bangzhuanpingtai.com/Yuehui1/home/info?city=%E5%B9%BF%E5%B7%9E&page=5'
    #     ]


    # start_urls = [
    #     'http://www.bangzhuanpingtai.com/Yuehui1/home/info?city=%E6%9C%9D%E9%98%B3%E5%8C%BA%7C%E6%B5%B7%E6%B7%80%E5%8C%BA%7C%E4%B8%9C%E5%9F%8E%E5%8C%BA%7C%E8%A5%BF%E5%9F%8E%E5%8C%BA%7C%E7%9F%B3%E6%99%AF%E5%B1%B1%7C%E4%B8%B0%E5%8F%B0%E5%8C%BA%7C%E5%AE%A3%E6%AD%A6%E5%8C%BA%7C%E5%B4%87%E6%96%87%E5%8C%BA%7C%E5%8C%97%E4%BA%AC%7C%E9%80%9A%E5%B7%9E%E5%8C%BA%7C%E5%A4%A7%E5%85%B4%E5%8C%BA',
    #     'http://www.bangzhuanpingtai.com/Yuehui1/home/info?city=%E6%9C%9D%E9%98%B3%E5%8C%BA%7C%E6%B5%B7%E6%B7%80%E5%8C%BA%7C%E4%B8%9C%E5%9F%8E%E5%8C%BA%7C%E8%A5%BF%E5%9F%8E%E5%8C%BA%7C%E7%9F%B3%E6%99%AF%E5%B1%B1%7C%E4%B8%B0%E5%8F%B0%E5%8C%BA%7C%E5%AE%A3%E6%AD%A6%E5%8C%BA%7C%E5%B4%87%E6%96%87%E5%8C%BA%7C%E5%8C%97%E4%BA%AC%7C%E9%80%9A%E5%B7%9E%E5%8C%BA%7C%E5%A4%A7%E5%85%B4%E5%8C%BA&page=2',
    #     'http://www.bangzhuanpingtai.com/Yuehui1/home/info?city=%E6%9C%9D%E9%98%B3%E5%8C%BA%7C%E6%B5%B7%E6%B7%80%E5%8C%BA%7C%E4%B8%9C%E5%9F%8E%E5%8C%BA%7C%E8%A5%BF%E5%9F%8E%E5%8C%BA%7C%E7%9F%B3%E6%99%AF%E5%B1%B1%7C%E4%B8%B0%E5%8F%B0%E5%8C%BA%7C%E5%AE%A3%E6%AD%A6%E5%8C%BA%7C%E5%B4%87%E6%96%87%E5%8C%BA%7C%E5%8C%97%E4%BA%AC%7C%E9%80%9A%E5%B7%9E%E5%8C%BA%7C%E5%A4%A7%E5%85%B4%E5%8C%BA&page=3',
    #     'http://www.bangzhuanpingtai.com/Yuehui1/home/info?city=%E6%9C%9D%E9%98%B3%E5%8C%BA%7C%E6%B5%B7%E6%B7%80%E5%8C%BA%7C%E4%B8%9C%E5%9F%8E%E5%8C%BA%7C%E8%A5%BF%E5%9F%8E%E5%8C%BA%7C%E7%9F%B3%E6%99%AF%E5%B1%B1%7C%E4%B8%B0%E5%8F%B0%E5%8C%BA%7C%E5%AE%A3%E6%AD%A6%E5%8C%BA%7C%E5%B4%87%E6%96%87%E5%8C%BA%7C%E5%8C%97%E4%BA%AC%7C%E9%80%9A%E5%B7%9E%E5%8C%BA%7C%E5%A4%A7%E5%85%B4%E5%8C%BA&page=4',
    #     'http://www.bangzhuanpingtai.com/Yuehui1/home/info?city=%E6%9C%9D%E9%98%B3%E5%8C%BA%7C%E6%B5%B7%E6%B7%80%E5%8C%BA%7C%E4%B8%9C%E5%9F%8E%E5%8C%BA%7C%E8%A5%BF%E5%9F%8E%E5%8C%BA%7C%E7%9F%B3%E6%99%AF%E5%B1%B1%7C%E4%B8%B0%E5%8F%B0%E5%8C%BA%7C%E5%AE%A3%E6%AD%A6%E5%8C%BA%7C%E5%B4%87%E6%96%87%E5%8C%BA%7C%E5%8C%97%E4%BA%AC%7C%E9%80%9A%E5%B7%9E%E5%8C%BA%7C%E5%A4%A7%E5%85%B4%E5%8C%BA&page=5',
    # ]   

    start_urls  = [ 
        'http://www.bangzhuanpingtai.com/yuehui1/home/info?city=%E6%88%90%E9%83%BD'
        ]
    baseUrl = start_urls[0]

    count = 1
        
    def parse(self,response):
        result =  response.xpath('//table[1] //p[1]/text()').extract()
        if len(result)<1 :
            return
        
        data = response.url + '\n'
        for key in result:
            data += key + '\n'
        filename = 'C:\\Users\\zfz\Documents\\zfz\\bz_spider_chengdu.txt'  
        with open(filename, 'a') as f:        #python文件操作，不多说了；
            f.write(data)             #刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！
        self.log('保存文件: %d' % test.count)


        
        test.count +=  1 
        url = test.baseUrl + '&page=' + str(test.count)
        yield scrapy.Request(url, callback=self.parse)
