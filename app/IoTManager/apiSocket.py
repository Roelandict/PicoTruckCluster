import flask
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
        self.app.run(debug=False, port=5000, host="0.0.0.0")
