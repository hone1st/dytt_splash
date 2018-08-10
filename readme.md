##最基本的splash-scrapy的设置：
###首先是：setting.py文件的设置：如下
####添加Splash中间件  指定优先等级
######DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

#### 设置SPLASH_URL
######SPLASH_URL = 'http://192.168.99.100:8050'
####设置Splash自己的去重过滤器
######DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
#### 缓存后台存储介质
######HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
###然后是使用在spider中：最基本的使用如例子所示