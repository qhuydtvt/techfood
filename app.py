from __future__ import unicode_literals

from bson import ObjectId
from flask import Flask, request, session
from questions import Question, QuestionCollection
from versions import Version
from question_packs import QuestionPack, QuestionPackCollection
from user import User
from usertoken import UserToken
import json
from flask import request
import mongoengine

import youtube_dl
from flask_restful import Resource, Api, reqparse
from todo import ToDo
import json
import hmac

LOGIN_ENABLED = False

from mlab import  *

mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

app = Flask(__name__)
app.config['SECRET_KEY'] = "y9rWGS|*d2[OBzOL0O6W\"8Mq8{esk6"

api = Api(app)

def remove_dollar_sign(s):
    OLD_OID = "$oid"
    NEW_OID = "oid"
    return s.replace(OLD_OID, NEW_OID)

# @app.route('/api/login', methods=["POST"])
# def login():
#     form = request.form
#     user_name = form['username']
#     password = form['password']
#     if user_name == "admin" and password == "12345678":
#         return json.dumps({ "result_code" : 1, "message" : "Success" })
#     else:
#         return json.dumps({"result_code" : 0, "message" : "Failure" })

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

@app.route("/api/hairstyle")
def hairstyle():
  return json.dumps({
  "d": [
    {
      "Id": 1,
      "Title": "Slick-back Undercut",
      "Description": "Kiểu tóc phô trương vẻ nam tính và lịch lãm với phần mái chuốt dài ra phía sau",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_1-OJgL32.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_1-OJgL32x350.jpg",
          "title": "1",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_2-S4ahWr.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_2-S4ahWrx350.jpg",
          "title": "2",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_3-oEHwAs.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_3-oEHwAsx350.jpg",
          "title": "3",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_4-wUwfX1.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_4-wUwfX1x350.jpg",
          "title": "4",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_5-kMXfFb.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_5-kMXfFbx350.jpg",
          "title": "5",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_6-M4cGVg.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_6-M4cGVgx350.jpg",
          "title": "6",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_7-wByPUM.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_7-wByPUMx350.jpg",
          "title": "7",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_8-g22xHP.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Slick-back-Undercut_8-g22xHPx350.jpg",
          "title": "8",
          "description": ""
        }
      ]
    },
    {
      "Id": 2,
      "Title": "Side-swept Undercut",
      "Description": "Undercut với mái vuốt lệch về một bên, kết hợp giữa sự khỏe khoắn cùng nét phá cách tự nhiên",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_1-LY3KBi.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_1-LY3KBix350.jpg",
          "title": "1",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_2-qMuIwe.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_2-qMuIwex350.jpg",
          "title": "2",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_3-AMHbvM.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_3-AMHbvMx350.jpg",
          "title": "3",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_4-pqyQZa.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_4-pqyQZax350.jpg",
          "title": "4",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_5-JKtQnu.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_5-JKtQnux350.jpg",
          "title": "5",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_6-SbBYqv.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_6-SbBYqvx350.jpg",
          "title": "6",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_7-ChIQUZ.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_7-ChIQUZx350.jpg",
          "title": "7",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_8-TvsBbr.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-swept-Undercut_8-TvsBbrx350.jpg",
          "title": "8",
          "description": ""
        }
      ]
    },
    {
      "Id": 3,
      "Title": "Quiff Undercut",
      "Description": "Mái vuốt bồng cầu kỳ tương phản với mai và gáy cắt gọn gàng",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_1-FPHlZa.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_1-FPHlZax350.jpg",
          "title": "1",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_2-uKgO2s.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_2-uKgO2sx350.jpg",
          "title": "2",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_3-EHjaIk.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_3-EHjaIkx350.jpg",
          "title": "3",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_4-dTwtwl.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_4-dTwtwlx350.jpg",
          "title": "4",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_5-2JBOUQ.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_5-2JBOUQx350.jpg",
          "title": "5",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_6-DsCPRC.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_6-DsCPRCx350.jpg",
          "title": "6",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_7-heRMOA.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_7-heRMOAx350.jpg",
          "title": "7",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_8-VGwsZw.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Quiff-Undercut_8-VGwsZwx350.jpg",
          "title": "8",
          "description": ""
        }
      ]
    },
    {
      "Id": 4,
      "Title": "Long-top Quiff",
      "Description": "Bộ sưu tập hot nhất của Long-top Quiff",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_1-MDL1Az.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_1-MDL1Azx350.jpg",
          "title": "1",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_2-ozHmFX.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_2-ozHmFXx350.jpg",
          "title": "2",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_3-f1ZfIL.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_3-f1ZfILx350.jpg",
          "title": "3",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_4-IORxKm.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_4-IORxKmx350.jpg",
          "title": "4",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_5-xVQKGT.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_5-xVQKGTx350.jpg",
          "title": "5",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_6-uCFhsS.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_6-uCFhsSx350.jpg",
          "title": "6",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_7-fb3DWu.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_7-fb3DWux350.jpg",
          "title": "7",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_8-RY2FIq.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Long-top-Quiff_8-RY2FIqx350.jpg",
          "title": "8",
          "description": ""
        }
      ]
    },
    {
      "Id": 5,
      "Title": "Side Part",
      "Description": "Ngôi lệch kinh điển không bao giờ lỗi mốt",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_1-ydsZpU.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_1-ydsZpUx350.jpg",
          "title": "1",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_2-RjJMgC.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_2-RjJMgCx350.jpg",
          "title": "2",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_3-oIUQZR.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_3-oIUQZRx350.jpg",
          "title": "3",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_4-gNjWm2.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_4-gNjWm2x350.jpg",
          "title": "4",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_5-3BLof1.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_5-3BLof1x350.jpg",
          "title": "5",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_6-hNMhMw.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_6-hNMhMwx350.jpg",
          "title": "6",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_7-G1tuaJ.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_7-G1tuaJx350.jpg",
          "title": "7",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_8-EY3psT.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Side-Part_8-EY3psTx350.jpg",
          "title": "8",
          "description": ""
        }
      ]
    },
    {
      "Id": 6,
      "Title": "Middle Part",
      "Description": "Tóc ngôi giữa đang được các chàng trai Hàn mang trở lại trẻ trung và lịch lãm",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_1-wktd2M.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_1-wktd2Mx350.jpg",
          "title": "1",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_2-Rs2yGz.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_2-Rs2yGzx350.jpg",
          "title": "2",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_3-NrH2Nc.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_3-NrH2Ncx350.jpg",
          "title": "3",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_4-l1iVEw.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_4-l1iVEwx350.jpg",
          "title": "4",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_5-cjymev.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_5-cjymevx350.jpg",
          "title": "5",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_6-gQMqai.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_6-gQMqaix350.jpg",
          "title": "6",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_7-dkoAUL.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_7-dkoAULx350.jpg",
          "title": "7",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_8-yG3wJC.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Middle-Part_8-yG3wJCx350.jpg",
          "title": "8",
          "description": ""
        }
      ]
    },
    {
      "Id": 7,
      "Title": "Sport",
      "Description": "Năng động và khỏe khoắn với các kiểu Sport/Short-Quiff",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_1-oxjvAb.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_1-oxjvAbx350.jpg",
          "title": "1",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_2-ltG3iH.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_2-ltG3iHx350.jpg",
          "title": "2",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_3-k4EBtS.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_3-k4EBtSx350.jpg",
          "title": "3",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_4-zNfLw2.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_4-zNfLw2x350.jpg",
          "title": "4",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_5-quOuDX.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_5-quOuDXx350.jpg",
          "title": "5",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_6-GjtHBN.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_6-GjtHBNx350.jpg",
          "title": "6",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_7-xNKnHv.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_7-xNKnHvx350.jpg",
          "title": "7",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_8-dkyeeD.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Sport_8-dkyeeDx350.jpg",
          "title": "8",
          "description": ""
        }
      ]
    },
    {
      "Id": 8,
      "Title": "Layer",
      "Description": "Layer lãng tử",
      "Images": [
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_1-K3mQMn.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_1-K3mQMnx350.jpg",
          "title": "1",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_2-wQF3sT.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_2-wQF3sTx350.jpg",
          "title": "2",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_3-ZpiyHj.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_3-ZpiyHjx350.jpg",
          "title": "3",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_4-PqeMV1.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_4-PqeMV1x350.jpg",
          "title": "4",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_5-QlqRrf.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_5-QlqRrfx350.jpg",
          "title": "5",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_6-YPQmjE.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_6-YPQmjEx350.jpg",
          "title": "6",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_7-ucaBFv.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_7-ucaBFvx350.jpg",
          "title": "7",
          "description": ""
        },
        {
          "url": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_8-ZEGBbr.jpg",
          "thumb": "http://ql.30shine.com/Public/Media/Upload/Images/Common/2016/7/25/Layer_8-ZEGBbrx350.jpg",
          "title": "8",
          "description": ""
        }
      ]
    }
  ]
})

