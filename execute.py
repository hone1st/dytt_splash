from scrapy.cmdline import execute

# 开始spider

# 测试没有splash是否能获取动态加载数据
execute(["scrapy", 'crawl', 'none_splash_dytt'])
# 测试splash获取动态加载
execute(["scrapy", 'crawl', 'with_splash_dytt'])
# 下载迅雷链接
execute(["scrapy", 'crawl', 'download_with_splash'])
# 下载ftd链接
execute(["scrapy", 'crawl', 'with_splash_dytt'])
