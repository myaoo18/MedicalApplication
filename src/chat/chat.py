import logging
import sys
import os
import json
import datetime
import collections
import pymongo
from pymongo import MongoClient

# Credentials for mongoDB
cluster = MongoClient("mongodb+srv://myao:z8psEQQV9vAONT68@cluster0.thk7f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Medical_Application_Chat"]
collection = db["Messages"]

# Check parameter type to be valid
def check_parameter_type (data, keys, validType):
    dict_valueType = []
    message:str = ""

    # Get value types from data 
    for key in keys:
        # Store value types in list
        dict_valueType.append(type(data[key]).__name__)

    # Check value type differences
    for index, (first, second) in enumerate(zip(validType, dict_valueType)):
        if first != second:
            message += "Fail: {} should be {} but is {} instead. ".format(keys[index], validType[index], dict_valueType[index])

    return message

# Validate all keys from json exist
def validate_all_key_exist (keys, types):
    if (collections.Counter(keys) != collections.Counter(types)):
            missing_keys = set(keys) - set(types)
            extra_keys = set(types) - set(keys)
            message:str = "Fail: json file has missing primary key(s) {} and extra key(s) {}. It should only contain {}".format(missing_keys, extra_keys, keys)
            logging.error(message)
            return [False, message]
    return [True, "Success: json file has {}".format(keys)]

# Validate information
def validate_info(messageInfo):
    dict_infoKeys = ["messageId", "sessionId", "deviceType", "timestamp"]
    dict_validInfoValueType = ['int', 'int', 'str', 'str']
    message:str = ""

    message+= check_parameter_type(messageInfo, dict_infoKeys, dict_validInfoValueType)

    # Check messageId parameter
    if (type(messageInfo["messageId"]).__name__ == 'int' and (messageInfo["messageId"] < 0 or messageInfo["messageId"] > 999999)):
        message += "Fail: messageId value should be between 0 and 999999. "

    # Check sessionId parameter
    if (type(messageInfo["sessionId"]).__name__ == 'int' and (messageInfo["sessionId"] < 0 or messageInfo["sessionId"] > 999999)):
        message += "Fail: sessionId value should be between 0 and 999999. "

    # Check deviceType parameter
    if (type(messageInfo["deviceType"]).__name__ == 'str' and (messageInfo["deviceType"] == "")):
        message += "Fail: deviceType is {} which is not valid. ".format(messageInfo["deviceType"])

    # Validate timestamp parameter "%Y-%m-%dT%H:%M:%SZ"
    try:
        datetime.datetime.strptime(messageInfo["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
    except:
        message += "Fail: {} is not a valid timestamp. Timestamp should be in %Y-%m-%dT%H:%M:%SZ format. ".format(messageInfo["timestamp"])

    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]

    # Otherwise, return True and success message
    message = "Success: patient temperature is validated"
    logging.info(message)
    return [True, message]

 # Validate person information
def validate_person(personInfo):
    dict_infoKeys = ["userId", "userName", "name"]
    dict_validInfoValueType = ['int', 'str', 'str']
    message:str = ""

    message+= check_parameter_type(personInfo, dict_infoKeys, dict_validInfoValueType)

    # Check userId
    if (type(personInfo["userId"]).__name__ == 'int' and (personInfo["userId"] < 0 or personInfo["userId"] > 999999)):
        message += "Fail: userId value should be between 0 and 999999. "

    # Check userName
    if (type(personInfo["userName"]).__name__ == 'str' and (personInfo["userName"] == "")):
        message += "Fail: userName is {} which is not valid. ".format(personInfo["userName"])

    # Check name parameter   
    first_last = personInfo["name"].split(' ')
    for name in first_last:
        if len(name) < 2 or not name.isalpha() or len(first_last) < 2:
            message += "Fail: {} is invalid. System expects a first and last name separated with a space. ".format(personInfo["name"])
            break
    
    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]

    # Otherwise, return True and success message
    message = "Success: patient temperature is validated"
    logging.info(message)
    return [True, message]

