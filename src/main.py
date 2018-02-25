#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from downloader import Downloader
import sys

class Main():
    def __init__(self):
        self.args = sys.argv
        if len(self.args) < 2:
            print("Faltam argumentos!")
            exit(0)
        elif len(self.args) == 2:
            self.url_base = str(sys.argv[1])
            self.path = None
        else: 
            self.url_base = str(sys.argv[1])
            self.path = str(sys.argv[2])

    def run(self):
        print(self.args)
        down = Downloader()
        down.get_url(self.url_base)
        down.get_file(self.path)
        print(down.url)
if __name__ == "__main__":
    app = Main()
    app.run()

