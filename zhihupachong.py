# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import re
import random
from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
ua = [
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
            'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
            'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
            'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
            'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
        ]
thisua = random.choice(ua)
headers = ("User-Agent", thisua)

opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
url = "https://www.zhihu.com/node/TopicsPlazzaListV2"
values = {"method": "next", "params": '{"topic_id":237,"offset":0,"hash_id":"990423d52d7f527ff662f67e6620a96e"}'}
data = urllib.parse.urlencode(values).encode(encoding='UTF8')
req = urllib.request.Request(url, data)
res = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
print(res)