# Validate messages
def validate_messages(text, attachments):
    dict_infoKeys = ["videoRecording", "voiceRecording", "picture", "fileUpload"]
    dict_validInfoValueType = ['str', 'str', 'str', 'str']
    message:str = ""

    message+= check_parameter_type(attachments, dict_infoKeys, dict_validInfoValueType)

    # Refuse empty messages
    if (text == "" and attachments["videoRecording"] == "" and attachments["voiceRecording"] == "" and attachments["picture"] == "" and attachments["fileUpload"] == ""):
        message:str = "Fail: message was empty. Nothing was being sent. "
        return [False, message]

    # Check text to be string
    if (type(text).__name__ != 'str'):
         message += "Fail: text is not string type. "
    
    # Check videoRecording in mov format
    if (attachments["videoRecording"]!= "" and attachments["videoRecording"][-4:] != ".mov"):
        message += "Fail: videoRecording file is not in .mov format but in {} instead. ".format(attachments["videoRecording"][-4:])

    # Check voiceRecording in mp3 format
    if (attachments["voiceRecording"]!= "" and attachments["voiceRecording"][-4:] != ".mp3"):
        message += "Fail: voiceRecording file is not in .mp3 format but in {} instead. ".format(attachments["voiceRecording"][-4:])

    # Check picture in jpg format
    if (attachments["picture"]!= "" and attachments["picture"][-4:] != ".jpg"):
        message += "Fail: picture file is not in .jpg format but in {} instead. ".format(attachments["picture"][-4:])

    # Check file in pdf format
    if (attachments["fileUpload"]!= "" and attachments["fileUpload"][-4:] != ".pdf"):
        message += "Fail: fileUpload file is not in .pdf format but in {} instead. ".format(attachments["fileUpload"][-4:])

    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]

    # Otherwise, return True and success message
    message = "Success: patient temperature is validated"
    logging.info(message)
    return [True, message]

# Parent function to validate json file or string
def validate_json(inputFile:str):
    dict_dataKeys = ["accessToken", "messageInfo", "sender", "recipient", "text", "attachments"]
    dict_validDataValueType = ['int', 'dict', 'dict', 'dict', 'str', 'dict']
    message:str = ""
    logging.info("Processing: validating json format")

    try:
        # Check to see if json file is passed in
        if (inputFile[-5:] == ".json"):
    
            with open (inputFile, "r") as f:
                if os.path.getsize(inputFile) == 0:
                    message = f"{inputFile} is empty"
                    logging.error(message)
                    return [False, message]
                
                data = json.load(f)
                logging.info("Processing input that's a json file")
               
        else:
            data = json.loads(inputFile)
            logging.info("Processing input that's not a json file")

        validateAllInfo = []

        # Validate json input
        dataKeys = data.keys()

        # Check if all primary keys are there, order does not matter
        validateKeys = validate_all_key_exist(dict_dataKeys, dataKeys)
        if (validateKeys[0] == False):
            return validateKeys

        # Confirm data type is correct
        message+= check_parameter_type(data, dict_dataKeys, dict_validDataValueType)

        # Validate access token
        if (data["accessToken"] != 123):
            message:str = "Fail: accessToken is incorrect. Try again."
            logging.error(message)
            return [False, message]

        # Validate message info
        validateMessageInfo = validate_info(data["messageInfo"])
        validateAllInfo.append(validateMessageInfo)

        validateSender = validate_person(data["sender"])
        validateAllInfo.append(validateSender)

        validateSender = validate_person(data["recipient"])
        validateAllInfo.append(validateSender)

        validateMessages = validate_messages(data["text"], data["attachments"])
        validateAllInfo.append(validateMessages)

        # Sum up all error messages if there are any false
        for results in validateAllInfo:
            if (results[0] == False): 
                message += results[1]

        # Return False along with all the messages when encountered with errors
        if message != "":
            return [False, message]

        # Otherwise, return True and success message
        message = "Success: message measurements are validated"
        logging.info(message)
        return [True, message, data]

    except:
        message:str = "Fail: json file format is incorrect"
        logging.error(message)
        return [False, message]


# Validate input file is valide json file
def validate(inputFile:str):

    logging.info("Processing: began validating file")

    # Validate argument parameter is a string
    if (not isinstance(inputFile, str)):
        message:str = "Fail: input argument is not a string"
        logging.error(message)
        return [False, message]
    logging.info("Success: file argument passed in is a string")

    validateJsonResult = validate_json(inputFile)
    logging.info(validateJsonResult)

    return validateJsonResult


