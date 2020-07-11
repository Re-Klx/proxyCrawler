# -*- coding: utf-8 -*-
import telnetlib
import time

import scrapy

from bilibili_spider.proxyCrawler.proxyCrawler.items import ProxycrawlerItem


class ProxycrawlerSpiderSpider(scrapy.Spider):
    name = 'proxyCrawler_spider'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']

    def get_one_page(url, response):  # 获取网页xml
        return response.text

    def parse(self, response):
        # print(response.text)
        ip_list = response.xpath("//div[@id='list']/table[@class='table table-bordered table-striped']/tbody/tr")
        for i_item in ip_list:
            proxy_item = ProxycrawlerItem()
            proxy_item['type_name'] = i_item.xpath("./td[4]/text()").extract_first()
            proxy_item['ip_name'] = i_item.xpath("./td[1]/text()").extract_first()
            proxy_item['port_name'] = i_item.xpath("./td[2]/text()").extract_first()
            print(proxy_item)
            # 验证ip是否可用
            if self.telnet(proxy_item):
                time.sleep(1)
                ip = 'http://' + proxy_item['ip_name'] + ':' + proxy_item['port_name']
                with open('valid_proxy_ip.txt', 'a') as f:
                    f.write(ip+'\n')
                    f.close()
                yield proxy_item

        # 解析下一页规则，通过观察url发现变动部分只有数字，即页数，直接for循环回调函数即可
        for next_link in range(11, 20): # 从第二页开始，因为起始页是第一页
            next_url = "https://www.kuaidaili.com/free/inha/{0}/".format(next_link)
            yield scrapy.Request(next_url, callback=self.parse)

    def telnet(self, proxy_item):  # 检验代理ip的可用性，使用telnet检验，延时10秒
        try:
            telnetlib.Telnet(proxy_item['ip_name'], port=proxy_item['port_name'], timeout=10.0)
        except:
            print('connect failure')
            return False
        else:
            print('conncet success')
            return True
