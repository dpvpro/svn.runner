#!/usr/bin/env python3
# -*- coding: utf-8

# copyright - https://gist.github.com/giumas/994e48d3c1cff45fbe93

import sqlite3
import logging
import time

initial_sql = """CREATE TABLE IF NOT EXISTS svn_action_log(
                    TimeStamp TEXT,
                    Source TEXT,
                    LogLevel INT,
                    LogLevelName TEXT,
                    Message TEXT,
                    Args TEXT,
                    Module TEXT,
                    FuncName TEXT,
                    LineNo INT,
                    Exception TEXT,
                    Process INT
               )"""

insertion_sql = """INSERT INTO svn_action_log(
                    TimeStamp,
                    Source,
                    LogLevel,
                    LogLevelName,
                    Message,
                    Args,
                    Module,
                    FuncName,
                    LineNo,
                    Exception,
                    Process
               )
               VALUES (
                    '%(dbtime)s',
                    '%(name)s',
                    %(levelno)d,
                    '%(levelname)s',
                    '%(msg)s',
                    '%(args)s',
                    '%(module)s',
                    '%(funcName)s',
                    %(lineno)d,
                    '%(exc_text)s',
                    %(process)d
               );
               """


class sqlitehandler(logging.Handler):
    """
    Thread-safe logging handler for SQLite.
    """

    def __init__(self, db='app.db'):
        logging.Handler.__init__(self)
        self.db = db
        conn = sqlite3.connect(self.db)
        conn.execute(initial_sql)
        conn.commit()

    def format_time(self, record):
        """
        Create a time stamp
        """
        record.dbtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))

    def emit(self, record):
        self.format(record)
        self.format_time(record)
        if record.exc_info:  # for exceptions
            record.exc_text = logging._defaultFormatter.formatException(record.exc_info)
        else:
            record.exc_text = ""

        # Insert the log record
        sql = insertion_sql % record.__dict__
        conn = sqlite3.connect(self.db)
        conn.execute(sql)
        conn.commit()  # not efficient, but hopefully thread-safe