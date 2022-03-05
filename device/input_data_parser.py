import sys
import json
import logging
import collections
import re
import datetime

# Location where data gets stored after validation
database:str = "./data/database.json"

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

# Validate patient info
def validate_patient_info (data):
    dict_validDataKeys = ["deviceId", "patientId", "patientName", "gender", "dob", "phoneNumber"]
    dict_validDataValueType = ['int', 'int', 'str', 'str', 'str', 'str']
    message:str = ""

    message+= check_parameter_type(data, dict_validDataKeys, dict_validDataValueType)

    # Check deviceID parameter    
    if type(data["deviceId"]).__name__ == 'int' and (data["deviceId"] < 0 or  data["deviceId"] > 999999):
        message += "Fail: deviceId value should be between 0 and 999999. "

    # Check patientId parameter   
    if type(data["patientId"]).__name__ == 'int' and (data["patientId"] < 0 or  data["patientId"] > 999999):
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
        datetime.datetime.strptime(data["dob"], '%d-%m-%Y')
    except:
        message += "Fail: {} is not a valid dob. dob should be in MM/DD/YYYY format. ".format(data["dob"])

    # Check phoneNumber parameter   
    if type(data["phoneNumber"]).__name__ == 'str' and not re.match(r'^(?:\(\d{3}\)|\d{3}-)\d{3}-\d{4}$', data["phoneNumber"]):
        message += "Fail: {} is not a valid phone number. Phone number should be in XXX-XXX-XXXX format. ".format(data["phoneNumber"])

    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]
    
    # Otherwise, return True and success message
    message = "Success: patient info is validated"
    logging.info(message)
    return [True, message]

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
    message:str = ""

    message+= check_parameter_type(address, dict_validAddressKeys, dict_validAddressValueType)

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

    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]

    # Otherwise, return True and success message
    message = "Success: patient address is validated"
    logging.info(message)
    return [True, message]

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
def validate_temperature_info (tempMeasurements):
    dict_validTempKeys = ["temperature", "unit"]
    dict_validTempValueType = ['int', 'str']
    message:str = ""

    message+= check_parameter_type(tempMeasurements, dict_validTempKeys, dict_validTempValueType)

    # Check temperature parameter
    if type(tempMeasurements["temperature"]).__name__ == 'int' and (tempMeasurements["temperature"] < 50 or tempMeasurements["temperature"] > 200):
        message += "Fail: {} is not a valid temperature. ".format(tempMeasurements["temperature"])
    
    # Check unit parameter
    if tempMeasurements["unit"] != "F":
        message += "Fail: {} is not a valid temperature unit. Please use F.  ".format(tempMeasurements["unit"])

    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]

    # Otherwise, return True and success message
    message = "Success: patient temperature is validated"
    logging.info(message)
    return [True, message]

# Validate blood pressure info
def validate_BP_info (bpMeasurements):
    dict_validBPKeys = ["systolic", "diastolic", "unit"]
    dict_validBPValueType = ['int', 'int', 'str']
    message:str = ""

    message+= check_parameter_type(bpMeasurements, dict_validBPKeys, dict_validBPValueType)

    # Check systolic parameter
    if type(bpMeasurements["systolic"]).__name__ == 'int' and (bpMeasurements["systolic"] < 0 or bpMeasurements["systolic"] > 300):
        message += "Fail: {} is not a valid systolic. ".format(bpMeasurements["systolic"])
    

    # Check diastolic parameter
    if type(bpMeasurements["diastolic"]).__name__ == 'int' and bpMeasurements["diastolic"] > 300:
        message += "Fail: {} is not a valid diastolic. ".format(bpMeasurements["diastolic"])
    
    # Check unit parameter
    if bpMeasurements["unit"] != "mmHg":
        message += "Fail: {} is not a valid blood pressure unit. Please use mmHg.  ".format(bpMeasurements["unit"])

   # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]

    # Otherwise, return True and success message
    message = "Success: patient blood pressure is validated"
    logging.info(message)
    return [True, message]

