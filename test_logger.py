#!/usr/bin/env python3
# -*- coding: utf-8

# copyright - https://gist.github.com/giumas/994e48d3c1cff45fbe93

import logging, time, os, sys
import sqlite_handler

def main():
    # set working catalog
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # sqlite handler
    sh = sqlite_handler.sqlitehandler(db="test.db")
    sh.setLevel(logging.INFO)
    # logging.getLogger("main").addHandler(sh)
    logger.addHandler(sh)

    # test
    logger.info('Start')
    time.sleep(1)
    # print (sys.stdout)
    # logger.info("sys.stdout")
    logger.info('End')

if __name__ == '__main__':
    main()