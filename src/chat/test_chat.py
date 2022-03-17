from . import chat
import json

# Validate happy path of insert_message function with valid json file
def test_insert_message_function_with_valide_file() -> None:
    result1 = chat.insert_message("data/valid_message1.json")
    resultBoolean1:bool = result1[0]
    assert resultBoolean1

    result2 = chat.insert_message("data/valid_message2.json")
    resultBoolean2:bool = result2[0]
    assert resultBoolean2

    result3 = chat.insert_message("data/valid_message3.json")
    resultBoolean3:bool = result3[0]
    assert resultBoolean3

# Validate happy path of insert_message function with valid json string
def test_insert_message_function_with_valide_string() -> None:
    json_string1 = {'accessToken': 123, 'messageInfo': {'messageId': 1234, 'sessionId': 4321, 'deviceType': 'ios', 'timestamp': '2022-02-20T09:35:20Z'}, 'sender': {'userId': 111, 'userName': 'mandyyao', 'name': 'Mandy Yao'}, 'recipient': {'userId': 222, 'userName': 'santiagogomez', 'name': 'Santiago Gomez'}, 'text': 'Hello World!', 'attachments': {'videoRecording': 'video.mov', 'voiceRecording': 'voice.mp3', 'picture': 'picture.jpg', 'fileUpload': 'file.pdf'}}
    json_dump1 = json.dumps(json_string1)
    result1 = chat.insert_message(json_dump1)
    resultBoolean1:bool = result1[0]
    assert resultBoolean1

    json_string2 = {'accessToken': 123, 'messageInfo': {'messageId': 4321, 'sessionId': 1234, 'deviceType': 'android', 'timestamp': '2022-10-31T09:35:20Z'}, 'sender': {'userId': 12342, 'userName': 'billgates', 'name': 'Bill Gates'}, 'recipient': {'userId': 1, 'userName': 'osama', 'name': 'Osama Alshaykh'}, 'text': 'I love coding!', 'attachments': {'videoRecording': '', 'voiceRecording': '', 'picture': '', 'fileUpload': ''}}
    json_dump2 = json.dumps(json_string2)
    result2 = chat.insert_message(json_dump2)
    resultBoolean2:bool = result2[0]
    assert resultBoolean2

    json_string3 = {'accessToken': 123, 'messageInfo': {'messageId': 43231, 'sessionId': 12334, 'deviceType': 'android', 'timestamp': '2022-11-01T09:35:20Z'}, 'sender': {'userId': 142, 'userName': 'presidentbrown', 'name': 'President Brown'}, 'recipient': {'userId': 2, 'userName': 'osama', 'name': 'Osama Alshaykh'}, 'text': '', 'attachments': {'videoRecording': 'file/video.mov', 'voiceRecording': '', 'picture': '', 'fileUpload': ''}}
    json_dump3 = json.dumps(json_string3)
    result3 = chat.insert_message(json_dump3)
    resultBoolean3:bool = result3[0]
    assert resultBoolean3

# Validate fail path of invalid json file
def test_insert_message_function_with_invalide_file() -> None:
    result1 = chat.insert_message("data/invalid_message1.json")
    resultBoolean1:bool = result1[0]
    assert not resultBoolean1

    # access token must be 123, fail otherwise
    result2 = chat.insert_message("data/invalid_token.json")
    resultBoolean2:bool = result2[0]
    assert not resultBoolean2

    result3 = chat.insert_message("data/invalid_message3.json")
    resultBoolean3:bool = result3[0]
    assert not resultBoolean3

# Validate fail path of invalid json string
def test_insert_message_function_with_invalide_string() -> None:
    json_string1 = {'accessToken': 123, 'messageInfo': {'messageId': 1234, 'sessionId': 4321, 'deviceType': 'ios', 'timestamp': '2022-02-20T09:35:20Z'}, 'sender': {'userId': 111, 'userName': 'mandyyao', 'name': 'Mandy Yao'}, 'recipient': {'userId': 222, 'userName': 'santiagogomez', 'name': 'Santiago Gomez'}}
    json_dump1 = json.dumps(json_string1)
    result1 = chat.insert_message(json_dump1)
    resultBoolean1:bool = result1[0]
    assert not resultBoolean1

    # access token must be 123, fail otherwise
    json_string2 = {'accessToken': 1234, 'messageInfo': {'messageId': 4321, 'sessionId': 1234, 'deviceType': 'android', 'timestamp': '2022-10-31T09:35:20Z'}, 'sender': {'userId': 12342, 'userName': 'billgates', 'name': 'Bill Gates'}, 'recipient': {'userId': 1, 'userName': 'osama', 'name': 'Osama Alshaykh'}, 'text': 'I love coding!', 'attachments': {'videoRecording': '', 'voiceRecording': '', 'picture': '', 'fileUpload': ''}}
    json_dump2 = json.dumps(json_string2)
    result2 = chat.insert_message(json_dump2)
    resultBoolean2:bool = result2[0]
    assert not resultBoolean2

    json_string3 = {'accessToken': 123, 'messageInfo': {'messageId': 43231, 'sessionId': 12334, 'deviceType': 'android', 'timestamp': '2022-11-01T09:35:20Z'}, 'text': '', 'attachments': {'videoRecording': 'file/video.mov', 'voiceRecording': '', 'picture': '', 'fileUpload': ''}}
    json_dump3 = json.dumps(json_string3)
    result3 = chat.insert_message(json_dump3)
    resultBoolean3:bool = result3[0]
    assert not resultBoolean3

# Validate delete all messages function
def test_delete_all_messages_function() -> None:
    result = chat.delete_all_messages()
    resultBoolean:bool = result[0]
    assert resultBoolean

# Validate number_of_packages function
def test_number_of_packages_function() -> None:
    result = chat.number_of_packages()
    assert result == 0

# Validate find_message_by_messageId function
def test_find_message_by_messageId_function() -> None:
    chat.insert_message("data/valid_message1.json")
    result = chat.find_message_by_messageId(1234)
    resultBoolean:bool = result[0]
    assert resultBoolean

# Validate find_message_by_senderId function
def test_find_message_by_senderId_function() -> None:
    result = chat.find_message_by_senderId(111)
    resultBoolean:bool = result[0]
    assert resultBoolean

# Validate find_message_by_recipientId function
def test_find_message_by_recipientId_function() -> None:
    result = chat.find_message_by_recipientId(222)
    resultBoolean:bool = result[0]
    assert resultBoolean
