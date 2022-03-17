# MedicalApplication by Mandy Yao (EC 530)
## Description
The goal of this project is to create a medical application API to help monitor patients at home or in the hospital and faciliate communication between patient and medical professional through device module and chat module. The users of this application include patients, medical professionals, administrators and developers.  


## Database Module
The goal of the datebase module is to provide an API that accepts data in json format, validates the input, and transfers it to a database. 
For details on device module package structure: [Device Package Structure](https://github.com/myaoo18/MedicalApplication/wiki/Device-Package-Structure)
For details on device api: [Device API](https://github.com/myaoo18/MedicalApplication/wiki/Device-API)

## Chat System Module
The goal of the chat system module is to validate message packages, store them in mongoDB, allow users to find messages based on id and names, delete message packages from mongoDB and return a count of existing packages from the database. This API allows users to connect to a backend communication plateform that mimics that of a real-time chat functionality.
For details on chat module package structure: [Chat Package Structure](https://github.com/myaoo18/MedicalApplication/wiki/Device-Package-Structure)
For details on chat API: [Chat API](https://github.com/myaoo18/MedicalApplication/wiki/Chat-API)

## Branching Strategy
For details on branching: [Branching Strategy](https://github.com/myaoo18/MedicalApplication/wiki/Branching-Strategy)

## Results and Conclusions
For details on results and conclusions: [Results and Conclusion](https://github.com/myaoo18/MedicalApplication/wiki/Results-and-Conclusion)


## How to Use
1) Create a python file for connecting to the API. (Sample: /device/api_simulation.py)
2) Import two libraries on the top
```import requests & import json```
3) Create a variable for the calling of API: "http://127.0.0.1:5000/" (locally and supported) or "http://medicalapplication-env.eba-if3c99xq.us-east-1.elasticbeanstalk.com/" (deprecated due to cost)
4) Follow api_simulation.py to call different functions of the api: 
```
device/parser/
device/database/
chat/parser/
chat/insertMessage/
chat/findAllByMessageId/
chat/findAllBySenderId/
chat/findAllByRecipientId/
chat/findAllBySenderName/
chat/deleteAllMessage/
chat/findNumberOfPackages/
```


## Results
To avoid aws from billing, the medical application api is disabled Amazon BeanStalk. Below are proofs that it runs successfully when api_simulation.py is ran. This can also be tested locally by doing ```python3 api_simulation.py```:

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
