from bson import ObjectId
from flask import Flask

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

@app.route('/api/food')
def get_food():
    return json.dumps({"items":
                           [
                               {"name" : "Pizza",
                                "detail":"Large pizza",
                                "price": "100000 VND",
                                "image": "https://www.cicis.com/media/1138/pizza_trad_pepperoni.png"},

                               {"name": "Humbuger",
                                "detail": "Large Humbuger",
                                "price": "50000 VND",
                                "image": "http://www.awok.co.jp/wp/wp-content/uploads/2014/07/humberger-01.png"},

                               {"name": "Salad",
                                "detail": "Good salad",
                                "price": "25000 VND",
                                "image": "http://images.bigoven.com/image/upload/t_recipe-256/avocado-tomato-salad-534a1f.jpg"},

                               {"name": "Taco",
                                "detail": "Lovely taco",
                                "price": "20000 VND",
                                "image": "http://pix.iemoji.com/images/emoji/apple/ios-9/256/taco.png"},

                               {"name": "Apple juice",
                                "detail": "Delicious apple juice",
                                "price": "10000 VND",
                                "image": "https://dtgxwmigmg3gc.cloudfront.net/files/53a93526e1272f237300787c-icon-256x256.png"}
                               ]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9696)

