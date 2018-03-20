import requests
from clint.textui import progress
import lxml.html
import os
class Downloader():
    def __init__(self):
        self.url = ''
        pass
    def get_url(self, base_url):
        if base_url == '':
           return 1
        url_part = base_url + '/download?client=n'
        dom = lxml.html.fromstring(requests.get(url_part).content)
        url_final = [x for x in dom.xpath('//a/@href') if 'file' in x]
        self.url = 'https://www.curseforge.com' + url_final[0]
        self.filename = base_url
        self.filename = self.filename.replace("https://www.curseforge.com/minecraft/modpacks/", "")
        self.filename = self.filename + ".zip"
    
    def get_file(self, path=None):
        self.temp_file = requests.get(self.url, stream=True)
        if path == None:
            self.path = os.path.join(os.getcwd(), self.filename)
        else:
            self.path = os.path.join(path, self.filename)
        with open(self.path, 'wb') as out:
            total_length = int(self.temp_file.headers.get('content-length'))
            for chunk in progress.bar(self.temp_file.iter_content
                                     (chunk_size=1024),
                                     expected_size=(float(total_length/1024)) + 1,
                                     label=self.filename): 
                if chunk:
                    out.write(chunk)
                    out.flush()
