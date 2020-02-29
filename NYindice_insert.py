import requests

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

SP5 = requests.get(
    'https://api.stlouisfed.org/fred/series/observations?series_id=SP500&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-01-01')
DOW = requests.get(
    'https://api.stlouisfed.org/fred/series/observations?series_id=DJIA&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-01-01')
NDQ = requests.get(
    'https://api.stlouisfed.org/fred/series/observations?series_id=NASDAQCOM&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-01-01')

Sjson = SP5.json()
Djson = DOW.json()
Njson = NDQ.json()

Svals = Sjson['observations']

data = [Sjson,Djson,Njson]
keyword = "observations"
count = 0
name_list = ["SP500","DOWJONES","NASDAQ"]
for item in data:
    row_data = item[keyword]

    for element in row_data:
        try:
            value = '{:,.2f}'.format(float(element['value']))
        except ValueError:
            value = element['value']
        data_type = str(name_list[count])
        result = {'type':data_type,'date': element['date'], 'value': value}
        db.indice.insert_one(result)
    count += 1
# for Sval in Svals:
#     try:
#         value = '{:,.2f}'.format(float(Sval['value']))
#     except ValueError:
#         value = Sval['value']
#     SP500 = {'date': Sval['date'], 'value': value}
#     db.SP500.insert_one(SP500)
#
# Dvals = Djson['observations']
#
# for Dval in Dvals:
#
#     try:
#         value = '{:,.2f}'.format(float(Dval['value']))
#     except ValueError:
#         value = Dval['value']
#
#     DOWJONES = {'date': Dval['date'], 'value': value}
#     db.DOWJONES.insert_one(DOWJONES)
#
#
# Nvals = Njson['observations']
#
# for Nval in Nvals:
#     try:
#         value = '{:,.2f}'.format(float(Nval['value']))
#     except ValueError:
#         value = Nval['value']
#
#     NASDAQ = {'date': Nval['date'], 'value': value}
#     db.NASDAQ.insert_one(NASDAQ)
