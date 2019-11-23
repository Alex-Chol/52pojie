from downloader import Downloader
from htmlParser import HtmlParser
from saveData import SaveData
from openpyxl import Workbook
from choice import Choice
import random,time,os

class SpiderMain(object):
    def __init__(self):
        # 初始化程序 
        self.download = Downloader()
        self.parser = HtmlParser()
        self.save = SaveData()
        self.workbook = Workbook()
        self.ch = Choice()
        print('初始化完成...')
    def run(self):
        while True:
            try:
                p = int(input('想要爬多少页的数据？'+'\n'))
                break
            except ValueError:
                print('输入错误！请输入数字')
        page = p+1
        print("================================")
        print(' A.原创发布区     B.精品软件区    ')
        print(' C.脱壳破解区     D.移动安全区    ')
        print(' E.病毒分析区     F.编程语言区    ')
        print(' G.软件调试区     H.动画发布区    ')
        print(' I.逆向资源区     J.安全工具区    ')
        print(' K.招聘求职区                    ')
        print("================================")
        while True:
            choice = input("选择爬取的专区，输入 Q 退出程序(输入的字母必须大写)：")
            half_url,name = self.ch.make_the_arrg(choice)
            if name != 'Error':
                break
        print(half_url+'\n'+name)
        self.save.createfile(name)
        for i in range(1,page):
            url = half_url+str(i)+'.html'
            response = self.download.download(url)
            self.parser.parser(response,name)
            sleep = random.randint(2,10) 
            print('爬取第'+str(i)+'页完成，程序休息'+str(sleep)+'秒')
            time.sleep(sleep) # 程序睡眠
            if i != page-1:
                print('-----------------------------')
                print('          下一页              ')
                print('-----------------------------')
        print('数据写入完成，正在进行数据去重...')
        self.save.delete_same_data()
        try:
            self.workbook.save('将csv的数据导入此表.xlsx')
        except:
            print('创建xlsx文件失败，请手动创建')
        print('程序运行完毕')

if __name__ == "__main__":
    crawl = SpiderMain()
    crawl.run()
    input('数据文件保存在本程序当前目录下,按任意键结束...')
