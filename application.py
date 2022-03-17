from flask import Flask, abort
from flask_restful import Api, Resource
import json
import src

application = Flask(__name__)
api = Api(application)

patientParserResults = []
messageParserResults = []


# For Device
class HomePage(Resource):
    def get(self):
        return "Landing page for Medical Application APIs"

class JsonParser(Resource):
    def get(self, json_string):
        global patientParserResults
        try:
           # patientParserResults = input_data_parser.validate(json_string)
            patientParserResults = src.input_data_parser.validate(json_string)
            if (patientParserResults[0]):
                return {"success": patientParserResults[0],
                        "message": patientParserResults[1],
                        "data": patientParserResults[2]}
            else:
                return {"success": patientParserResults[0],
                        "message": patientParserResults[1],
                        "path": json_string}
        except:
            abort(404, message="Json passed in is invalid. Check that you don't have unnecessary '/' in your string.")

class SendToDatabase(Resource):
    def post(self, json_string):
        try:
            #databaseResults = input_data_parser.write_to_database(json_string)
            databaseResults = src.input_data_parser.write_to_database(json_string)
            if (databaseResults[0]):
                return {"success": databaseResults[0],
                        "message": databaseResults[1]}
            else: 
                return {"success": patientParserResults[0],
                         "message": patientParserResults[1] + "Therefore, nothing is written to database. Please correct your json input first."}
        except:
            abort(404, message="Cannot write to database. Please check database json file exist.")


# For Chat
class MessagePackageParser(Resource):
    def get(self, json_string):
        global messageParserResults
        try:
            #messageParserResults = chat.validate(json_string)
            messageParserResults = src.chat.validate(json_string)
            if (messageParserResults[0]):
                return {"success": messageParserResults[0],
                        "message": messageParserResults[1],
                        "data": messageParserResults[2]}
            else:
                return {"success": messageParserResults[0],
                        "message": messageParserResults[1],
                        "path": json_string}
        except:
            abort(404, message="Json passed in is invalid. Check that you don't have unnecessary '/' in your string.")

class InsertMessageToMongoDB(Resource):
    def post(self, json_string):
        try:
            #mongoDBResult = chat.insert_message(json_string)
            mongoDBResult = src.chat.insert_message(json_string)
            if (mongoDBResult[0]):
                return {"success": mongoDBResult[0],
                        "message": mongoDBResult[1]}
            else:
                return {"success": messageParserResults[0],
                        "message": messageParserResults[1] + "Therefore, nothing is written to mongoDB. Please correct your json input first."}
        except:
            abort(404, message="Cannot write to mongoDB. Please check mongoDB cluster and collection exist.")

class FindMessagesByMessageId(Resource):
    def get(self, message_id):
        try:
            #messageResult = chat.find_message_by_messageId(int(message_id))
            messageResult = src.chat.find_message_by_messageId(int(message_id))
            if (messageResult[0]):
                return {"success": messageResult[0],
                        "data": messageResult[1]}
            else:
                return {"success": messageResult[0],
                        "message": messageResult[1]}
        except:
            abort(404, message="Cannot retrieve message through message id from mongoDB. Please only pass in numbers in string format.")

class FindMessagesBySenderId(Resource):
    def get(self, sender_id):
        try:
            #messageResult = chat.find_message_by_senderId(int(sender_id))
            messageResult = src.chat.find_message_by_senderId(int(sender_id))
            if (messageResult[0]):
                return {"success": messageResult[0],
                        "data": messageResult[1]}
            else:
                return {"success": messageResult[0],
                        "message": messageResult[1]}
        except:
            abort(404, message="Cannot retrieve message through sender id from mongoDB. Please only pass in numbers in string format.")

class FindMessagesByRecipientId(Resource):
    def get(self, recipient_id):
        try:
            #messageResult = chat.find_message_by_recipientId(int(recipient_id))
            messageResult = src.chat.find_message_by_recipientId(int(recipient_id))
            if (messageResult[0]):
                return {"success": messageResult[0],
                        "data": messageResult[1]}
            else:
                return {"success": messageResult[0],
                        "message": messageResult[1]}
        except:
            abort(404, message="Cannot retrieve message through recipient id from mongoDB. Please only pass in numbers in string format.")

class FindMessagesBySenderName(Resource):
    def get(self, sender_name):
        try:
            #messageResult = chat.find_message_by_sender_name(sender_name)
            messageResult = src.chat.find_message_by_sender_name(sender_name)
            if (messageResult[0]):
                return {"success": messageResult[0],
                        "data": messageResult[1]}
            else:
                return {"success": messageResult[0],
                        "message": messageResult[1]}
        except:
            abort(404, message="Cannot retrieve message through sender name from mongoDB. Please only first and last name in string format.")

class DeleteAllMessages(Resource):
    def post(self):
        try:
            #result = chat.delete_all_messages()
            result = src.chat.delete_all_messages()
            return {"success": result[0],
                    "message": result[1]}
        except:
            abort(404, message="Cannot delete all messages from mongoDB. Please check mongoDB.")

class FindNumberOfPackages(Resource):
    def get(self):
        try:
            #result = chat.number_of_packages()
            result = src.chat.number_of_packages()
            return {"packages": result[0]}
        except:
            abort(404, message="Cannot retrieve number of message packages from mongoDB. Please check mongoDB.")


api.add_resource(HomePage, "/")
api.add_resource(JsonParser, "/device/parser/<string:json_string>")
api.add_resource(SendToDatabase, "/device/database/<string:json_string>")
api.add_resource(MessagePackageParser, "/chat/parser/<string:json_string>")
api.add_resource(InsertMessageToMongoDB, "/chat/insertMessage/<string:json_string>")
api.add_resource(FindMessagesByMessageId, "/chat/findAllByMessageId/<string:message_id>")
api.add_resource(FindMessagesBySenderId, "/chat/findAllBySenderId/<string:sender_id>")
api.add_resource(FindMessagesByRecipientId, "/chat/findAllByRecipientId/<string:recipient_id>")
api.add_resource(FindMessagesBySenderName, "/chat/findAllBySenderName/<string:sender_name>")
api.add_resource(DeleteAllMessages, "/chat/deleteAllMessages")
api.add_resource(FindNumberOfPackages, "/chat/findNumberOfPackages")


if __name__ == "__main__":
    application.run(debug=True)