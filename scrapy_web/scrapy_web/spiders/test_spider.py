import scrapy

class test(scrapy.Spider):
    name = 'testspider'
    def start_request(self):
        urls = [
            'https://www.baidu.com',
            'http://localhost/action/json'
        ]
        for url in urls :
            yield scrapy.Request(url,callback=self.parse)
        
    def parse(self,response):
        page = response.url.split("/")[-2]     #根据上面的链接提取分页,如：/page/1/，提取到的就是：1
        filename = 'mingyan-%s.html' % page    #拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html
        with open(filename, 'wb') as f:        #python文件操作，不多说了；
            f.write(response.body)             #刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！
        self.log('保存文件: %s' % filename)      # 打个日志
