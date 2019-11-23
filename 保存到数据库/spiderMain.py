# 爬虫主文件 encoding = utf-8
# 
from downloader import Downloader
from htmlParser import HtmlParser
from mysqldb import Mysqldb
import random,time
class SpiderMain(object):
    def __init__(self):
        # 初始化程序
        self.download = Downloader()
        self.parser = HtmlParser()
        self.mysql = Mysqldb()

    def run(self,url,database):
        response = self.download.download(url)
        self.parser.parser(response,database)

if __name__ == "__main__":
    crawl = SpiderMain()
    page = 20
    print("================================")
    print(' A.原创发布区     B.精品软件区    ')
    print("================================")
    choice = input("选择你想要爬取的专区：")
    if choice == 'A':
        for i in range(1,page):
            url = 'https://www.52pojie.cn/forum-2-'+str(i)+'.html'
            crawl.run(url,'wuai_yuanchaung') # 请求url，解析并保存数据
            sleep = random.randint(2,10)
            print('爬取第'+str(i)+'完成，程序休息'+str(sleep)+'秒')
            time.sleep(sleep) # 程序睡眠
            if i != page-1:
                print('-----------------------------')
                print('          下一页              ')
                print('-----------------------------')
    if choice == 'B':
        for i in range(1,page):
            url = 'https://www.52pojie.cn/forum-16-'+str(i)+'.html'
            crawl.run(url,'wuai_ruanjian') # 请求url，解析并保存数据
            sleep = random.randint(2,10)
            print('爬取第'+str(i)+'完成，程序休息'+str(sleep)+'秒')
            time.sleep(sleep) # 程序睡眠
            if i != page-1:
                print('-----------------------------')
                print('          下一页              ')
                print('-----------------------------')
    if choice == 'A':
        crawl.mysql.delete_same_data('wuai_yuanchaung') # 数据去重
    if choice == 'B':
        crawl.mysql.delete_same_data('wuai_ruanjian') # 数据去重
    crawl.mysql.close_db() # 关闭数据库
    print('程序运行完毕')

    # 精品软件区
    # https://www.52pojie.cn/forum-16-1.html
