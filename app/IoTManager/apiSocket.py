import flask
import os
from main import Item

class ApiSocket:
    def __init__(self):
        self.app = flask.Flask(__name__)
        self.receiveData()

    def database_connection(self):
        # connect to the database

        return


    def receiveData(self):
        @self.app.route("/registerDevice", methods=["POST"])
        def handle_request():
            macAddress = flask.request.json["macAddress"]
            if macAddress is None:
                return {"status": "error not authorized for registration"}, 403
            else:
                # make a new item in the no-sql database
                Item.meters.registerMeter(Item.meters,"placeholder")
            # TODO: Implement your logic here
            # item.registerMeter(item.id)
            return {"status": "success"}, 200


        handle_request()

        @self.app.route("/getMeterData", methods=["GET"])
        def getMeterData():
            return

    def run(self):
        # Use environment variable for host, defaulting to 0.0.0.0 for container networking
        # In production, this should be controlled via container orchestration
        host = os.getenv('FLASK_HOST', '0.0.0.0')
        port = int(os.getenv('FLASK_PORT', '5000'))
        debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
        self.app.run(debug=debug, port=port, host=host)
