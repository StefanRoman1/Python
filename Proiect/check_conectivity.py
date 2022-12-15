import argparse
import requests
import time
import psycopg2
import pymongo
import elasticsearch
import warnings
import ftplib
warnings.filterwarnings("ignore")

class check_conectivity :
    def read_data(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-url", help="url to check")
        parser.add_argument("-ftp", help="ftp url to check")
        parser.add_argument("-mongodb", help="mongodb URI to check")
        parser.add_argument("-postgresql", help="postgresql URI to check")
        parser.add_argument("-elasticsearch", help="elasticSearch URI to check")
        parser.add_argument("-time", help="time interval to check the connection in minutes")
        args = parser.parse_args()
        self.link = args.url or args.mongodb or args.postgresql or args.elasticsearch or args.ftp
        self.type = args.url and "-url" or args.mongodb and "-mongodb" or args.postgresql and "-postgresql" or args.elasticsearch and "-elasticsearch" or args.ftp and "-ftp"
        self.x = float(args.time) if args.time else 0

    def check(self):
        if self.type == "-url":
            self.check_http()
        elif self.type == "-ftp":
            self.check_ftp()
        elif self.type == "-mongodb":
            self.check_mongo()
        elif self.type == "-postgresql":
            self.check_postgresql()
        elif self.type == "-elasticsearch":
            self.check_elasticSearch()

    def check_http(self):
        try:
            response = requests.get(self.link)
            print(f'HTTP Status Code: {response.status_code}, {response.reason}')
            print(f'Response Time: {response.elapsed.total_seconds()}')
        except:
            print(f'Connection could not be established for {self.link}')

    def check_ftp(self):
            try:
                start = time.time()
                ftp = ftplib.FTP(self.link)
                ftp.login()
                ftp.quit()
                end = time.time()
                print("Connection Successful")
                print(f'Response Time: {end-start}')
            except:
                print(f'Connection could not be established for {self.link}')

    def check_postgresql(self):
            try:
                start = time.time()
                conn = psycopg2.connect(self.link)
                cur = conn.cursor()
                cur.execute("SELECT version();")
                record = cur.fetchone()
                end = time.time()
                print("You are connected to - ", record,"\n")
                print("Connection Successful")
                print(f'Response Time: {end-start}')
                cur.close()
            except (Exception, psycopg2.Error) as error :
                print (f'Connection could not be established for {self.link}')

    def check_mongo(self):
        try:
            start = time.time()
            myclient = pymongo.MongoClient(self.link, serverSelectionTimeoutMS=3000)
            myclient.server_info()
            end = time.time()
            print("Connection Successful")
            print(f'Response Time: {end-start}')
        except:
            print(f'Connection could not be established for {self.link }')

    def check_elasticSearch(self):
        try:
            start = time.time()
            es = elasticsearch.Elasticsearch(self.link, timeout=3)
            es.info()
            end = time.time()
            print("Connection Successful")
            print(f'Response Time: {end-start}')
        except:
            print(f'Connection could not be established for {self.link }')

if __name__ == "__main__":
    project = check_conectivity()
    project.read_data()
    if(project.x == 0):
        project.check()
    else:
        while True:
            project.check()
            time.sleep(project.x*60)