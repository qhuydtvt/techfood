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
                                "price": 100,
                                "image": "https://d2mekbzx20fc11.cloudfront.net/uploads/Peri-Peri-new-3001.png"},

                               {"name": "Humbuger",
                                "detail": "Large Humbuger",
                                "price": 50,
                                "image": "https://s-media-cache-ak0.pinimg.com/originals/64/b4/bd/64b4bdd1475b0cda9f6f8de6bfc635f9.jpg"},

                               {"name": "Salad",
                                "detail": "Good salad",
                                "price": 25,
                                "image": "https://s-media-cache-ak0.pinimg.com/564x/51/1b/2e/511b2e9b62016d362025b601195aba0f.jpg"},

                               {"name": "Taco",
                                "detail": "Lovely taco",
                                "price": 20,
                                "image": "https://s-media-cache-ak0.pinimg.com/originals/5e/53/33/5e5333408376aa88abd5980d873eb180.jpg"},

                               {"name": "Apple juice",
                                "detail": "Delicious apple juice",
                                "price": 10,
                                "image": "http://cdn.girlishh.com/wp-content/uploads/2013/09/apple-juice.jpg"}
                               ])
@app.route("/api/salon")
def get_salon():
    return json.dumps({
  "d": [
    {
      "Id": 3,
      "Name": "82 Trần Đại Nghĩa, HN",
      "Phone": "0906.206.804",
      "Fanpage": "https://www.facebook.com/30Shine82tdn/",
      "FanpageId": "459230314265092",
      "ManagerName": "Quản lý 82 Trần Đại Nghĩa",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN1-jXMZdf.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN1-jXMZdfx350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN2-vvtQrt.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN2-vvtQrtx350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN3-3eInlo.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN3-3eInlox350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/8/5/82-Tran-dai-nghia-EdovYK-4uOogZ.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/8/5/82-Tran-dai-nghia-EdovYK-4uOogZx350.jpg",
          "title": "",
          "description": ""
        }
      ]
    },
    {
      "Id": 5,
      "Name": "702 Đường Láng, HN",
      "Phone": "0888228702",
      "Fanpage": "https://www.facebook.com/30Shine702dl/",
      "FanpageId": "237581956634057",
      "ManagerName": "Quản lý 702 Đường Láng",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN1-jXMZdf.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN1-jXMZdfx350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN2-vvtQrt.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN2-vvtQrtx350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN3-3eInlo.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN3-3eInlox350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/8/5/702-Duong-Lang-Ca1zwd-KLzPhO.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/8/5/702-Duong-Lang-Ca1zwd-KLzPhOx350.jpg",
          "title": "",
          "description": ""
        }
      ]
    },
    {
      "Id": 2,
      "Name": "346 Khâm Thiên, HN",
      "Phone": "0947.602.605",
      "Fanpage": "https://www.facebook.com/30Shine346kt/",
      "FanpageId": "992375274119367",
      "ManagerName": "Quản lý 346 Khâm Thiên",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/Khamthien1-eKdKat.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/Khamthien1-eKdKatx350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/Khamthien2-IJkLNK.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/Khamthien2-IJkLNKx350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/Khamthien3-nY2Icy.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/Khamthien3-nY2Icyx350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/8/5/346-Kham-Thien-OZmbBr-dNdFxe.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/8/5/346-Kham-Thien-OZmbBr-dNdFxex350.jpg",
          "title": "",
          "description": ""
        }
      ]
    },
    {
      "Id": 4,
      "Name": "235 Đội Cấn, HN",
      "Phone": "0888.684.235",
      "Fanpage": "https://www.facebook.com/30shine235dc/",
      "FanpageId": "120119718385438",
      "ManagerName": "Quản lý 235 Đội Cấn",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/Doican1-RuevtT.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/Doican1-RuevtTx350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/Doican2-Umajzj.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/Doican2-Umajzjx350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/Doican3-BQPEcE.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/Doican3-BQPEcEx350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/8/5/235-Doi-Can-pnm2bL-lTmETQ.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/8/5/235-Doi-Can-pnm2bL-lTmETQx350.jpg",
          "title": "",
          "description": ""
        }
      ]
    },
    {
      "Id": 7,
      "Name": "136 Hùng Vương-Q10-HCM",
      "Phone": "0917.269.810",
      "Fanpage": "https://www.facebook.com/30Shine136HV/",
      "FanpageId": "1764458343814973",
      "ManagerName": "Quản lý 136 Hùng Vương",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN1-jXMZdf.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/22/TDN1-jXMZdfx350.jpg",
          "title": "",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/11/7/136-HV-DMbs4s.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/11/7/136-HV-DMbs4sx350.jpg",
          "title": "",
          "description": ""
        }
      ]
    }
  ]
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9696)
