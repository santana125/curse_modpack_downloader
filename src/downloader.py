import requests
from clint.textui import progress
import lxml.html
class Downloader():
    def __init__(self):
        self.url = ''
        pass
    def get_url(self, base_url):
        if base_url == '':
           print("Url não encontrada !")
           return 1
        url_part = base_url + '/download?client=n'
        dom = lxml.html.fromstring(requests.get(url_part).content)
        url_final = [x for x in dom.xpath('//a/@href') if 'file' in x]
        self.url = 'https://www.curseforge.com' + url_final[0]
        self.filename = base_url
        self.filename = self.filename.replace("https://www.curseforge.com/minecraft/modpacks/", "")
    def get_file(self):
        self.temp_file = requests.get(self.url, stream=True)
        self.path = '/home/gustavo/Projects/'+ self.filename +'.zip'
        with open(self.path, 'wb') as out:
            total_length = int(self.temp_file.headers.get('content-length'))
            for chunk in progress.bar(self.temp_file.iter_content
                                     (chunk_size=1024),
                                     expected_size=(total_length/1024) + 1): 
                if chunk:
                    out.write(chunk)
                    out.flush()
