# -*- coding:utf-8 -*-
class DataAdapter():
    # 数据适配器
    def adapter(self,values):
        pass
class TableAdapter(DataAdapter):
    def adapter(self,values,default=0):
        dim1,dim2 = set(),set()
        for d1,d2,v in values:
            dim1.add(d1)
            dim2.add(d2)
        print dim1
        print dim2

