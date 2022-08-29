import requests
import json

slack_webhook_url = "https://hooks.slack.com/services/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"     # slack에서 생성된 webhook url

def sendSlackWebhook(strText):      # webhook 방식으로 메세지를 보내는 함수
    headers = {
        "Contetnt-type": "application/json"
    }
    
    data = {
        "text" : strText
    }
    
    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
    
    if res.status_code == 200 :
        return "ok"
    else :
        return "error"
    
print(sendSlackWebhook("안녕하세요. 파이썬에서 보내는 메세지 입니다."))