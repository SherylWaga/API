from flask_restful import reqparse
import datetime
from flask import jsonify,json,request, make_response
users=[]
class user():

    def __init__(self):
        self.db = users

    def view_users(self):
        return jsonify({"status":200,"data":self.db})
    def register_user(self):
           
        user = {
            "id":len(self.db)+1,
            "Registered":datetime.datetime.now(),
            "Firstname":request.get_json()["Firstname"],
            "Lastname":request.get_json()["Lastname"],
            "email":request.get_json()["email"],
            "phonenumber":request.get_json()["phonenumber"],
            "username":request.get_json()["username"],
            "password":request.get_json()["password"]
                     
             }
        
        self.db.append(user)
        return make_response(jsonify({"status":201, "data":[{"id":user["id"],"message":"Registration successful"}]}), 201)
















# from flask import request,jsonify,make_response 
# from flask_restful import Resource
# #local import
# from app.api.v1.models.user_models import Register

#     def post(self):
#         user=Register().save_user()
#         return make_response(jsonify({"status":201, "data":[{"id":user["id"],"message":"Registration successful"}]}), 201)
#     #    if  self.db ["id"]== user_id :
#     #        return  make_response(jsonify({"status":201, "data":[{"id":users["id"],"message":"Login successful"}]}), 201)
#     #    else:
#     #        newUser = Register().register_user()
#     #        return newUser