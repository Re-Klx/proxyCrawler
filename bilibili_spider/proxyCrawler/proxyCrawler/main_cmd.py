#_*_coding:utf-8_*_
# author     :一叶丶知秋
# create_time:2020/7/10 17:37
# file_name  :main_cmd.py
# IDE        :PyCharm
from scrapy import cmdline

# cmdline.execute('scrapy genspider proxyCrawler_spider www.kuaidaili.com'.split())
# cmdline.execute('scrapy startproject proxyCrawler'.split())
cmdline.execute('scrapy crawl proxyCrawler_spider'.split())