# Validate pulse info
def validate_pulse_info (pulseMeasurements):
    dict_validPulseKeys = ["pulse", "unit"]
    dict_validPulseValueType = ['int', 'str']
    message:str = ""

    message+= check_parameter_type(pulseMeasurements, dict_validPulseKeys, dict_validPulseValueType)

    # Check pulse parameter
    if type(pulseMeasurements["pulse"]).__name__ == 'int' and (pulseMeasurements["pulse"] < 0 or pulseMeasurements["pulse"] > 300):
        message += "Fail: {} is not a valid pulse. ".format(pulseMeasurements["pulse"])
    
    # Check unit parameter
    if pulseMeasurements["unit"] != "bpm":
        message += "Fail: {} is not a valid temperature unit. Please use bpm.  ".format(pulseMeasurements["unit"])

    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]

    # Otherwise, return True and success message
    message = "Success: patient pulse is validated"
    logging.info(message)
    return [True, message]
    
# Validate oximeter info
def validate_oximeter_info (oximeterMeasurements):
    dict_validOximeterKeys = ["oxygen", "unit"]
    dict_validOximeterValueType = ['int', 'str']
    message:str = ""

    message+= check_parameter_type(oximeterMeasurements, dict_validOximeterKeys, dict_validOximeterValueType)

    # Check oxygen parameter
    if type(oximeterMeasurements["oxygen"]).__name__ == 'int' and oximeterMeasurements["oxygen"] < 0:
        message += "Fail: {} is not a valid oxygen level. ".format(oximeterMeasurements["oxygen"])
    
    # Check unit parameter
    if oximeterMeasurements["unit"] != "%":
        message += "Fail: {} is not a valid oxygen level unit. Please use %.  ".format(oximeterMeasurements["unit"])

    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]

    # Otherwise, return True and success message
    message = "Success: patient oximeter is validated"
    logging.info(message)
    return [True, message]

# Validate weight info
def validate_weight_info (weightMeasurements):
    dict_validWeightKeys = ["weight", "unit"]
    dict_validWeightValueType = ['int', 'str']
    message:str = ""

    message+= check_parameter_type(weightMeasurements, dict_validWeightKeys, dict_validWeightValueType)

    # Check weight parameter
    if type(weightMeasurements["weight"]).__name__ == 'int' and weightMeasurements["weight"] < 0 :
        message += "Fail: {} is not a valid weight number. ".format(weightMeasurements["weight"])
    
    # Check unit parameter
    if weightMeasurements["unit"] != "lb":
        message += "Fail: {} is not a valid weight unit. Please use lb.  ".format(weightMeasurements["unit"])

    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]

    # Otherwise, return True and success message
    message = "Success: patient weight is validated"
    logging.info(message)
    return [True, message]

# Validate pulse info
def validate_glucometer_info (glucometerMeasurements):
    dict_validGlucometerKeys = ["bloodSugarLvl", "unit"]
    dict_validGlucometerValueType = ['int', 'str']
    message:str = ""

    message+= check_parameter_type(glucometerMeasurements, dict_validGlucometerKeys, dict_validGlucometerValueType)

    # Check bloodSugarLvl parameter
    if type(glucometerMeasurements["bloodSugarLvl"]).__name__ == 'int' and glucometerMeasurements["bloodSugarLvl"] < 0 :
        message += "Fail: {} is not a valid blood sugar level. ".format(glucometerMeasurements["bloodSugarLvl"])
    
    # Check unit parameter
    if glucometerMeasurements["unit"] != "mg-per-dL":
        message += "Fail: {} is not a valid blood sugar unit. Please use mg/dL.  ".format(glucometerMeasurements["unit"])

    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]

    # Otherwise, return True and success message
    message = "Success: patient glucometer is validated"
    logging.info(message)
    return [True, message]

