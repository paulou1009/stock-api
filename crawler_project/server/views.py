import requests
import datetime
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import QueryDict

#from pymongo.connection import Connection
#db = Connection().sms

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test_database
db.test_collection.drop()
collection = db.test_collection
collection.drop



def index(request):

  print request

  print request.body
  print request.scheme
  print request.path
  print request.path_info

  query = QueryDict(request.GET.urlencode())

  print query

  print query["ert"] == "234"

  url = "https://www.google.com/finance/getprices?q=AAPL&i=60&p=1d&f=d,o,h,l,c,v"
  symbol = "AAPL"
  response = requests.get(url)
  tokenString = response.text.split("\n")
  
  ts_raw = tokenString[7].split(",")[0]
  ts = ts_raw[1:]
  utc_dt = datetime.datetime.utcfromtimestamp(float(ts))
  index = 0

  return HttpResponse(response)
  """
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
  """

