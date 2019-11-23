from lxml import etree
from mysqldb import Mysqldb
class HtmlParser(object):
    def __init__(self):
        self.mysql = Mysqldb()
    def parser(self,response,database):
        html = etree.HTML(response,etree.HTMLParser())
        try:
            data = html.xpath("//tbody")
            for i in data:
                title = i.xpath(".//a[@class='s xst']/text()")
                l = i.xpath(".//a[@class='s xst']/@href")
                time = i.xpath(".//td[@class='by']/em/span/text()")
                power = i.xpath(".//span[@class='xw1']/text()")
                if len(title) != 0:
                    # 构建完整的链接
                    link = 'https://www.52pojie.cn/'+l[0]
                    print(title[0])
                    print(link)
                    print(time)
			        # 如果需要阅读权限则不显示该链接，不加入到数据库
                    if len(power) != 0:
                        # 使用save_data方法保存数据到数据库中
                        sq = self.mysql.save_data(database,title[0],link,time[0])
                        print(sq)
                        print('-------------------------------')
        except Exception as e:
            print('分析模块出错\n'+e)

