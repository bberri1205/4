
from pymongo import MongoClient

c=MongoClient("lisa.stuy.edu",27017);
collie=c.test.restaurants

def find_boroughs(borough):
   '''
   prints and returns all restaurants in a specified borough.
   '''
   dictionary = collie.find({"borough":borough})
   for each in dictionary:
      print each["name"]
   return dictionary

def by_zip(code):
   '''
   prints and returns all restaurants in a specified zip code.
   '''
   dictionary_zip=collie.find({"address.zipcode":code})
   for each in dictionary_zip:
      print each["name"]
   return dictionary_zip

def by_zip_grade(zc,grade):
   '''
   prints and returns all restaurants in a specified zipcode and with a specified grade.
   '''
   dictionary=collie.find({"$and":[{"address.zipcode":zc},{"grades.grade":grade}]})
   for each in dictionary:
      print each["name"]
   return dictionary

def by_zip_score(zc,threshold):
   '''
   prints and returns all restaurants in a specified zip code
   with a score below a specified threshold
   '''
   dictionary=collie.find({"$and":[{"address.zipcode":zc},{"grades.score":{"$lt":threshold}}]})
   for each in dictionary:
       print each["name"]
   return dictionary

'''
def Something more clever:

'''

print "=====================BOROUGH==================\n"
find_boroughs("Manhattan")
print "=====================ZIP==================\n"
by_zip('11218')
print "=====================ZG==================\n"
by_zip_grade("11218","A")
print "===================ZS===================\n"
by_zip_score("11218",4)
