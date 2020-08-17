#!/bin/python3

#import mysql.connector
import pymysql

#mydb = mysql.connector.connect (
mydb = pymysql.connect(
    host="localhost",
    user="master",
    passwd="2547561"
    )
print(mydb)

