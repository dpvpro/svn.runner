#!/usr/bin/env python3
# -*- coding: utf-8

import subprocess, logging, time, os, re, datetime
import tozip

class svn_runner(object):
    def __init__(self):

        self.path_work_dir = "/tmp/"
        self.path_url_file = "svn_urls.txt"
        self.name_arhive = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "-SvnArhive"
        self.path_archive = "/tmp/"

        # set working catalog
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        print (os.getcwd())

        p = subprocess.run("which svn", stdout=subprocess.PIPE, shell=True)
        if p.returncode:
            raise SystemExit('No svn installed. Please install')
        p = subprocess.run("which sqlite3", stdout=subprocess.PIPE, shell=True)
        if p.returncode:
            raise SystemExit('No sqlite3 installed. Please install.')
        # print (self.path_url_file)

    def read_file(self):
        with open(self.path_url_file, 'r') as svn_urls:
            self.url_items = [line.strip() for line in svn_urls]
            # print (self.url_items)
    
    def download_svn(self):
        self.normalized_url_items = []
        for item in self.url_items:
            # pass strings with comment
            if re.search('#', item):
                continue
            # print (item)
            parts = re.findall('\w+', item)
            # print (parts)
            normalized_url_item = "-".join(parts)
            self.normalized_url_items.append(normalized_url_item)
            p = subprocess.run(("svn checkout "+ item + " " + self.path_work_dir + normalized_url_item), stdout=subprocess.PIPE, shell=True)
            if p.returncode:
                raise SystemExit('Checkout svn repo iterrupted')
        print (self.normalized_url_items)

    def pack_svn(self):
        # os.chdir(os.path.dirname(os.path.realpath(__file__)))
        print (os.getcwd())
        arhive = tozip.ziputilities()
        for item in self.normalized_url_items:
            arhive.tozip(self.path_archive+item, self.name_arhive)
        


        




def main():
    svn_instance = svn_runner()
    # print ("Url_file -", x.path_url_file)
    svn_instance.read_file()
    svn_instance.download_svn()
    svn_instance.pack_svn()


if __name__ == '__main__':
    main()