# -*- coding: utf-8 -*-
import scrapy
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class MyprojectItem(scrapy.Item):
        mytitle = scrapy.Field()
        mytext = scrapy.Field()
        myurl = scrapy.Field()
        pass

class YuanSpider(scrapy.Spider):
        name = "yuan"
        start_urls = ['http://www.hbzkzx.com/Article/ShowClass.asp?ClassID=6']

        def parse(self, response):
            item = MyprojectItem()
            a = response.xpath('//a[@class="listA"]').extract()  #获取a标签list  a[0] unicode类型
            for i in a:
                s = i.encode("utf-8")
                t = re.findall(r'title\=\"[\s\S]*?\"', s)  #获取t列表      t[0] string类型
                u = re.findall(r'\/Article\/ShowArticle\.asp\?ArticleID\=\d{3}', s)  #获取u列表    u[0] string类型
                if t:  #筛选有标题的文章类型
                    for j, k in zip(t, u):
                        item['myurl'] = "http://www.hbzkzx.com" + k
                        item['mytitle'] = j[12:]
                        yield scrapy.Request(item['myurl'], meta={'item': item}, callback=self.parse_text)

        def parse_text(self, response):
            item = response.meta['item']
            p = response.xpath('//p').extract()  #获取p标签list  p[0] unicode类型
            temp = ""
            for i in p:
                s = i.encode("utf-8")
                temp_text = re.findall(r'>.*?<', s) #获取text列表      text[0] string类型
                for t in temp_text:
                    temp = temp + t
            text = re.sub(r'>\s*<', "", temp)  #文本初步加工
            text = re.sub(r'<>', "", text)
            text = re.sub(r'<', "", text)
            text = re.sub(r'>', "", text)
            item['mytext'] = text
            yield item


























