from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


DB = db.DOWJONES.find()[0]
#어차피 다 가져와서 API로 뿌릴거라면 굳이 for문을 쓰지 않아도 됨
Sdata = DB['S&P']
Ddata = DB['DOW']
Ndata = DB['NDQ']

print (Ddata)

#print(DB['S&P'][0]['date'],DB['S&P'][0]['value'])
#print(DB['DOW'][0]['date'])

#for Sval in Svals:


