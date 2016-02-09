import yaml
import os
current_dir = os.path.split(os.path.realpath(__file__))[0]
class DataSource():
    def __init__(self):
        self.config = yaml.load(file('%s/datasource.yaml'%current_dir))
        self.meta_data= self.config['meta_data']
        print self.config

    def get_mongo(self):
        return self.meta_data['host'],self.meta_data['port'],self.meta_data['username'],self.meta_data['password']

if __name__=='__main__':
    DataSource()
    print DataSource().get_mongo()