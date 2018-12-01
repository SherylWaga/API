import unittest
import os
import json
from app import create_app

class Redflag(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.data= {
             "Createdby": "sheryl",
            "Description": "police officer receiving bribe",
            "Location": "jjk nhjnairf",
            "Status": "Resolved",
            "Title": "Cor",
            "image": "sheryl.jpg",
            "type": "Redflag",
            "video": "new.mp4"
        }
        self.dt={
          "Createdby": "sheryl",
            "Description": "police officer receiving bribe",
            "Location": "Nairobi",
            "Status": "Resolved",
            "Title": "Corruption",
            "image": "sheryl.jpg",
            "type": "Redflag",
            "video": "new.mp4"   
        }

        
    def test_cteate_redflag(self):
        res = self.client().post('/api/v1/redflags',data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(res.status_code, 201)
        self.assertIn("Adding redflag successful",str(res.data))
    
    def test_get_redflag(self):
        res = self.client().get('/api/v1/redflags',data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(res.status_code, 200)  
    # def test_edit(self):
    #     res = self.client().post('/redflags',data=json.dumps(self.data),content_type="application/json")
    #     self.assertEqual(res.status_code, 201)
    #     res=self.client().put('/redflags',data=json.dumps(self.dt),content_type="application/json")
    #     self.assertEqual(res.status_code,200)
    def test_delete(self):
        res= self.client().post('/api/v1/redflags',data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(res.status_code, 201)  
        self.client().delete('/api/v1/redflags/1')
        self.assertEqual(res.status_code,201)
if __name__ =='__main__':
    unittest.main()