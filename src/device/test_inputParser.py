from . import input_data_parser
import json

# Validate happy path of a valid json file
def test_write_to_database_function_with_valide_file() -> None:
    validJson = input_data_parser.write_to_database("data/sample_patient1.json")
    resultBoolean:bool = validJson[0]
    assert resultBoolean

# Validate invalid input
def test_write_to_database_function_with_invalide_input() -> None:
    validJson = input_data_parser.write_to_database("123")
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a json file
def test_write_to_database_function_with_invalide_file() -> None:
    validJson = input_data_parser.write_to_database("data/sample_fail_file.json")
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a non json file
def test_write_to_database_function_with_invalide_file_two() -> None:
    validJson = input_data_parser.write_to_database("data/sample.txt")
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate happy path of a valid json string 
def test_write_to_database_function_with_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'Male', 'dob': '01-01-1992', 'phoneNumber': '123-456-7890', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert resultBoolean

# Validate fail path of an empty json string 
def test_write_to_database_function_with_empty_json_string() -> None:
    data_set = {}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid deviceId in json string 
def test_write_to_database_function_with_invalid_deviceID_json_string() -> None:
    data_set = {'deviceId': "1234", 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'Male', 'dob': '01-01-1992', 'phoneNumber': '123-456-7890', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid deviceId in json string 
def test_write_to_database_function_with_invalid_patientId_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': "4321", 'patientName': 'ja mendes', 'gender': 'Male', 'dob': '01-01-1992', 'phoneNumber': '123-456-7890', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid patientName in json string 
def test_write_to_database_function_with_invalid_patientName_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 23, 'gender': 'Male', 'dob': '01-01-1992', 'phoneNumber': '123-456-7890', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid gender in json string 
def test_write_to_database_function_with_invalid_gender_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'invalid gender', 'dob': '01-01-1992', 'phoneNumber': '123-456-7890', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid dob in json string 
def test_write_to_database_function_with_invalid_dob_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'male', 'dob': '01.01.1992', 'phoneNumber': '123-456-7890', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid phoneNumber in json string 
def test_write_to_database_function_with_invalid_phoneNumber_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'male', 'dob': '01-01-1992', 'phoneNumber': '12312-456-783290', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid address in json string 
def test_write_to_database_function_with_invalid_address_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'male', 'dob': '01-01-1992', 'phoneNumber': '12312-456-783290', 'address': {'street': '440 Terry Ave N', 'city': 'Seattl123e', 'state': 'WA12', 'zipcode': 98213109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid temperature in json string 
def test_write_to_database_function_with_invalid_temperature_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'male', 'dob': '01-01-1992', 'phoneNumber': '12312-456-783290', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 25, 'unit': 'C'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid bloodPressure in json string 
def test_write_to_database_function_with_invalid_bloodPressure_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'male', 'dob': '01-01-1992', 'phoneNumber': '12312-456-783290', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': -2, 'diastolic': 800, 'unit': 'mmmmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid pulse in json string 
def test_write_to_database_function_with_invalid_pulse_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'male', 'dob': '01-01-1992', 'phoneNumber': '12312-456-783290', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 700, 'unit': 'beats'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid oximeter in json string 
def test_write_to_database_function_with_invalid_oximeter_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'male', 'dob': '01-01-1992', 'phoneNumber': '12312-456-783290', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': -96, 'unit': 'times'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid weight in json string 
def test_write_to_database_function_with_invalid_weight_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'male', 'dob': '01-01-1992', 'phoneNumber': '12312-456-783290', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': -120, 'unit': 'kg'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid glucometer in json string 
def test_write_to_database_function_with_invalid_glucometer_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'male', 'dob': '01-01-1992', 'phoneNumber': '12312-456-783290', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg/dL'}, 'timestamp': '2022-02-20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean

# Validate fail path of a invalid timestamp in json string 
def test_write_to_database_function_with_invalid_timestamp_json_string() -> None:
    data_set = {'deviceId': 1234, 'patientId': 4321, 'patientName': 'ja mendes', 'gender': 'male', 'dob': '01-01-1992', 'phoneNumber': '12312-456-783290', 'address': {'street': '440 Terry Ave N', 'city': 'Seattle', 'state': 'WA', 'zipcode': 98109}, 'measurements': {'temperature': {'temperature': 100, 'unit': 'F'}, 'bloodPressure': {'systolic': 120, 'diastolic': 80, 'unit': 'mmHg'}, 'pulse': {'pulse': 70, 'unit': 'bpm'}, 'oximeter': {'oxygen': 96, 'unit': '%'}, 'weight': {'weight': 120, 'unit': 'lb'}, 'glucometer': {'bloodSugarLvl': 139, 'unit': 'mg-per-dL'}, 'timestamp': '2022/02/20T09:35:20Z'}}
    json_dump = json.dumps(data_set)
    validJson = input_data_parser.write_to_database(json_dump)
    resultBoolean:bool = validJson[0]
    assert not resultBoolean