import scrapy


class MySpider(scrapy.Spider):

    name = 'download_none_splash'
    # 开始页面
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/index.html',]
    head_url = 'http://www.ygdy8.net'
    movie_url = 'http://www.ygdy8.net/html/gndy/dyzz/'

    # 解析页面
    def parse(self, response):

        # 详情页解析
        edu = response.xpath('//tbody[1]').extract_first()
        if edu is not None:
            url = edu.split('href="')[1].split('">')[0]
            title = edu.split('">')[-1].split('阳光电影www.ygdy8.com.')[-1].split('</a></td>')[0]
            with open('ftd_none_splash.text', 'a+', encoding='utf-8') as f:
                f.write(url+'\r\n'+title+'\r\n')

        # 访问详细页的url
        all_selector = response.xpath('//a[@class="ulink"]')
        if all_selector is not None:
            for i in all_selector:
                yield response.follow(self.head_url + i.extract().split('\"')[1], self.parse)

        # 下一页
        next = response.xpath('//a[text()="下一页"]').extract_first()
        if next is not None:
            yield response.follow(self.movie_url + next.split('\"')[1], self.parse)