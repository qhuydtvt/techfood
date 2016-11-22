from bson import ObjectId
from flask import Flask, request

from questions import Question, QuestionCollection
from versions import Version
from question_packs import QuestionPack, QuestionPackCollection
from users import User
import json
from flask import request
import mongoengine


from mlab import  *

mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

app = Flask(__name__)

def remove_dollar_sign(s):
    OLD_OID = "$oid"
    NEW_OID = "oid"
    return s.replace(OLD_OID, NEW_OID)

@app.route('/api/login', methods=["POST"])
def login():
    form = request.form
    user_name = form['username']
    password = form['password']
    if user_name == "admin" and password == "12345678":
        return json.dumps({ "result_code" : 1, "message" : "Success" })
    else:
        return json.dumps({"result_code" : 0, "message" : "Failure" })

@app.route('/api/food')
def get_food():
    return json.dumps(
                           [
                               {"name" : "Pizza",
                                "detail":"Large pizza",
                                "price": 100000,
                                "image": "https://d2mekbzx20fc11.cloudfront.net/uploads/Peri-Peri-new-3001.png"},

                               {"name": "Humbuger",
                                "detail": "Large Humbuger",
                                "price": 50000,
                                "image": "https://s-media-cache-ak0.pinimg.com/originals/64/b4/bd/64b4bdd1475b0cda9f6f8de6bfc635f9.jpg"},

                               {"name": "Salad",
                                "detail": "Good salad",
                                "price": 25000,
                                "image": "https://s-media-cache-ak0.pinimg.com/564x/51/1b/2e/511b2e9b62016d362025b601195aba0f.jpg"},

                               {"name": "Taco",
                                "detail": "Lovely taco",
                                "price": "20000 VND",
                                "image": "https://s-media-cache-ak0.pinimg.com/originals/5e/53/33/5e5333408376aa88abd5980d873eb180.jpg"},

                               {"name": "Apple juice",
                                "detail": "Delicious apple juice",
                                "price": "10000 VND",
                                "image": "http://cdn.girlishh.com/wp-content/uploads/2013/09/apple-juice.jpg"}
                               ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9696)
