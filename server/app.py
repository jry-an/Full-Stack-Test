from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.json_util import dumps, loads, ObjectId



client = MongoClient('mongodb://localhost:27017/')

mydb = client.mydb
orders = mydb.orders
id_col = orders.id


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/orders', methods=['GET'])
def all_orders():
    output = []
    for x in orders.find():
        x["_id"] = str(  x["_id"])
        output.append(x)

    return jsonify({
        'status': 'success',
        'orders': output
    })


if __name__ == '__main__':
    app.run(debug=True)