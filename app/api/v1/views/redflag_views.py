from flask_restful import reqparse
import datetime

from flask import jsonify, json, request, make_response
Redflags = []


class Instance():

    def __init__(self):
        self.db = Redflags
        
    def view_redflags(self):
        return jsonify({"status": 200, "data": self.db})

    def create_redflag(self):
   
        Redflag = {
            "id": len(self.db)+1,
            "createdon": datetime.datetime.now(),
            "Title": request.get_json()["Title"],
            "type": "Redflag",
            "Createdby": request.get_json()["Createdby"],
            "Description": request.get_json()["Description"],
            "Location": request.get_json()["Location"],
            "Status": "Resolved",
            "Video": request.get_json()["Video"],
            "Image": request.get_json()["Image"]

        }
        for item in self.db:
            if item["Title"] == Redflag["Title"]:
              return make_response(jsonify({"status": 201, "message": " Record already exists "}), 201) 
        # validation for white spaces
        if Redflag["Title"].isspace() or Redflag["Createdby"].isspace() or Redflag["Description"].isspace() or Redflag["Location"].isspace():
            return make_response(jsonify({"status": 201, "message": " no blanks "}), 201)
        # validation for no entry
        keys = Redflag.keys()
        for key in keys:

            if not Redflag[key]:
                return make_response(jsonify({"status": 201, "message": " Please enter details"}), 201)

        self.db.append(Redflag)
        return make_response(jsonify({"status": 201, "data": [{"id": Redflag["id"], "message":"Adding redflag successful"}]}), 201)

    def specific(self, item_id):
        for record in self.db:
            if record['id'] == item_id:
                return make_response(jsonify({"status": 200, "data": record[0]}), 200)
        return jsonify({"status": 200, "data": "Redflag not found"})

    def delete_redflag(self, item_id):
        for record in Redflags:
            if record["id"] == item_id:
                self.db.remove(record)
                return make_response(jsonify({"status": 200, "data": [{"id": record["id"], "message":"Successfully deleted"}]}), 200)
        return jsonify({"status": 200, "data": [{"message": "Redflag does not exist"}]})

    def edit_redflag(self, item_id):
        for record in Redflags:
            if record["id"] == item_id:
                record['Title'] = request.json['Title']
                record['Location'] = request.json['Location']
                return jsonify({"status": 200, "data": [{"id": record["id"], "message":"Successfully updated"}]}, 200)
        return jsonify({"status": 200, "data": [{"message": " Redflag does not exist"}]})
