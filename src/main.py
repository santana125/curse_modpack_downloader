#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from downloader import Downloader
import sys

class Main():
    def __init__(self):
        self.url_base = str(sys.argv[1])
    def run(self):
        down = Downloader()
        down.get_url(self.url_base)
        down.get_file()
if __name__ == "__main__":
    app = Main()
    app.run()