# Insert Messages
def insert_message (json_input):
    try:
        json_results = validate(json_input)

        # Check validate results, return false and error message when invalid
        if (json_results[0] == False):
            message:str = json_results[1] + "Therefore, no message data is written to mongoDB. Please try again."
            logging.error(message)
            return [False, message]

        # Otherwise, try writing to mongoDB
        collection.insert_one(json_results[2])
        message:str = "Successfully written to mongoDB"
        logging.info(message)
        return [True, message]

    except:
        message:str = "Could not write result or data to mongoDB"
        logging.error(message)
        return [False, message]


# Find data by messageId
def find_message_by_messageId (messageId:int):

    # Confirm input type to be integer between 
    if (not isinstance(messageId, int) or int(messageId) < 0 or int(messageId) > 999999):
        message:str = "messageId is not an integer between 0 and 999999. Please retry."
        return [False, message]

    try: 
        results = collection.find({"messageInfo.messageId": messageId})
        data = []
        for result in results:
            result.pop("_id")
            data.append(result)
        if (data == []):
            message:str = "Could not find data through messageId {} in mongoDB. ".format(messageId)
            return [False, message]
        else: 
            return [True, data]
    except:
        message:str = "Could not find data through messageId {} in mongoDB. ".format(messageId)
        logging.error(message)
        return [False, message]


# Find data by senderId
def find_message_by_senderId (senderId:int):

    # Confirm input type to be integer between 
    if (not isinstance(senderId, int) or int(senderId) < 0 or int(senderId) > 999999):
        message:str = "senderId is not an integer between 0 and 999999. Please retry."
        return [False, message]

    try: 
        results = collection.find({"sender.userId": senderId})
        data = []
        for result in results:
            result.pop("_id")
            data.append(result)
        if (data == []):
            message:str = "Could not find data through sender's userId {} in mongoDB. ".format(senderId)
            return [False, message]
        else: 
            return [True, data]
    except:
        message:str = "Could not find data through sender's userId {} in mongoDB. ".format(senderId)
        logging.error(message)
        return [False, message]


# Find Messages by recipientId
def find_message_by_recipientId (recipientId:int):

    # Confirm input type to be integer between 
    if (not isinstance(recipientId, int) or int(recipientId) < 0 or int(recipientId) > 999999):
        message:str = "recipientId is not an integer between 0 and 999999. Please retry."
        return [False, message]

    try: 
        results = collection.find({"recipient.userId": recipientId})
        data = []
        for result in results:
            result.pop("_id")
            data.append(result)
        if (data == []):
            message:str = "Could not find data through recipient's userId {} in mongoDB. ".format(recipientId)
            return [False, message]
        else: 
            return [True, data]
    except:
        message:str = "Could not find data through recipient's userId {} in mongoDB. ".format(recipientId)
        logging.error(message)
        return [False, message]


# Find Messages by sender name
def find_message_by_sender_name (senderName:str):
    # Confirm input type to be integer between 
    if (not isinstance(senderName, str) or len(senderName.split())!=2):
        message:str = "Sender name must be a string of first and last name. Please retry."
        return [False, message]
    
    try:
        results = collection.find({"sender.name": senderName})
        data = []
        for result in results:
            result.pop("_id")
            data.append(result)
        if (data == []):
            message:str = "Could not find data through sender's name {} in mongoDB. ".format(senderName)
            return [False, message]
        else: 
            return [True, data]
    except:
        message:str = "Could not find data through sender's name {} in mongoDB. ".format(senderName)
        logging.error(message)
        return [False, message]
    

# Delete Messages
def delete_all_messages():
    try:
        collection.delete_many({})
        all_deleted = collection.count_documents({})
        if (all_deleted == 0):
            message:str = "All message packages are deleted from mongoDB. "
            logging.info(message)
            return [True, message]    
        else: 
            message:str = "Could not delete all message packages from mongoDB. "
            logging.error(message)
            return [False, message]
    except:
        message:str = "Could not delete all message packages from mongoDB. "
        logging.error(message)
        return [False, message]


# Return number of message packages
def number_of_packages ():
    return str(collection.count_documents({}))


def main():
    if len(sys.argv) != 2:
        message:str = "You must insert one file as an argument. Please try again."
        logging.error(message)
        exit(1)
    insert_message(sys.argv[1])
    

if __name__ == "__main__":
    main()