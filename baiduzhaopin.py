# -*- coding:utf-8 -*-
import re
import urllib.request
import random
import json
import jsonpath
from lxml import etree

#area = input("请输入你要查询的地区")
#job = input("请输入你要查询的工作")
#area = urllib.request.quote(area)
#job = urllib.request.quote(job)
area = urllib.request.quote("北京")
job = urllib.request.quote("python爬虫")
ua = [
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
            'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
            'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
            'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
            'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
        ]

with open("./baiduzhappin1.txt", "w+", encoding="utf-8") as f:
    for i in range(1, 13):
        try:
            url = "http://zhaopin.baidu.com/api/quanzhiasync?query="+job+"&sort_type=1&city_sug="+area+"&detailmode=close&rn=20&pn="+str((i-1)*20)
            #url = "http://zhaopin.baidu.com/quanzhi?tid=4139&ie=utf8&oe=utf8&query=python%E7%88%AC%E8%99%AB&city_sug=%E5%8C%97%E4%BA%AC&qq-pf-to=pcqq.temporaryc2c"
            req = urllib.request.Request(url)
            req.add_header("User-Agent", random.choice(ua))
            data = urllib.request.urlopen(req).read().decode("utf-8", "ignore")

            jsobj = json.loads(data)
            id_list = jsonpath.jsonpath(jsobj, "$..@id")
            print(jsonpath.jsonpath(jsobj, "$..@id"))
            print(len(id_list))
        except Exception as err:
            print(err)

        for j in range(0, len(id_list)):
            try:
                m = (i-1)*20+j
                #print(jsobj)
                this_id = id_list[j]
                this_id = urllib.request.quote(this_id)
                urll = "http://zhaopin.baidu.com/szzw?detailidx="+str(m)+"&city=%E5%8C%97%E4%BA%AC&id="+this_id+"&query=python%E7%88%AC%E8%99%AB%2B%E6%8B%9B%E8%81%98"
                req1 = urllib.request.Request(urll)
                req1.add_header("User-Agent", random.choice(ua))
                data1 = urllib.request.urlopen(req1).read().decode("utf-8", "ignore")
                selector = etree.HTML(data1)
                title = selector.xpath('//div[@class="top-txt"]/span[@class="title line-clamp1"]/text()')
                salary = selector.xpath('//div[@class="top-txt"]/span[@class="salary"]/text()')
            except Exception as err:
                print(err)
            description = selector.xpath('//div[@class="abs"]/p/text()')
            #print(description)
            try:
                f.write("标题：" + title[0] + "\r\n")
                f.write("工资" + salary[0] + "\r\n")
                for h in range(0, len(description)):
                    #print(description[h])

                    f.write(description[h]+"\r\n")

            except Exception as err:
                print(err)
            f.write("==========="+"第"+str(m)+"个"+"==============\r\n")