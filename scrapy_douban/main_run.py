
from scrapy import cmdline



if __name__ == '__main__':
    #在pycharm中运行爬虫
    cmdline.execute("scrapy crawl douban_moive".split())