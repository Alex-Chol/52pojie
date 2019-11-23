import csv
from os import path
import pandas as pd

class SaveData(object):
    def createfile(self,name):
        self.file_name = name+'.csv'
        # 判断文件是否存在
        isExists = path.exists(self.file_name)
        if not isExists:
            # 创建文件
            with open(self.file_name,'a+',encoding='utf-8-sig',newline='',errors='ignore') as f:
                w = csv.writer(f)
                w.writerow(['title','link','time'])
        else:
            with open(self.file_name,'a+',encoding='utf-8-sig',newline='',errors='ignore') as f:
                w = csv.writer(f)

    def savedata(self,writer,title,link,time):
        try:
            writer.writerow([title,link,time])
        except UnicodeEncodeError: 
            writer.writerow(['Error','None','None'])

    def delete_same_data(self):
        # 数据去重
        df = pd.read_csv(self.file_name,encoding='utf-8-sig')
        fe = df.drop_duplicates(subset='link',keep='last')
        fe.to_csv(self.file_name,index = False)
        print('数据去重成功...')

