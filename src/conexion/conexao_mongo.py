import pymongo

class ConexaoMongo:
    def __init__(self):
        self.host = "localhost"
        self.port = 27017
        self.client = None
        self.db = None  
    
    def __del__(self):
        if self.client:
            self.close()

    def connect(self):
        self.client = pymongo.MongoClient(f"mongodb://{self.host}:{self.port}/")
        self.db = self.client["banco_loja"]

        return self.db
    
    def close(self):
        if self.client:
            self.client.close()