# {
# Phone : '09123123123',
# CustomerName : 'Test API',
# Email : 'testapi@gmail.com',
# Password : 'api123',
# DayOfBirth : 20,
# MonthOfBirth : 10,
# YearOfBirth : 1999
# }

# @app.route("/api/register", methods=["POST"])
# def register():
#   json_data = request.get_json()
#   phone = json_data["Phone"]
#   customerName = json_data["CustomerName"]
#   email = json_data["Email"]
#   password = json_data["Password"]
#   day_of_birth = json_data["DayOfBirth"]
#   month_of_birth = json_data["MonthOfBirth"]
#   year_of_birth = json_data["YearOfBirth"]
#
#   return json.dumps({
#   "d": {
#     "Id": 83181,
#     "Phone": phone,
#     "CustomerName": customerName,
#     "Email": email,
#     "AccessToken": "xxxxooooo",
#     "DayOfBirth": day_of_birth,
#     "MonthOfBirth": month_of_birth,
#     "YearOfBirth": year_of_birth
#   }
# })

@app.route("/api/company")
def company():
  return json.dumps(
    {
      "content" : {
          "author" : {
              "name": "TechKids connect",
              "url": "http://techkids.vn"
          },
          "items": [
              {
                  "name": "FPT Software",
                  "phone": "+84473007575",
                  "website": "https://www.fpt-software.com",
                  "images": [
                      {
                          "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/LogoFSO1.jpg/220px-LogoFSO1.jpg",
                          "type": "logo"
                      },
                      {
                          "url": "http://www.reviewcompany.vn/public/media/uploads/company/gallery/2014-08-18/watermarked/c75bddabea3d35f812f2f45389ce05e0de18bf24.jpg",
                          "type": "picture"
                      }
                  ]
              },
              {
                  "name": "EWay",
                  "phone": "+84432595450",
                  "website": "https://eway.vn",
                  "images": [
                      {
                          "url": "https://e27.co/img/startups/6595/logo-1443495246.png",
                          "type": "logo"
                      },
                      {
                          "url": "https://officesnapshots.com/wp-content/uploads/2015/08/eway-office-design-2.jpg",
                          "type": "picture"
                      }
                  ]
              },
              {
                  "name": "BraveBits",
                  "phone": "+84463260066",
                  "website": "http://www.bravebits.co/",
                  "images": [
                      {
                          "url": "http://i.imgur.com/8ONaQnl.png",
                          "type": "logo"
                      },
                      {
                          "url": "http://www.bravebits.co/wp-content/uploads/2016/01/gallery_1-1024x683.jpg",
                          "type": "picture"
                      }
                  ]
              }
          ]

        }

    }
  )

