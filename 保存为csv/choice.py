import os
class Choice(object):
    def make_the_arrg(self,arrg):
        true_arrg = ['A','B','C','D','E','F','G','H','I','J','K','Q']
        if arrg not in true_arrg:
            print('输入有误,请重新输入')
            return 'Error','Error'
        if arrg == 'A':
            # 原创发布区 https://www.52pojie.cn/forum-2-1.html
            link = 'https://www.52pojie.cn/forum-2-'
            ti = '原创发布区'
        if arrg == 'B':
            # 精品软件区 https://www.52pojie.cn/forum-16-1.html
            link = 'https://www.52pojie.cn/forum-16-'
            ti = '精品软件区'
        if arrg == 'C':
            # 脱壳破解区 https://www.52pojie.cn/forum-5-1.html
            link = 'https://www.52pojie.cn/forum-5-'
            ti = '脱壳破解区'
        if arrg == 'D':
            # 移动安全区 https://www.52pojie.cn/forum-65-1.html
            link = 'https://www.52pojie.cn/forum-65-'
            ti = '移动安全区'
        if arrg == 'E':
            # 病毒分析区 https://www.52pojie.cn/forum-32-1.html
            link = 'https://www.52pojie.cn/forum-32-'
            ti = '病毒分析区'
        if arrg == 'F':
            # 编程语言区 https://www.52pojie.cn/forum-24-1.html
            link = 'https://www.52pojie.cn/forum-24-'
            ti = '编程语言区'
        if arrg == 'G':
            # 软件调试区 https://www.52pojie.cn/forum-59-1.html
            link = 'https://www.52pojie.cn/forum-59-'
            ti = '软件调试区'
        if arrg == 'H':
            # 动画发布区 https://www.52pojie.cn/forum-6-1.html
            link = 'https://www.52pojie.cn/forum-6-'
            ti = '动画发布区'
        if arrg == 'I':
            # 逆向资源区 https://www.52pojie.cn/forum-4-1.html
            link = 'https://www.52pojie.cn/forum-4-'
            ti = '逆向资源区'
        if arrg == 'J':
            # 安全工具区 https://www.52pojie.cn/forum-41-1.html
            link = 'https://www.52pojie.cn/forum-41-'
            ti = '安全工具区'
        if arrg == 'K':
            # 招聘求职区 https://www.52pojie.cn/forum-39-1.html
            link = 'https://www.52pojie.cn/forum-39-'
            ti = '招聘求职区'
        if arrg == 'Q':
            print('程序结束')
            os._exit(0)
        return link,ti