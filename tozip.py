#!/usr/bin/env python3
# -*- coding: utf-8

import zipfile
import os


class ziputilities(object):

    def tozip(self, file, filename):
        zip_file = zipfile.ZipFile(filename, 'a')
        if os.path.isfile(file):
            zip_file.write(file)
        else:
            self.addfoldertozip(zip_file, file)
        zip_file.close()

    def addfoldertozip(self, zip_file, folder): 
        for file in os.listdir(folder):
            full_path = os.path.join(folder, file)
            if os.path.isfile(full_path):
                print ('File added: ' + str(full_path))
                zip_file.write(full_path)
            elif os.path.isdir(full_path):
                # print ('Entering folder: ' + str(full_path))
                self.addfoldertozip(zip_file, full_path)

def main():
    utilities = ziputilities()
    filename = 'temp.zip'
    directory = '/tmp/http-anonsvn-icesoft-org-repo-icefaces3-trunk-icefaces'
    utilities.tozip(directory, filename)

if __name__ == '__main__':
    main()
