import argparse

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

if __name__ == "__main__":
    project = check_conectivity()
    project.read_data()