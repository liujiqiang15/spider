# -*- coding: utf-8 -*-
import scrapy

import pprint
class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://movie.douban.com/chart/']

    def parse(self, response):
        pass
"https://m10.music.126.net/20190322074001/27a3e26d74ef606b92035b184b4f55a9/ymusic/0153/0408/5558/69c72472ec3b68c3ec71b2a96ba13cf2.mp3"
"https://m10.music.126.net/20190322074636/f81b4e215b377c202ea8b53a96dc8d0e/ymusic/540f/0408/050e/ceebcac0da3bb270d96d2dd59e192003.mp3"
"curl 'http://vhotwsh.video.qq.com/flv/142/56/a02015yl8z1.p201.1.mp4?fmt=shd&vkey=76E5FB903E156460E54271EDE7AFCCA757453FC2918A11359C7932F9DE6C158796A0E93CC8510DAE4B3624F0E6F5746A88C5AD708676DA6899B9C12FA846260EAD55764615F143F7E52A6A223A07D3C50E5622BB53E5CB814EFAC6011F4670CED127A3CAB81C10176A3715442FEA7FC9662D5A18B643C7FB&platform=10901&level=0&sdtfrom=' -H 'Origin: https://v.qq.com' -H 'Accept-Encoding: identity;q=1, *;q=0' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"