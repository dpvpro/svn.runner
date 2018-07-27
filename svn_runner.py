#!/usr/bin/env python3
# -*- coding: utf-8

import subprocess, logging, time, os, re

class svn_runner(object):
    def __init__(self):
        self.path_url_file = "svn_urls.txt"
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
    
    def download_links(self):
        self.normalized_url_items = []
        for item in self.url_items:
            if re.search('#', item):
                continue
            else:
                # print (item)
                parts = re.findall('\w+', item)
                # print (parts)
                self.normalized_url_items.append("-".join(parts))
        print (self.normalized_url_items)




def main():
    svn_instance = svn_runner()
    # print ("Url_file -", x.path_url_file)
    svn_instance.read_file()
    svn_instance.download_links()


if __name__ == '__main__':
    main()