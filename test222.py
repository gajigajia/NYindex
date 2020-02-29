from flask import Flask, render_template, jsonify
from pymongo import MongoClient

# DB import를 여기다 해야한다
client = MongoClient('localhost', 27017)

index = client.dbsparta.indice.find()
rawdata = []
test_dict = {}
for item in index:
    rawdata.append(item)

print(type(rawdata))
test_dict = rawdata
print(type(test_dict))
# FLASK는 list형은 불러오지 않으므로 jsonify를 사용하여 dict형으로 해야함. type(data)하면 data가 무슨 데이터타입인지 보여줌
print(rawdata)
