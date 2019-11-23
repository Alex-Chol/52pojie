import requests

class Downloader(object):
    def download(self,url):
        if url is None:
            return None
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Host':'www.52pojie.cn',
            'Referer':'https://www.52pojie.cn/',
            'Upgrade-Insecure-Requests':'1'}
        r = requests.get(url,headers=headers)
        if r.status_code == 200:
            return r.text
        return None