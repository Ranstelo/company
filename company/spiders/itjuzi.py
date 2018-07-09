# -*- coding: utf-8 -*-
import scrapy,json,time,random
from scrapy_redis.spiders import RedisSpider



class ItjuziSpider(RedisSpider):
    name = 'itjuzi'
    allowed_domains = ['itjuzi.com']
    start_urls = ['http://radar.itjuzi.com/company/infonew?page={}']

    def start_requests(self):
        cookies = "_ga=GA1.2.1831873868.1530361575; gr_user_id=98774bd1-9d56-4ec3-982c-78597e1486b1; _gid=GA1.2.555638236.1531036669; acw_tc=AQAAAFP1o3JQ6gMAIzBft1FHMxy62IKR; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1530361576,1531036669,1531037568; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1531037571; identity=511474992%40qq.com; remember_code=%2F6wbPG79iq; unique_token=586285; user-radar.itjuzi.com=%7B%22n%22%3A%22%5Cu6854%5Cu53cb4fe5fb1c2404c%22%2C%22v%22%3A2%7D; Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b=1531037574; MEIQIA_VISIT_ID=175qvXw6LnWPY7Cp1A406FxIncq; MEIQIA_EXTRA_TRACK_ID=16jkp2CE1ToZbbYhPPZ9w5uln48; gr_session_id_eee5a46c52000d401f969f4535bdaa78=0bcea6b2-5d8c-4ecf-9da2-f30835a8392e; gr_cs1_0bcea6b2-5d8c-4ecf-9da2-f30835a8392e=user_id%3A586285; gr_session_id_eee5a46c52000d401f969f4535bdaa78_0bcea6b2-5d8c-4ecf-9da2-f30835a8392e=true; session=5bf1b683690edf7e1ee599ee98a4caf4042440f2; _gat=1; Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b=1531042205"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(self.start_urls[0].format("1"),callback=self.parse,cookies=cookies)

    def parse(self, response):
        cookies = "_ga=GA1.2.1831873868.1530361575; gr_user_id=98774bd1-9d56-4ec3-982c-78597e1486b1; _gid=GA1.2.555638236.1531036669; acw_tc=AQAAAFP1o3JQ6gMAIzBft1FHMxy62IKR; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1530361576,1531036669,1531037568; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1531037571; identity=511474992%40qq.com; remember_code=%2F6wbPG79iq; unique_token=586285; user-radar.itjuzi.com=%7B%22n%22%3A%22%5Cu6854%5Cu53cb4fe5fb1c2404c%22%2C%22v%22%3A2%7D; Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b=1531037574; MEIQIA_VISIT_ID=175qvXw6LnWPY7Cp1A406FxIncq; MEIQIA_EXTRA_TRACK_ID=16jkp2CE1ToZbbYhPPZ9w5uln48; gr_session_id_eee5a46c52000d401f969f4535bdaa78=0bcea6b2-5d8c-4ecf-9da2-f30835a8392e; gr_cs1_0bcea6b2-5d8c-4ecf-9da2-f30835a8392e=user_id%3A586285; gr_session_id_eee5a46c52000d401f969f4535bdaa78_0bcea6b2-5d8c-4ecf-9da2-f30835a8392e=true; session=5bf1b683690edf7e1ee599ee98a4caf4042440f2; _gat=1; Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b=1531042205"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        json_str = json.loads(response.body_as_unicode())
        items = json_str["data"]["rows"]
        page_num = json_str["data"]["page_num"]
        page_total = json_str["data"]["page_total"]
        print(page_num,page_total)
        for item in items:
            print(type(item))
            yield item
        # with open("json.txt","a",encoding="utf-8") as f:
        #     f.write(json.dumps(datas,ensure_ascii=False,indent=2))


        time.sleep(random.randint(3,5))
        if page_num <= page_total:
            page_num += 1
            yield scrapy.Request(self.start_urls[0].format(page_num),callback=self.parse,cookies=cookies)


