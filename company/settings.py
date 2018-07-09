# -*- coding: utf-8 -*-

# Scrapy settings for company project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# LOG_LEVEL = "WARNING"

BOT_NAME = 'company'

SPIDER_MODULES = ['company.spiders']
NEWSPIDER_MODULE = 'company.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16




# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application / json, text / javascript, * / *; q = 0.01',
    'Accept - Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_ga=GA1.2.1831873868.1530361575; gr_user_id=98774bd1-9d56-4ec3-982c-78597e1486b1; _gid=GA1.2.555638236.1531036669; acw_tc=AQAAAFP1o3JQ6gMAIzBft1FHMxy62IKR; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1530361576,1531036669,1531037568; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1531037571; identity=511474992%40qq.com; remember_code=%2F6wbPG79iq; unique_token=586285; user-radar.itjuzi.com=%7B%22n%22%3A%22%5Cu6854%5Cu53cb4fe5fb1c2404c%22%2C%22v%22%3A2%7D; Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b=1531037574; MEIQIA_VISIT_ID=175qvXw6LnWPY7Cp1A406FxIncq; MEIQIA_EXTRA_TRACK_ID=16jkp2CE1ToZbbYhPPZ9w5uln48; gr_session_id_eee5a46c52000d401f969f4535bdaa78=0bcea6b2-5d8c-4ecf-9da2-f30835a8392e; gr_cs1_0bcea6b2-5d8c-4ecf-9da2-f30835a8392e=user_id%3A586285; gr_session_id_eee5a46c52000d401f969f4535bdaa78_0bcea6b2-5d8c-4ecf-9da2-f30835a8392e=true; session=5bf1b683690edf7e1ee599ee98a4caf4042440f2; _gat=1; Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b=1531042205',
    'Host': 'radar.itjuzi.com',
    'Referer': 'http://radar.itjuzi.com//company',
    'X-Requested-With': 'XMLHttpRequest'
}

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
REDIS_URL = "redis://192.168.119.155:6379"

IPPOOL = [
    {'ip': '101.236.18.101:8866'},
    {'ip': '60.205.205.48:80'},
    {'ip': '125.118.147.42:6666'},
]


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'company.middlewares.CompanySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'company.middlewares.CompanyDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'company.pipelines.CompanyPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
