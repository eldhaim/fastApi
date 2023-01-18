from pymongo import MongoClient

passw = 'frdsxDLu8RWhhMZP'
usr = 'firstApiFastApi'
client = MongoClient(f"mongodb+srv://{usr}:{passw}@fastapidb.6hlxv7b.mongodb.net/?retryWrites=true&w=majority")
db = client.FastApiDB
collection_name = db["Users"]
