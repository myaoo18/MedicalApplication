import sys
import json
import logging
import collections
import re
import datetime

# Location where data gets stored after validation
database:str = "./database.json"
# Emptying space for log file each time program is run
with open ('./logs/input_data_parser.log', 'r+') as f:
    f.truncate(0)
logging.basicConfig(filename='./logs/input_data_parser.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logging.getLogger(__name__)


# Validate input file name

# Validate patient info
def validate_patient_info (data):
    dict_validDataKeys = ["deviceId", "patientId", "patientName", "gender", "dob", "phoneNumber"]
    dict_validDataValueType = ['int', 'int', 'str', 'str', 'str', 'str']
    dict_dataValueType = []
    message:str = ""

    # Get primary value types from data 
    for keys in dict_validDataKeys:
        # Store primary value types in list
        dict_dataValueType.append(type(data[keys]).__name__)

    # Check primary value type differences
    for index, (first, second) in enumerate(zip(dict_validDataValueType, dict_dataValueType)):
        if first != second:
            message += "Fail: {} should be {} but is {} instead. ".format(dict_validDataKeys[index], dict_validDataValueType[index], dict_dataValueType[index])

    # Check deviceID parameter    
    if data["deviceId"] < 0 or  data["deviceId"] > 999999:
        message += "Fail: deviceId value should be between 0 and 999999. "

    # Check patientId parameter   
    if data["patientId"] < 0 or  data["patientId"] > 999999:
        message += "Fail: deviceId value should be between 0 and 999999. "

    # Check patientName parameter   
    first_last = data["patientName"].split(' ')
    for name in first_last:
        if len(name) < 2 or not name.isalpha() or len(first_last) < 2:
            message += "Fail: {} is invalid. System expects a first and last name separated with a space. ".format(data["patientName"])
            break

    # Check gender parameter   
    if data["gender"] != "Male" and data['gender'] != "Female":
        message += "Fail: {} is not a valid gender. Gender should either be Male or Female. ".format(data["gender"])

    # Check dob parameter   
    try:
        datetime.datetime.strptime(data["dob"], '%d/%m/%Y')
    except:
        message += "Fail: {} is not a valid dob. dob should be in MM/DD/YYYY format. ".format(data["dob"])

    # Check phoneNumber parameter   
    if not re.match(r'^(?:\(\d{3}\)|\d{3}-)\d{3}-\d{4}$', data["phoneNumber"]):
        message += "Fail: {} is not a valid phone number. Phone number should be in XXX-XXX-XXXX format. ".format(data["phoneNumber"])

    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]

    # Otherwise, return True and success message
    return [True, "Success: patient info is validated"]

# Validate all parent keys
def validate_parent_items (dataKeys, data):
    dict_dataKeys = ["deviceId", "patientId", "patientName", "gender", "dob", "phoneNumber", "address", "measurements"]
    
    logging.info("Processing: validating json parent keys of {}".format(dict_dataKeys))

    # Check if all primary keys are there, order does not matter
    if (collections.Counter(dict_dataKeys) != collections.Counter(dataKeys)):
        missing_keys = set(dict_dataKeys) - set(dataKeys)
        extra_keys = set(dataKeys) - set(dict_dataKeys)
        message:str = "Fail: json file has missing primary key(s) {} and extra key(s) {}. It should only contain {}".format(missing_keys, extra_keys, dict_dataKeys)
        logging.error(message)
        return [False, message]

    # Validate values in primary keys
    validatePatientInfo = validate_patient_info (data)
    
    return [validatePatientInfo[0], validatePatientInfo[1]]


# Validate address keys
def validate_address_info (address):
    dict_validAddressKeys = ["street", "city", "state", "zipcode"]
    dict_validAddressValueType = ['str', 'str', 'str', 'int']
    dict_addressDataValueType = []
    message:str = ""

    # Get address value types from data
    for keys in dict_validAddressKeys:
        # Store address value types in list
        dict_addressDataValueType.append(type(address[keys]).__name__)

    # Check address value type differences 
    for index, (first, second) in enumerate(zip(dict_validAddressValueType, dict_addressDataValueType)):
        if first != second:
            message += "Fail: {} should be {} but is {} instead. ".format(dict_validAddressKeys[index], dict_validAddressValueType[index], dict_addressDataValueType[index])

    # Check street parameter
    if (len(address["street"]) < 2):
        message += "Fail: {} is not a valid street. ".format(address["street"])

    # Check city parameter
    if (len(address["city"]) < 2):
        message += "Fail: {} is not a valid city. ".format(address["city"])

    # Check state parameter
    if (len(address["state"]) != 2):
        message += "Fail: {} is not a valid state. State should be in XX format. ".format(address["state"])
    # Check zipcode parameter
    if len(str(address["zipcode"])) != 5:
        message += "Fail: {} is not a valid zipcode. Zipcode should be in 5-digit format. ".format(address["zipcode"])

    if message != "":
        return [False, message]

    return [True, "Success: patient address is validated"]

