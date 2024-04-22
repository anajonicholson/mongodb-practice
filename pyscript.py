#!/usr/bin/env python3

from pymongo import MongoClient, errors
import os

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/fhy9gs"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
db = client["fhy9gs"]
collection = db["animals"]

animals = [
    {"name": "Lion", "color": "Yellow", "habitat": "Savannah"},
    {"name": "Elephant", "color": "Gray", "habitat": "Grasslands"},
    {"name": "Tiger", "color": "Orange Striped", "habitat": "Jungle"},
    {"name": "Giraffe", "color": "Brown Spotted", "habitat": "Arid regions"},
    {"name": "Penguin", "color": "Black and White", "habitat": "Antarctica"}
]
collection.insert_many(animals)

result = collection.find().limit(3)
for animal in result:
    print(animal)
