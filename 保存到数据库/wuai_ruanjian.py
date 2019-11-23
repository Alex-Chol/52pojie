import requests,time,random
from lxml import etree

class Wuai_ruanjian(object):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}
	def run(self):
		crawl_page = 3
		for i in range(1,crawl_page):
			url = 'https://www.52pojie.cn/forum-16-'+str(i)+'.html'
			self.get_data(url)
			if i != crawl_page-1:
				print('-----------------------------')
				print('          下一页              ')
				print('-----------------------------')
			time.sleep(random.randint(1,5))

	def get_data(self,url):
		r = requests.get(url,headers=self.headers)
		html = etree.HTML(r.text)
		data = html.xpath("//a[@class='s xst']")
		for each in data:
			title = each.xpath("./text()")
			print(title[0])
			# 添加一个功能：
			# 如果需要阅读权限则不显示该链接，不加入到数据库
			link = each.xpath("./@href")
			link = 'https://www.52pojie.cn/'+link[0]
			print(link)
			print('==================')
		
if __name__=='__main__':
	spider = Wuai_ruanjian()
	spider.run()