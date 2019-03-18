import requests as re
import json

uri = 'http://openapi.tuling123.com/openapi/api/v2'
jsonData ={
	"reqType":0,
    "perception": {
        "inputText": {
            "text": "给爷讲一个笑话"
        }
    },
    "userInfo": {
        "apiKey": "af1f11a39b5c4892a7774106a5ea0ae1",
        "userId": "417057",
        "userIdName": "柒小"
    }
}

response = re.post(uri,json=jsonData)
values = json.loads(response.text)['results']
value = values[0]['values']['text']
print(value)