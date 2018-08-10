import scrapy
from scrapy_splash import SplashRequest

# 测试带splash加载某个详细页面来测试是否能看到迅雷链接


class MySpider(scrapy.Spider):
    name = 'with_splash_dytt'
    allowed_domains = ['www.dytt8.net']
    start_urls = [
        'http://www.dytt8.net/html/gndy/dyzz/20180809/57264.html',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        print('----------使用splash爬取电影天堂迅雷地址异步加载内容-----------')
        res = response.xpath('//td[@bgcolor="#fdfddf"]').extract()[0]
        print(res)
        print('---------------success----------------')