@app.route("/api/youtube")
def youtube():
    ydl_opts = {}
    args = request.args
    if "url" in args:
        url = args["url"]
    else:
        url = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        vid_info = ydl.extract_info(url=url, download=False)
        return json.dumps(vid_info)

@app.route("/api/soundcloud")
def soundcloud():
    args = request.args
    if "url" in args:
        url = args["url"]
    else:
        url = 'https://soundcloud.com/svtoprod/son-tung-mtp-chung-ta-khong-thuoc-ve-nhau-svto-x-kk-bootleg'
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        vid_info = ydl.extract_info(url=url, download=False)
        return json.dumps(vid_info)

parser = reqparse.RequestParser()
parser.add_argument('id', type=str, help='Id of the note')
parser.add_argument('title', type=str, help='Title of the note')
parser.add_argument('content', type=str, help='Content of the note')
parser.add_argument("color", type=str, help='Color of the note')
parser.add_argument("time_in_total", type=str, help='Color of the note')
parser.add_argument("time_left", type=str, help='Color of the note')
parser.add_argument("completed", type=bool, help='Color of the note')
parser.add_argument('username', type=str, help='Username of noter')
parser.add_argument('password', type=str, help='Password of noter')
parser.add_argument('token', type=str, help='Token of noter', location="headers")

