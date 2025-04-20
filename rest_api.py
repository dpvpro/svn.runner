#!/usr/bin/env python3
# -*- coding: utf-8

# sudo -H pip3 install flask flask_restful sqlalchemy 

import os
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine, text
from json import dumps


# set working catalog
os.chdir(os.path.dirname(os.path.realpath(__file__)))

db_connect = create_engine("sqlite:///test.db")
app = Flask(__name__)
api = Api(app)

class ListByPeriod(Resource):
    def get(self, from_date, till_date):
        conn = db_connect.connect() # connect to database
        query = conn.execute(text("select * from svn_action_log WHERE TimeStamp >= '{} 00:00' and TimeStamp <= '{} 23:59';".format(from_date, till_date)))
        return {'Transaction for period ': query.fetchall()}

# example url - http://127.0.0.1:5002/listbyperiod/2018-07-28/2018-07-28
api.add_resource(ListByPeriod, '/listbyperiod/<from_date>/<till_date>')

if __name__ == '__main__':
     app.run(port=5002)