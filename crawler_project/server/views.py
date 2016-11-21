from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#from pymongo.connection import Connection
#db = Connection().sms

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test_database
db.test_collection.drop()
collection = db.test_collection
collection.drop

def index(request):

    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"]
            }

    print post
    collection.insert_one(post)
    print "One thing inserted..."


    post2 = collection.find_one()
    print "Read it back..."
    print post2
    

    return HttpResponse(post2["text"])

