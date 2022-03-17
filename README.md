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


## Release Notes 
Version 1.0
