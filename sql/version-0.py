#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql

con = pymysql.connect('localhost', 'master',
    '2547561', 'test1_db')

with con:

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()

    print("Database version: {}".format(version[0]))

