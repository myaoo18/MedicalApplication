import input_data_parser
from flask import Flask, request, abort
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

parserResults = []

class JsonParser(Resource):
    @app.route('/parser/')
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
    @app.route('/database/')
    def post(self, json_string):
        if not parserResults:
            abort(404, message="No json string or file passed in. It must be parsed first before putting it into database. Please call get function within JsonParser first.")
        if (parserResults[0] == True):
            writeToDataBase = input_data_parser.write_to_database(parserResults)
            return {"success": writeToDataBase[0],
                    "message": writeToDataBase[1]}
        else:
            return {"success": parserResults[0],
                    "message": parserResults[1] + "Therefore, nothing is written to database. Please correct your json input first."}

api.add_resource(JsonParser, "/parser/<string:json_string>")
api.add_resource(SendToDatabase, "/database/<string:json_string>")

if __name__ == "__main__":
    app.run(debug=True)