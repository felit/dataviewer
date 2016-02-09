#-*- coding:utf8-*-
import pymongo
from datasource import DataSource
class MetaData():
    def __init__(self):
        host,port,_,_=DataSource().get_mongo()
        self.datasource = pymongo.MongoClient(host,port)
        self.db = self.datasource.dataviewer
    def insert_datasource(self,datasource):
        self.db.datasource.insert_one(datasource)
    def get_all_datasource(self):
        result = []
        for item in self.db.datasource.find():
            result.append(item)
        return result

if __name__=='__main__':

    MetaData().insert_datasource({'type':'postgres','title':'小雅线上数据库','url':'jdbc:postgresql://localhost/xiaoya','username':'trace','password':'trace','remark':'测试'})
    print MetaData().get_all_datasource()