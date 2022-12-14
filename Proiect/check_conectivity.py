import argparse
import requests
import time
import psycopg2
import pymongo

class check_conectivity :
    def read_data(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-url", help="url to check")
        parser.add_argument("-mongodb", help="mongodb url to check")
        parser.add_argument("-postgresql", help="postgresql url to check")
        parser.add_argument("-elasticsearch", help="elasticSearch url to check")
        parser.add_argument("-x", help="time interval to check the connection")
        args = parser.parse_args()
        self.link = args.url or args.mongodb or args.postgresql or args.elasticsearch
        self.type = args.url and "-url" or args.mongodb and "-mongodb" or args.postgresql and "-postgresql" or args.elasticsearch and "-elasticsearch"
        self.x = int(args.x) if args.x else 0

    def check(self):
        if self.type.lower() == "-url":
            self.check_http()
        elif self.type.lower() == "-mongodb":
            self.check_mongo()
        elif self.type.lower() == "-postgresql":
            self.check_postgresql()
        elif self.type.lower() == "-elasticsearch":
            self.check_elasticSearch()

    def check_http(self):
        try:
            response = requests.get(self.link)
            print(f'HTTP Status Code: {response.status_code}, {response.reason}')
            print(f'Response Time: {response.elapsed.total_seconds()}')
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

if __name__ == "__main__":
    project = check_conectivity()
    project.read_data()
    project.check()