class ToDoRes(Resource):
  def get(self, todo_id):
    args = parser.parse_args()
    username = username_from(args["token"])
    if LOGIN_ENABLED and username is None:
      return {"result":0, "message": "Token not valid"}, 401
    return json.loads(ToDo.objects(username=username, id=todo_id).first().to_json())

# TODO
  def delete(self, todo_id):
    args = parser.parse_args()
    username = username_from(args["token"])
    if username is None:
      return {}, 401
    ToDo.objects(username=username, id=todo_id).first().delete()
    return {"result": 1, "message": "DELETED"}, 200

# TODO
  def put(self, todo_id):
    args = parser.parse_args()
    title = args["title"]
    content = args["content"]
    color = args["color"]
    completed = args["completed"]
    username = username_from(args["token"])
    if username is None:
      return {}, 401
    to_do = ToDo.objects(username=username, id=todo_id).first()
    to_do.update(set__title=title, set__content=content, set__color=color, set__completed=completed)
    return json.loads(to_do.to_json()), 200

class ToDoListRes(Resource):
  def get(self):
    args = parser.parse_args()
    if LOGIN_ENABLED:
      token = args["token"]
      if token not in session:
        return [], 401
      username = session[token]
      return [json.loads(to_do.to_json()) for to_do in ToDo.objects(username=username).exclude("username")]
    else:
      return [json.loads(to_do.to_json()) for to_do in ToDo.objects().exclude("username")]

  def post(self):
    args = parser.parse_args()
    token = args["token"]
    title = args["title"]
    content = args["content"]
    color = args["color"]
    if LOGIN_ENABLED:

      username = username_from(token)
      if LOGIN_ENABLED and username is None:
        return {"result": 0, "message": "Not authenticated"}, 401
      new_to_do = ToDo(title=title, content=content, color=color, username=username)
      new_to_do.save()
      return json.loads(ToDo.objects(username=username, id=new_to_do.id).exclude("username").to_json()), 201
    else:
      new_to_do = ToDo(title=title, content=content, color=color, username="")
      new_to_do.save()
      return json.loads(ToDo.objects(id=new_to_do.id).exclude("username").to_json()), 201

class V2ToDoListRes(Resource):
  def get(self):
    args = parser.parse_args()
    username = username_from(args["token"])
    if username is None:
        return {"token": args["token"]}, 401
    return [json.loads(to_do.to_json()) for to_do in ToDo.objects(username=username).exclude("username")]

  def post(self):
    args = parser.parse_args()
    token = args["token"]
    title = args["title"]
    content = args["content"]
    color = args["color"]
    username = username_from(token)
    if LOGIN_ENABLED and username is None:
        return {"result": 0, "message": "Not authenticated"}, 401
    new_to_do = ToDo(title=title, content=content, color=color, username=username)
    new_to_do.save()
    return json.loads(ToDo.objects(username=username, id=new_to_do.id).exclude("username").to_json()), 201

class RegisterRes(Resource):
  def post(self):
    args = parser.parse_args()
    username = args["username"]
    password = args["password"]
    found_user = User.objects(username=username).first()
    if found_user is not None:
      return {"result": 0, "message": "User already exists"}, 400
    user = User(username = username, password = password)
    user.save()
    return {"result": 1, "message": "Registered"}, 201

class LoginRes(Resource):
  def post(self):
    args = parser.parse_args()
    username = args["username"]
    password = args["password"]
    user = User.objects(username=username).first()
    if user is None:
      print("Could not find user")
      return {"result": 0, "message": "User doesn't exist"}, 401
    if password != user.password:
      print("user name and password mismatch")
      return {"result": 0, "message": "User or password doesn't match"}, 401

    token = hmac.new(str.encode(username)).hexdigest()
    session[token] = user_name
    return {"result": 1, "message": "Logged in", "token": token}, 201

api.add_resource(ToDoListRes, "/api/todos")
api.add_resource(V2ToDoListRes, "/api/v2/todos")
api.add_resource(ToDoRes, "/api/todos/<todo_id>")
api.add_resource(RegisterRes, "/api/register")
api.add_resource(LoginRes, "/api/login")

def username_from(token):
  if token not in session:
    return None
  return session[token]

if __name__ == '__main__':
    # for todo in ToDo.objects:
    #   todo.delete()
    app.run(host='0.0.0.0', port=9696)
