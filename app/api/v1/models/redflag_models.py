from flask_restful import reqparse
import datetime
from flask import jsonify,json,request, make_response
Redflags=[]
class Locate():

    def __init__(self):
        self.db = Redflags

    def new(self):
        #self.parser = reqparse.RequestParser()
        #args = self.parser.parse_args()
        Redflag = {
            "id":len(self.db)+1,
            "createdon":datetime.datetime.now(),
            "Title":request.get_json()["Title"],
            "type":"Redflag",
            "Createdby":request.get_json()["Createdby"],
            "Description":request.get_json()["Description"],
            "Location":request.get_json()["Location"],
            "Status":"Resolved",
            "video":request.get_json()["video"],
            "image":request.get_json()["image"]
     
        }
        resp=self.db.append(Redflag)
        return make_response(jsonify({"status":201, "data":[{"id":Redflag["id"],"message":"Adding redflag successful"}]}), 201)

    