from flask import request,jsonify
from flask_restful import Resource
#local import
from app.api.v1.views.redflag_views import Instance
class Redflags(Resource):
    def get(self):
        redflags = Instance().view_redflags()
        return redflags
    def post(self):
        new_post= Instance().create_redflag()
        return new_post
class RedflagsSpecific(Resource):
    def get(self, item_id):
        specific_data = Instance().specific(item_id)
        return specific_data
    def delete(self,item_id):
        return Instance().delete_redflag(item_id)
    def put(self,item_id):
        return Instance().edit_redflag(item_id)
    
























# from flask_restful import reqparse
# import datetime
# from flask import jsonify,json,request, make_response
# Redflags=[]
# class Instance():

#     def __init__(self):
#         self.db = Redflags

#     def view_redflags(self):
#         return jsonify({"status":200,"data":self.db})
#     def create_redflag(self):
       
#         Redflag = {
#             "id":len(self.db)+1,
#             "createdon":datetime.datetime.now(),
#             "Title":request.get_json()["Title"],
#             "type":"Redflag",
#             "Createdby":request.get_json()["Createdby"],
#             "Description":request.get_json()["Description"],
#             "Location":request.get_json()["Location"],
#             "Status":"Resolved",
#             "video":request.get_json()["video"],
#             "image":request.get_json()["image"]
     
#         }
#         resp=self.db.append(Redflag)
#         return make_response(jsonify({"status":201, "data":[{"id":Redflag["id"],"message":"Adding redflag successful"}]}), 201)

#     def specific(self,item_id):
#         record=[record for record in self.db if record['id']==item_id]
#         if len(record)==0:
#            return jsonify({"status":404,"data": "Redflag not found"})
#         return make_response( jsonify({"status":200,"data":record[0]}),200)

#     def delete_redflag(self,item_id):
#          for record in Redflags:
#             if record["id"]==item_id:
#                 self.db.remove(record)
#                 return make_response(jsonify({  "status":200, "data":[{"id":record["id"],"message":"Successfully deleted"}]  }),200)
           
        
#     def edit_redflag(self, item_id):
#         for record in Redflags:
#             if record["id"]==item_id:
#                 record['Title']=request.json['Title']
#                 record['Location']=request.json['Location']
#                 return jsonify({  "status":200, "data":[{"id":record["id"],"message":"Successfully updated"}]  },200)
