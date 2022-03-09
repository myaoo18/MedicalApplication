import input_data_parser
from flask import Flask, abort
from flask_restful import Api, Resource

application = Flask(__name__)
api = Api(application)

parserResults = []

class HomePage(Resource):
    def get(self):
        return "Landing page for Device Module API"

class JsonParser(Resource):
    def get(self, json_string):
        global parserResults
        try:
            parserResults = input_data_parser.validate_file(json_string)
            if (parserResults[0]):
                return {"success": parserResults[0],
                        "message": parserResults[1],
                        "data": parserResults[2]}
            else:
                return {"success": parserResults[0],
                        "message": parserResults[1],
                        "path": json_string}
        except:
            abort(404, message="Json string passed in is invalid. Check that you don't have unnecessary '/' in your string.")

class SendToDatabase(Resource):
    def post(self, json_string):
        try:
            databaseResults = input_data_parser.write_to_database(json_string)
            if (databaseResults[0]):
                return {"success": databaseResults[0],
                        "message": databaseResults[1]}
            else: 
                return {"success": parserResults[0],
                         "message": parserResults[1] + "Therefore, nothing is written to database. Please correct your json input first."}
        except:
            abort(404, message="Cannot write to database. Please check database json file exist.")

        # if not parserResults:
        #     abort(404, message="No json string or file passed in. It must be parsed first before putting it into database. Please call get function within JsonParser first.")
        # if (parserResults[0] == True):
        #     writeToDataBase = input_data_parser.write_to_database(parserResults)
        #     return {"success": writeToDataBase[0],
        #             "message": writeToDataBase[1]}
        # else:
        #     return {"success": parserResults[0],
        #             "message": parserResults[1] + "Therefore, nothing is written to database. Please correct your json input first."}


api.add_resource(HomePage, "/")
api.add_resource(JsonParser, "/parser/<string:json_string>")
api.add_resource(SendToDatabase, "/database/<string:json_string>")


if __name__ == "__main__":
    application.run(debug=True)