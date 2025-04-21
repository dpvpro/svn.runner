#!/usr/bin/env python3
# -*- coding: utf-8

import subprocess, logging, time, os, re, datetime, traceback
import tozip, sqlite_handler


class svn_runner(object):
    def __init__(self, logger=None):

        self.db_file = "test.db"
        self.path_work_dir = "/tmp/"
        self.path_url_file = "svn_urls.txt"
        self.name_arhive = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "-svnarhive.zip"
        self.path_archive =  "/tmp/"

        # set working catalog
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        # print (os.getcwd())

        # set logger handler
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # sqlite handler
        sh = sqlite_handler.sqlitehandler(db=self.db_file)
        sh.setLevel(logging.INFO)
        self.logger.addHandler(sh)

        # check instaslled soft
        p = subprocess.run("which svn", stdout=subprocess.PIPE, shell=True)
        if p.returncode:
            self.logger.info('No svn installed. Please install', exc_info=True)
            raise SystemExit()
        p = subprocess.run("which sqlite3", stdout=subprocess.PIPE, shell=True)
        if p.returncode:
            self.logger.info('No sqlite3 installed. Please install.', exc_info=True)
            raise SystemExit()

    def read_file(self):
        with open(self.path_url_file, 'r') as svn_urls:
            self.url_items = [line.strip() for line in svn_urls]
        self.logger.info("List urls - " + ', '.join(self.url_items))
    
    def download_svn(self):
        self.normalized_url_items = []
        for item in self.url_items:
            # pass strings with comment
            if re.search('#', item):
                continue
            # print (item)
            parts = re.findall(r'\w+', item)
            # print (parts)
            normalized_url_item = "-".join(parts)
            self.normalized_url_items.append(normalized_url_item)
            p = subprocess.run(("svn checkout "+ item + " " + self.path_work_dir + normalized_url_item), stdout=subprocess.PIPE, shell=True)
            if p.returncode:
                self.logger.info('Checkout svn repo interrupted', exc_info=True)
                raise SystemExit()
        self.logger.info("List normalized urls - " + ', '.join(self.normalized_url_items))

    def pack_svn(self):
        # os.chdir(os.path.dirname(os.path.realpath(__file__)))
        # print (os.getcwd())
        try:
            arhive = tozip.ziputilities()
            for item in self.normalized_url_items:
                arhive.tozip(self.path_archive + item, self.path_archive + self.name_arhive)
                self.logger.info("Zip file " + item +  ".zip created ")

        except Exception as e:
            self.logger.info("Zip files interrupted with error: \n" + traceback.format_exc())



def main():

    svn_instance = svn_runner()
    svn_instance.read_file()
    svn_instance.download_svn()
    svn_instance.pack_svn()


if __name__ == '__main__':
    main()