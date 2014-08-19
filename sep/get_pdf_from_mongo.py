# coding=utf-8
from pymongo import MongoClient
import csv
import sys

db_name = sys.argv[1]
col_name = sys.argv[2]

aux = sys.argv[1]
client = MongoClient()
estados = client[db_name][col_name]

cursor = estados.find()

for x in cursor:
	for archivo in x['archivo']:
		print archivo[1]
			