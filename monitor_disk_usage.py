# 필요 라이브러리
import psutil
from slack_sdk import WebClient
import json

# 디스크 사용량 통계
usage = psutil.disk_usage('/')

# 사용량이 90% 이상일 때
if usage.percent > 90:
    
    # 슬랙 알림
    client = WebClient(token='Your_Token')
        
    message = [{
                    "type": "section",
                    "text": {
                                "type": "mrkdwn",
                                "text": "⚠️ AWS EC2 Airflow Server의 잔여 Disk 용량이 10% 미만입니다. ⚠️"
                            }
                }]
    
    client.chat_postMessage(channel="Your_Channel", blocks=json.dumps(message))