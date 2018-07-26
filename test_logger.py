#!/usr/bin/env python3
# -*- coding: utf-8

# copyright - https://gist.github.com/giumas/994e48d3c1cff45fbe93

import logging, time

from sqlite_handler import SQLiteHandler 


def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # sqlite handler
    sh = SQLiteHandler(db="test.db")
    sh.setLevel(logging.INFO)
    # logging.getLogger("main").addHandler(sh)
    logger.addHandler(sh)

    # test
    logger.info('Start')
    time.sleep(1)
    logger.info('End')

if __name__ == '__main__':
    main()