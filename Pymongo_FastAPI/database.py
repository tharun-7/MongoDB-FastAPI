from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
# Select the database
db = client.MyDataBase
