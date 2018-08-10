import scrapy
from scrapy_splash import SplashRequest


class MySpider(scrapy.Spider):
    name = 'download_with_splash'
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/index.html', ]
    head_url = 'http://www.ygdy8.net'
    movie_url = 'http://www.ygdy8.net/html/gndy/dyzz/'

    def parse(self, response):
        # 访问详细页的url
        all_selector = response.xpath('//a[@class="ulink"]')
        if all_selector is not None:
            for i in all_selector:
                yield SplashRequest(self.head_url + i.extract().split('\"')[1], self.save, args={'wait': 0.5})

        # 下一页
        next = response.xpath('//a[text()="下一页"]').extract_first()
        if next is not None:
            yield response.follow(self.movie_url + next.split('\"')[1], self.parse)

    def save(self, response):
        res = response.xpath('//td[@bgcolor="#fdfddf"]')[0]
        if res is not None:
            thunder_list = res.extract().split('\"')
            thunder = thunder_list[-2]
            title = thunder_list[-1].split('www.ygdy8.com.')[-1].split('</a>')[0]
            with open('thunder_splash.text', 'a+', encoding='utf-8') as f:
                f.write(title + '\n' + thunder + '\r\n')