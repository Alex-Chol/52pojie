from lxml import etree
from saveData import SaveData
import csv
class HtmlParser(object):
    def __init__(self):
        self.sa = SaveData()
    def parser(self,response,filename):
        html = etree.HTML(response,etree.HTMLParser())
        try:
            data = html.xpath("//tbody")
            for i in data:
                title = i.xpath(".//a[@class='s xst']/text()")
                l = i.xpath(".//a[@class='s xst']/@href") # 链接的部分内容
                time = i.xpath(".//td[@class='by']/em/span/text()")
                power = i.xpath(".//span[@class='xw1']/text()")
                if len(title) != 0:
                    # 构建完整的链接
                    link = 'https://www.52pojie.cn/'+l[0]
                    print(title[0])
                    print(link)
                    print(time[0])
			        # 如果需要阅读权限则不显示该链接,不保存数据
                    if len(power) == 0:
                        with open(filename+'.csv','a+',encoding='utf-8-sig',newline='') as f:
                            w = csv.writer(f)
                            # 使用savedata方法保存数据到csv文件中
                            self.sa.savedata(w,title[0],link,time[0])
                        print('------------------------------')
        except Exception as e:
            print(e)

