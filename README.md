# MedicalApplication by Mandy Yao (EC 530)
## Description
The goal of this project is to create a medical application to monitor patients at home or in the hospital and faciliate communication between patient and medical professional through device module and chat module. The users of this application include patients, medical professionals, administrators and developers.  

## Database Module
The goal of the datebase module is to provide an API that accepts data in json format, validates the input, and transfers it to database. 

### How to Use
1) Create a python file for connecting to the API. (Sample: /device/api_simulation.py)
2) Import two libraries on the top
```import requests & import json```
3) Create a variable for the calling of API: "http://medicalapplication-env.eba-if3c99xq.us-east-1.elasticbeanstalk.com/" 
4) Create a json string that you want to pass in. It must be in the format of /device/sample_patient1.json.
*** Note: Please do not have '/' in the json file, otherwise the API will assume it's a separate input *** 
5) Make your json string into json:
```json.dumps(YOUR_JSON_STRING)```
6) Request get response for data validation:
```requests.get(BASE + "parser/" + json_dump)```
7) Request post response for posting data to the database:
```requests.post(BASE + "database/" + json_dump)```


## Chat System Module
The goal of the chat system module is to process communication requests and to facilitate live chat messaging between two or more parties. This API allows users to connect to a backend communication plateform that mimics that of a real-time chat functionality. The backend plateform uses MongoDB, NodeJS and Socket.io. 


### How to Use


### Results
To avoid aws from billing, the medical application api website is disabled. Below are proofs that it runs successfully when api_simulation.py is ran. This can also be tested locally by doing ```python3 api_simulation.py```:

```
{'success': True, 'message': "Success: all of patient's information is validated. ", 'data': {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'Male', 'dob': '01-01-1992', 'phoneNumber': '123-456-7890', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}}
{'success': True, 'message': 'Successfully written to database. '}
{'success': True, 'message': 'Success: message measurements are validated', 'data': {'accessToken': 123, 'messageInfo': {'messageId': 1234, 'sessionId': 4321, 'deviceType': 'ios', 'timestamp': '2022-02-20T09:35:20Z'}, 'sender': {'userId': 111, 'userName': 'mandyyao', 'name': 'Mandy Yao'}, 'recipient': {'userId': 222, 'userName': 'santiagogomez', 'name': 'Santiago Gomez'}, 'text': 'Hello World!', 'attachments': {'videoRecording': 'video.mov', 'voiceRecording': 'voice.mp3', 'picture': 'picture.jpg', 'fileUpload': 'file.pdf'}}}
{'success': True, 'message': 'Successfully written to mongoDB. '}
{'success': True, 'data': [{'accessToken': 123, 'messageInfo': {'messageId': 1234, 'sessionId': 4321, 'deviceType': 'ios', 'timestamp': '2022-02-20T09:35:20Z'}, 'sender': {'userId': 111, 'userName': 'mandyyao', 'name': 'Mandy Yao'}, 'recipient': {'userId': 222, 'userName': 'santiagogomez', 'name': 'Santiago Gomez'}, 'text': 'Hello World!', 'attachments': {'videoRecording': 'video.mov', 'voiceRecording': 'voice.mp3', 'picture': 'picture.jpg', 'fileUpload': 'file.pdf'}}]}
{'success': True, 'data': [{'accessToken': 123, 'messageInfo': {'messageId': 1234, 'sessionId': 4321, 'deviceType': 'ios', 'timestamp': '2022-02-20T09:35:20Z'}, 'sender': {'userId': 111, 'userName': 'mandyyao', 'name': 'Mandy Yao'}, 'recipient': {'userId': 222, 'userName': 'santiagogomez', 'name': 'Santiago Gomez'}, 'text': 'Hello World!', 'attachments': {'videoRecording': 'video.mov', 'voiceRecording': 'voice.mp3', 'picture': 'picture.jpg', 'fileUpload': 'file.pdf'}}]}
{'success': True, 'data': [{'accessToken': 123, 'messageInfo': {'messageId': 1234, 'sessionId': 4321, 'deviceType': 'ios', 'timestamp': '2022-02-20T09:35:20Z'}, 'sender': {'userId': 111, 'userName': 'mandyyao', 'name': 'Mandy Yao'}, 'recipient': {'userId': 222, 'userName': 'santiagogomez', 'name': 'Santiago Gomez'}, 'text': 'Hello World!', 'attachments': {'videoRecording': 'video.mov', 'voiceRecording': 'voice.mp3', 'picture': 'picture.jpg', 'fileUpload': 'file.pdf'}}]}
{'success': True, 'data': [{'accessToken': 123, 'messageInfo': {'messageId': 1234, 'sessionId': 4321, 'deviceType': 'ios', 'timestamp': '2022-02-20T09:35:20Z'}, 'sender': {'userId': 111, 'userName': 'mandyyao', 'name': 'Mandy Yao'}, 'recipient': {'userId': 222, 'userName': 'santiagogomez', 'name': 'Santiago Gomez'}, 'text': 'Hello World!', 'attachments': {'videoRecording': 'video.mov', 'voiceRecording': 'voice.mp3', 'picture': 'picture.jpg', 'fileUpload': 'file.pdf'}}]}
{'success': True, 'message': 'All message packages are deleted from mongoDB. '}
{'packages': '0'} 
```

## Release Notes 
Version 1.0