def validate_address_items (addressKeys, address):
    dict_dataKeys = ["street", "city", "state", "zipcode"]
    
    logging.info("Processing: validating json address keys of {}".format(dict_dataKeys))

    # Check if all address keys are there, order does not matter
    if (collections.Counter(dict_dataKeys) != collections.Counter(addressKeys)):
        missing_keys = set(dict_dataKeys) - set(addressKeys)
        extra_keys = set(addressKeys) - set(dict_dataKeys)
        message:str = "Fail: json file has missing address key(s) {} and extra key(s) {}. It should only contain {}".format(missing_keys, extra_keys, dict_dataKeys)
        logging.error(message)
        return [False, message]
    
    # Validate values in address keys
    validateAddressInfo = validate_address_info (address)
    return [validateAddressInfo[0], validateAddressInfo[1]]


# Validate temperature info
def validate_temperature_info (measurements):
    dict_validTempKeys = ["temperature", "unit", "timestamp"]
    dict_validTempValueType = ['int', 'str', 'str']
    dict_tempValueType = []
    message:str = ""

    # Get temp value types from data 
    for keys in dict_validTempKeys:
        # Store primary value types in list
        dict_tempValueType.append(type(measurements[keys]).__name__)

    # Check temp value type differences
    for index, (first, second) in enumerate(zip(dict_validTempValueType, dict_tempValueType)):
        if first != second:
            message += "Fail: {} should be {} but is {} instead. ".format(dict_validTempKeys[index], dict_validTempValueType[index], dict_tempValueType[index])
    
    # Check temperature parameter
    if type(measurements["temperature"]).__name__ == int and (measurements["temperature"] < 50 or measurements["temperature"] > 200):
        message += "Fail: {} is not a valid temperature. ".format(measurements["temperature"])
    
    # Check unit parameter
    if measurements["unit"] != "F":
        message += "Fail: {} is not a valid temperature unit. Please use F.  ".format(measurements["unit"])

    # Check timestamp parameter "%Y-%m-%dT%H:%M:%SZ"
    try:
        datetime.datetime.strptime(measurements["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
    except:
        message += "Fail: {} is not a valid timestamp. Timestamp should be in %Y-%m-%dT%H:%M:%SZ format. ".format(measurements["timestamp"])

    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]
    
    return [True, "Success: patient temperature is validated"]

# Validate blood pressure info
def validate_BP_info (measurements):
    return False

# Validate pulse info
def validate_pulse_info (measurements):
    return False


# Validate measurement keys
def validate_measurement_items (measurementKeys, measurements):
    dict_dataKeys = ["temperature", "bloodPressure", "pulse", "condition", "medicalRequest"]
    
    logging.info("Processing: validating json measurement keys of {}".format(dict_dataKeys))

    # Check if all measurement keys are there, order does not matter
    if (collections.Counter(dict_dataKeys) != collections.Counter(measurementKeys)):
        missing_keys = set(dict_dataKeys) - set(measurementKeys)
        extra_keys = set(measurementKeys) - set(dict_dataKeys)
        message:str = "Fail: json file has missing primary key(s) {} and extra key(s) {}. It should only contain {}".format(missing_keys, extra_keys, dict_dataKeys)
        logging.error(message)
        return [False, message]

    # Validate values in temperature keys
    validateTemperatureInfo = validate_temperature_info (measurements["temperature"])
    print (validateTemperatureInfo)
    # Validate values in bloodPressure keys
    #validateBloodPressureInfo = validate_BP_info (measurements)
    
    # Validate values in Pulse keys
    #validatePulseInfo = validate_pulse_info (measurements)
    
    # Validate condition parameter

    # Validate medicalRequest parameter
    

    return False

# Validate json file
def validate_json (inputFile:str):

    logging.info("Processing: validating json format")

    try:
        f = open(inputFile)
        data = json.load(f)
        f.close()

        validate_parentItems = validate_parent_items(data.keys(), data)
        print (validate_parentItems)

        validate_addressItems = validate_address_items(data["address"].keys(), data["address"])
        print (validate_addressItems)

        validate_measurementItems = validate_measurement_items(data["measurements"].keys(), data["measurements"])
        print(validate_measurementItems)

    except:
        message:str = "Fail: json file format is incorrect"
        logging.error(message)
        print (message)
        return [False, message]

# Store data to database 

# Validate input file is valide json file
def validate_file (inputFile:str):

    logging.info("Processing: began validating file")

    # Validate argument parameter is a string
    if (not isinstance(inputFile, str)):
        message:str = "Fail: input argument is not a string"
        logging.error(message)
        return [False, message]
    logging.info("Success: file passed in is a string")

    # Validate argument parameter is json file
    if (len(inputFile) <= 5 or inputFile[-5:] != ".json"):
        message:str = "Fail: file passed in is not a json file"
        logging.error(message)
        return [False, message]
    logging.info("Success: file passed in is a json file")

    validateJson = validate_json(inputFile)

    return False
    # try:
    #     with open (inputFile) as f:
    #         json.load(f)
    # except:
    #     return False
    # return True

def main():
    if len(sys.argv) != 2:
        print("You must insert one file as an argument. Please try again.")
        exit(1)
    validFile = validate_file(sys.argv[1])
    
if __name__ == '__main__':
    main()