# import scrapy
# import re
# import codecs
#
#
# class MyprojectItem(scrapy.Item):
#         mytitle = scrapy.Field()
#         mydata = scrapy.Field()
#         myurl = scrapy.Field()
#         pass
#
#
# class YuanSpider(scrapy.Spider):
#         name = "yuan"
#         start_urls = ['http://www.hbzkzx.com/Article/ShowClass.asp?ClassID=6']
#
#         def parse(self, response):
#             item = MyprojectItem()
#             title = ""
#             url = ""
#             a = response.xpath('//a[@class="listA"]').extract()
#             for i in a:
#                 t = re.findall(r'title\=\"[\s\S]*?\"', i)
#                 u = re.findall(r'\/Article\/ShowArticle\.asp\?ArticleID\=\d{3}', i)
#                 if t:
#                     if u:
#                         tt = re.findall(r'title\=\"[\s\S]*?\n', t[0])
#                         item['mytitle'] = tt[0][12:]
#                         title = title + tt[0][12:]
#                         url = url + "http://www.hbzkzx.com" + u[0] + '\n'
#                         item['myurl'] = "http://www.hbzkzx.com" + u[0]
#                         yield scrapy.Request("http://www.hbzkzx.com" + u[0], meta={'item': item}, callback=self.parse_yuan)
#                 # if t:
#                 #     if u:
#                 #         tt = re.findall(r'title\=\"[\s\S]*?\n', t[0])
#                 #         item['mytitle'] = tt[0][12:]
#                 #         title = title + tt[0][12:]
#                 #         url = url + "http://www.hbzkzx.com" + u[0] + '\n'
#                 #         item['myurl'] = "http://www.hbzkzx.com" + u[0]
#                 #         yield scrapy.Request("http://www.hbzkzx.com" + u[0], meta={'item': item}, callback=self.parse_yuan)
#             f = codecs.open('url.txt', 'w', encoding='utf-8')
#             f.write(url)
#             f.close()
#             ff = codecs.open('title.txt', 'w', encoding='utf-8')
#             ff.write(title)
#             ff.close()
#
#
#             # r = open('url.txt')
#             # while 1:
#             #     myurl = r.readline()
#             #     if not myurl:
#             #         break
#             #     else:
#             #         yield scrapy.Request(myurl, meta={'item': item}, callback=self.parse_yuan)
#
#         def parse_yuan(self, response):
#             item = response.meta['item']
#             print item['myurl']+"================"
#             text = ""
#             p = response.xpath('//p').extract()
#             for i in p:
#                 myp = i.encode("utf-8")
#                 data = re.findall(r'>.*?<', myp)
#                 for j in data:
#                     text = text + j
#                 text = re.sub(r'>\s*<', "", text)
#                 text = re.sub(r'<>', "", text)
#                 text = re.sub(r'<', "", text)
#                 text = re.sub(r'>', "", text)
#             item['mydata'] = text
#             f = open("tt", 'w')
#             f.write(text)
#             f.close()
#             yield item

               # print p[0].xpath('.//p/text()').extract()
            # ss = response.body
            # dr = re.compile(r'<[^>]+>', re.S)
            # dd = dr.sub('', ss)
            # print dd
            # soup = BeautifulSoup(response.body, 'html.parser')
            # print type(soup.p)
            # if soup:
            #     ss = str(soup.p.extract())
            #     print type(ss)
            #     print "======"
            # p = response.xpath('//p/text()').extract()
            # if p:
            #     print type(p[0])
            #     print "===="
            # reload(sys)
            # sys.setdefaultencoding('utf-8')
            # if p:
            #     f = codecs.open('data1.txt', 'w', encoding='utf-8')
            #     #u = p.decode('gbk')
            #     #a = u.encode('utf-8')
            #     f.write(p[0])
            #     f.close()
            # print "================="

            # print a[0]
            # print "======="
            # u = response.body.decode('gbk')
            # a[0] = u.decode('utf-8')
            # print a[0]

            # s = response.body
            # u = s.decode('gbk')
           #  mystr = u.encode('utf-8')
           # # print mystr
           #  a = re.findall(r'<a[\s\S]*</a>', mystr)
           #  print "======================================================"
           #  print type(a[0])
            # urls = re.findall(r'/Article/ShowArticle.asp\?ArticleID=\d{3}', mystr)
            # temp = set()
            # for url in urls:
            #     temp.add(url)
            # urls = []
            # for i in temp:
            #     urls.append("http://www.hbzkzx.com"+i)
            # print urls

        #     aa = []
        #     bb = []
        #     s = set(aa)
        #     ss = set(bb)
        #
       # reload(sys)
        #sys.setdefaultencoding('utf-8')
        #     for box in response.xpath('//a[@class="listA"]'):
        #         a = box.xpath('.//@href').extract()
        #         b = box.xpath('.//@title').extract()
        #
        #         if a:
        #             a = unicode(a, 'GBK').encode('UTF-8')
        #             s.add(str(a[0]))
        #         if b:
        #             b = unicode(b, 'GBK').encode('UTF-8')
        #             ss.add(str(b[0]))
        #     s.remove('/Article/ShowClass.asp?ClassID=35')
        #     for u in s:
        #         url = "http://www.hbzkzx.com"+u
        #         yield scrapy.Request(url, callback=self.parse_yuan)
        #
        # def parse_yuan(self, response):
        #     soup = BeautifulSoup(response.body, 'html.parser')
        #     p = str(soup.p)
        #     print "==========>>>"+p
        #     text = re.findall(r'>.*?<', p)
        #     print text

            # for i in s:
            #     item['url'] = "http://www.hbzkzx.com"+i
            #     yield scrapy.Request(url, callback=self.parse_yuan)
            # for i in ss:
            #     item['title'] = i

                    # stock = re.findall(r'/Article/ShowArticle.asp\?ArticleID=\d{3}', str(box))
                    # if stock:
                    #     print stock[0]
                #item['url'] = box.xpath('//a[@href="/Article/ShowArticle.asp?ArticleID=783]').extract()[0].strip()
                #url = "http://www.hbzkzx.com"+u
               # urls = urls+url+'/n'
                #print stock
                #yield scrapy.Request(url, callback=self.parse_yuan)
            # f = open('mytext', 'w')
            # f.write(urls)
            # f.close()
            # / Article / ShowArticle.asp\?ArticleID =\d{3}
            # for href in response.css('a::attr(href)').extract():
            #     try:
            #         stock = re.findall(r'/Article/ShowArticle.asp\?ArticleID=\d{3}', href)[0]
            #         url = "http://www.hbzkzx.com"+stock
            #         yield scrapy.Request(url, callback=self.parse_yuan)
            #     except:
            #         continue

        # def parse_yuan(self, response):
        #     text = ""
        #     soup = BeautifulSoup(response.body, 'html.parser')
        #     soup.xpath
        #     # for i in len(soup.p):
        #     #     try:
        #     #         temp = re.findall(r'>.*?<', soup.p[i])
        #     #         for j in range(len(temp)):
        #     #             if temp[j] > 2:
        #     #                 text = text + temp[j][1:-2]
        #     #     except:
        #     #         continue
        #     f = open('mytext', 'w')
        #     f.write(str(soup.p))
        #     f.close()