# poetry add flask-restful
# https://devqa.io/curl-sending-api-requests/

# to test:
# curl http://127.0.0.1:5000/gta/4
# curl -X PUT -H "Content-Type: application/json" \
    # -d '{"userId": 5, "text": "Salamalekum aga!", "lang": "kz"}' \
    # http://127.0.0.1:5000/gta/5
# curl -X POST -H "Content-Type: application/json" \
    # -d '{"userId": 10, "text": "Minecraft", "lang": "rrr"}' \
    # http://127.0.0.1:5000/gta/10



import random
from flask import Flask
from flask_restful import Api, Resource, reqparse

my_list = [
    {
        "id": 1,
        "text": "Великая кража автомобилей V",
        "lang": "ru"
    },
    {
        "id": 2,
        "text": "侠盗猎车手V",
        "lang": "ch"
    },
    {
        "id": 3,
        "text": "Grand Theft Auto V",
        "lang": "en"
    },
    {
        "id": 4,
        "text": "Der große Diebstahl von Autos V",
        "lang": "de"
    },
    {
        "id": 6,
        "text": "Uzurbek, kalaisin ba?",
        "lang": "uzb"
}
]

class GTAResource(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(my_list), 200
        for val in my_list:
            if (val["id"] == id):
                return val, 200
        return "Warning! Can't find text! )))", 404

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("text")
        parser.add_argument("lang")
        params = parser.parse_args()
        for val in my_list:
            if id == val["id"]:
                val["text"] = params["text"]
                val["lang"] = params["lang"]
                return val, 200
        val = {
            "id": id,
            "text": params["text"],
            "text": params["lang"]
        }
        my_list.append(val)
        return val, 201

def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("text")
        parser.add_argument("lang")
        params = parser.parse_args()
        for val in my_list:
            if id == val["id"]:
                return f"This text with id={id} already exists", 400
        val = {
            "id": id,
            "text": params["text"],
            "text": params["lang"]
        }
        my_list.append(val)
        return val, 201

def delete(self, id):
    global my_list
    my_list = [val for val in my_list if val["id"] != id]
    return f"Record with id={id} was deleted!", 200


if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(GTAResource, "/gta", "/gta/", "/gta/<int:id>")
    app.run(debug=True)