# Validate measurement keys
def validate_measurement_items (measurementKeys, measurements):
    dict_dataKeys = ["temperature", "bloodPressure", "pulse", "oximeter", "weight", "glucometer", "timestamp"]
    
    logging.info("Processing: validating json measurement keys of {}".format(dict_dataKeys))

    # Check if all measurement keys are there, order does not matter
    if (collections.Counter(dict_dataKeys) != collections.Counter(measurementKeys)):
        missing_keys = set(dict_dataKeys) - set(measurementKeys)
        extra_keys = set(measurementKeys) - set(dict_dataKeys)
        message:str = "Fail: json file has missing primary key(s) {} and extra key(s) {}. It should only contain {}".format(missing_keys, extra_keys, dict_dataKeys)
        logging.error(message)
        return [False, message]
    
    validateMeasurementInfo = []

    # Validate values in temperature keys
    validateTemperatureInfo = validate_temperature_info (measurements["temperature"])
    validateMeasurementInfo.append(validateTemperatureInfo)

    # Validate values in bloodPressure keys
    validateBloodPressureInfo = validate_BP_info (measurements["bloodPressure"])
    validateMeasurementInfo.append(validateBloodPressureInfo)

    # Validate values in Pulse keys
    validatePulseInfo = validate_pulse_info (measurements["pulse"])
    validateMeasurementInfo.append(validatePulseInfo)

    # Validate values in Pulse keys
    validateOximeterInfo = validate_oximeter_info (measurements["oximeter"])
    validateMeasurementInfo.append(validateOximeterInfo)

    # Validate values in Pulse keys
    validateWeightInfo = validate_weight_info (measurements["weight"])
    validateMeasurementInfo.append(validateWeightInfo)

    # Validate values in Pulse keys
    validateGlucometerInfo = validate_glucometer_info (measurements["glucometer"])
    validateMeasurementInfo.append(validateGlucometerInfo)

    # Sum up all error messages if there are any false
    message:str = ""
    for results in validateMeasurementInfo:
        if (results[0] == False): 
            message += results[1]

    # Validate timestamp parameter "%Y-%m-%dT%H:%M:%SZ"
    try:
        datetime.datetime.strptime(measurements["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
    except:
        message += "Fail: {} is not a valid timestamp. Timestamp should be in %Y-%m-%dT%H:%M:%SZ format. ".format(measurements["timestamp"])

    # Return False along with all the messages when encountered with errors
    if message != "":
        return [False, message]

    # Otherwise, return True and success message
    message = "Success: patient measurements are validated"
    logging.info(message)
    return [True, message]

# Validate json file
def validate_json (inputFile:str):

    logging.info("Processing: validating json format")

    try:
        if (inputFile[-5:] == ".json"):
            f = open(inputFile)
            data = json.load(f)
            f.close()
        else:
            data = json.loads(inputFile)

        validateAllInfo = []

        # Validate parent items
        validate_parentItems = validate_parent_items(data.keys(), data)
        validateAllInfo.append(validate_parentItems)

        # Validate address items
        validate_addressItems = validate_address_items(data["address"].keys(), data["address"])
        validateAllInfo.append(validate_addressItems)

        # Validate measurement items
        validate_measurementItems = validate_measurement_items(data["measurements"].keys(), data["measurements"])
        validateAllInfo.append(validate_measurementItems)

        # Sum up all error messages if there are any false
        message:str = ""
        for results in validateAllInfo:
            if (results[0] == False): 
                message += results[1]

        # Return False along with all the messages when encountered with errors
        if message != "":
            return [False, message]

        # Otherwise, return True and success message
        message = "Success: all of patient's information is validated"
        logging.info(message)
        return [True, message, data]

    except:
        message:str = "Fail: json file format is incorrect"
        logging.error(message)
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
    logging.info("Success: file argument passed in is a string")

    validateJsonResult = validate_json(inputFile)
    logging.info(validateJsonResult)

    return validateJsonResult

def write_to_database (json_file):
    try:
        # Validate data
        json_results = validate_file (json_file)
        
        # Check validate results, return false and error message when invalid
        if (json_results[0] == False):
            message:str = json_results[1] + "Therefore, no data is written to database. Please try again."
            logging.error(message)
            return [False, message]

        # Otherwise, try writing to database
        with open(database, "w") as json_file:
            if (json_results[0] == True):
                json.dump(json_results[2], json_file, indent=4)
            else:
                result = {}
                result['results'] = json_results[1]
                json.dump(result, json_file, indent=4)
        message:str = "Successfully written to database"
        logging.info(message)
        return [True, message]
    except:
        message:str = "Could not write result or data to database"
        logging.error(message)
        return [False, message]
    

def main():
    if len(sys.argv) != 2:
        message:str = "You must insert one file as an argument. Please try again."
        logging.error(message)
        exit(1)
    results = write_to_database (sys.argv[1])
    print (results)

if __name__ == '__main__':
    main()