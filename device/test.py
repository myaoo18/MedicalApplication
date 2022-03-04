import requests
import json

# Elastic beanstalk website
BASE = "http://medicalapplication-env.eba-if3c99xq.us-east-1.elasticbeanstalk.com/"

# Test 1: json string
data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'Male', 'dob': '01-01-1992', 'phoneNumber': '123-456-7890', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
json_dump = json.dumps(data_set)

# validate data
response = requests.get(BASE + "parser/" + json_dump)
print(response.json())

# put data in database
response = requests.post(BASE + "database/" + json_dump)
print(response.json())