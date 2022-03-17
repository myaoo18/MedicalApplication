import requests
import json

# Elastic beanstalk website
#BASE = "http://medicalapplication-env.eba-if3c99xq.us-east-1.elasticbeanstalk.com/"
BASE = "http://127.0.0.1:5000/"

# Testing for device API
patient_data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'Male', 'dob': '01-01-1992', 'phoneNumber': '123-456-7890', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
patient_json_dump = json.dumps(patient_data_set)

# validate data
response = requests.get(BASE + "device/parser/" + patient_json_dump)
print(response.json())

# put data in database
response = requests.post(BASE + "device/database/" + patient_json_dump)
print(response.json())

###########################################################################################

# Testing for chat API
message_data_set = {'accessToken': 123, 'messageInfo': {'messageId': 1234, 'sessionId': 4321, 'deviceType': 'ios', 'timestamp': '2022-02-20T09:35:20Z'}, 'sender': {'userId': 111, 'userName': 'mandyyao', 'name': 'Mandy Yao'}, 'recipient': {'userId': 222, 'userName': 'santiagogomez', 'name': 'Santiago Gomez'}, 'text': 'Hello World!', 'attachments': {'videoRecording': 'video.mov', 'voiceRecording': 'voice.mp3', 'picture': 'picture.jpg', 'fileUpload': 'file.pdf'}}
message_json_dump = json.dumps(message_data_set)

# validate data
response = requests.get(BASE + "chat/parser/" + message_json_dump)
print(response.json())

# put message package in mongoDB
response = requests.post(BASE + "chat/insertMessage/" + message_json_dump)
print(response.json())

# find message by message id
response = requests.get(BASE + "chat/findAllByMessageId/" + "1234")
print(response.json())

# find message by sender id
response = requests.get(BASE + "chat/findAllBySenderId/" + "111")
print(response.json())

# find message by recipient id
response = requests.get(BASE + "chat/findAllByRecipientId/" + "222")
print(response.json())

# find message by sender name
response = requests.get(BASE + "chat/findAllBySenderName/" + "Mandy Yao")
print(response.json())

# delete all messages
response = requests.post(BASE + "chat/deleteAllMessages")
print(response.json())

# Get number of message packages
response = requests.get(BASE + "chat/findNumberOfPackages")
print(response.json())