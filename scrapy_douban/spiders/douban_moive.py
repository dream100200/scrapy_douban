import scrapy

from scrapy import Selector, Request
from scrapy.http import HtmlResponse
from scrapy import cmdline

from scrapy_douban.items import MovieItem


class DoubanMoiveSpider(scrapy.Spider):
    name = 'douban_moive'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        for page in range(2):
            url = f'https://movie.douban.com/top250?start={page * 25}&filter='
            yield Request(url=url, callback=self.parse)

    def parse(self, response: HtmlResponse, **kwargs):
        sel = Selector(response)
        li_items = sel.css('#content > div > div.article > ol > li')
        for li_item in li_items:
            movie_item = MovieItem()
            movie_item['title'] = li_item.css('span.title::text').extract_first()  ##content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)
            movie_item['rank'] = li_item.css('span.rating_num::text').extract_first()
            ##content > div > div.article > ol > li:nth-child(1) > div > div.info > div.bd > p.quote > span
            movie_item['subject'] = li_item.css('span.inq::text').extract_first()
            # print(movie_item['title'],movie_item['subject'],movie_item['rank'])
            yield movie_item


