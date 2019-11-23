import pyodbc
class Mysqldb(object):
    def __init__(self):
        self.conn = pyodbc.connect('driver=SQL Server Native Client 10.0;server=ALEX_HUA;database=52Pojie;uid=sa;pwd=')
        #cursor.execute(sql)   %传递sql语句给数据库
    def save_data(self,database,title,link,time):
        cursor = self.conn.cursor()
        try:
            if "'" in str(title):
                return '跳过了一个标题'
            # 将数据存储到数据库
            cursor.execute("insert "+database+" (title,link,time) values('"+title+"','"+link+"','"+time+"')")
            # 需要使用commit提交变更
            self.conn.commit()
            return '数据存储成功...'
        except:
            cursor.execute("insert "+database+" (title,link,time) values('未知标题','"+link+"','"+time+"')")
            self.conn.commit()
            return  "存储 "+title+" 时出错\n "
    def delete_same_data(self,database):
        # 将数据库中重复的数据去除,只留下一个
        try:
            cursor = self.conn.cursor()
            cursor.execute("delete from "+database+" where link in (select link from "+database+" group by link having count(link) > 1)\
            and id not in (select min(id) from "+database+" group by link  having count(link)>1)")
            # 需要使用commit提交变更
            self.conn.commit()
            print('数据去重成功...')
        except Exception as e:
            print('数据去重复模块出错！\n'+e)
    def close_db(self):
        try:
            self.conn.close()
            print('成功关闭数据库...')
        except Exception as e:
            print('无法关闭数据库\n'+e)
