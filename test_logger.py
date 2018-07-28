#!/usr/bin/env python3
# -*- coding: utf-8

# copyright - https://gist.github.com/giumas/994e48d3c1cff45fbe93

import logging, time, sqlite_handler, os

# from sqlite_handler import SQLiteHandler 


def main():
    # set working catalog
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # sqlite handler
    sh = sqlite_handler.SQLiteHandler(db="test.db")
    sh.setLevel(logging.INFO)
    # logging.getLogger("main").addHandler(sh)
    logger.addHandler(sh)

    # test
    logger.info('Start')
    time.sleep(1)
    logger.info('End')

if __name__ == '__main__':
    main()