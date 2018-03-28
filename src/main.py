#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from downloader import Downloader
import sys, getopt

class Main():
    def __init__(self,argv):
        self.path = None
        self.url_base = ""

        try:
            opts, args = getopt.getopt(argv,"hu:d:", ["help", "url", "dir"])

        except getopt.GetoptError as error:
            print(error)
            self.show_help()
            exit(2)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                self.show_help()
                exit(0)
            elif opt in ("-u", "--url"):
                self.url_base = arg
            elif opt in ("-d", "--dir"):
                self.path = arg

    def run(self):
        down = Downloader()
        down.get_url(self.url_base)
        down.get_file(self.path)
        
    def show_help(self):
        print("-h | --help \t\t\t Shows this.")
        print("-u | --url <Some URL>\t\t Defines the modpack link to download.")
        print("-d | --dir <Some Directory>\t Defines the directory to save the modpack meta-data.")

if __name__ == "__main__":
    app = Main(sys.argv[1:])
    app.run()
    exit(0)

