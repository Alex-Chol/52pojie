from openpyxl import Workbook
class MakeXlsx(object):
    def creatfile(self):  
        workbook = Workbook()
        workbook.save('将data.csv的数据导入此表.xlsx')
