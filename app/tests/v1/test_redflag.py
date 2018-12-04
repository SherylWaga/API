import unittest
import os
import json
from app import create_app


class Redflag(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.data = {
            "Createdby": "sheryl",
            "Description": "police officer receiving bribe",
            "Image": "sheryl.jpg",
            "Location": "jjk nhjnairf",
            "Status": "Resolved",
            "Title": "Cor",
            "Video": "new.mp4",
            "createdon": "Tue, 04 Dec 2018 17:59:23 GMT",
            "id": 3,
            "type": "Redflag"
        }
        self.dt = {
            "Createdby": "sheryl",
            "Description": "police officer receiving bribe",
            "Image": "sheryl.jpg",
            "Location": "jjk ",
            "Status": "Resolved",
            "Title": "Corruption",
            "Video": "new.mp4",
            "createdon": "Tue, 04 Dec 2018 17:59:23 GMT",
            "id": 3,
            "type": "Redflag"
        }
        self.datta = {
             "Createdby": " ",
            "Description": " ",
            "Image": " ",
            "Location": " ",
            "Status": " ",
            "Title": " ",
            "Video": " "
        
            
        }

    def test_cteate_redflag(self):
        res = self.client().post('/api/v1/redflags', data=json.dumps(self.data),
                                 content_type="application/json")
        self.assertEqual(res.status_code, 201)
        self.assertIn("Adding redflag successful", str(res.data))

    def test_get_redflag(self):
        res = self.client().get('/api/v1/redflags', data=json.dumps(self.data),
                                content_type="application/json")
        self.assertEqual(res.status_code, 200)

    def test_edit(self):
        res = self.client().post('/api/v1/redflags', data=json.dumps(self.data),
                                 content_type="application/json")
        self.assertEqual(res.status_code, 201)
        res = self.client().put('api/v1/redflags/3', data=json.dumps(self.dt),
                                content_type="application/json")
        self.assertEqual(res.status_code, 200)

    def test_delete(self):
        res = self.client().post('/api/v1/redflags', data=json.dumps(self.data),
                                 content_type="application/json")
        self.assertEqual(res.status_code, 201)
        res = self.client().delete('/api/v1/redflags/3', data=json.dumps(self.dt),
                                   content_type="application/json")
        self.assertEqual(res.status_code, 200)
    # trying to delete non-existing redflag

    def test_non_existing(self):
        res = self.client().post('/api/v1/redflags', data=json.dumps(self.data),
                                 content_type="application/json")
        self.assertEqual(res.status_code, 201)
        res = self.client().delete('/api/v1/redflags/4', data=json.dumps(self.data),
                                   content_type="application/json")
        self.assertEqual(res.status_code, 200)
    # trying to edit non-existing redflag

    def test_edit_non_existing(self):
        res = self.client().post('/api/v1/redflags', data=json.dumps(self.data),
                                 content_type="application/json")
        self.assertEqual(res.status_code, 201)
        res = self.client().delete('/api/v1/redflags/20', data=json.dumps(self.data),
                                   content_type="application/json")
        self.assertIn("Redflag does not exist", str(res.data))
    #test if redflag creation entries are blank
    def test_cteate_null(self):
        res = self.client().post('/api/v1/redflags', data=json.dumps(self.datta),
                                 content_type="application/json")
        self.assertEqual(res.status_code, 201)
      
        
    
        
    
    
if __name__ == '__main__':
    unittest.main()
