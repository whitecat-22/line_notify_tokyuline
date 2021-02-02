# postリクエストをline notify APIに送るためにrequestsのimport
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import slackweb

# webdriverの設定
option = Options()
option.add_argument('--incognito')
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)
driver.get("https://www.tokyu.co.jp/unten2/unten.html")
# webdriverにて情報を取得
elem_search_content = driver.find_elements_by_class_name("line-info_detail")

# lineに通知したいメッセージを入力
content_text = []
for i in range(8):
    content_text.append(elem_search_content[i].text)

notification_message = '\n\n'.join(content_text)

driver.close()

# line：token.txtからトークンの読み込み
with open('token.txt', 'r') as f:
	token = f.read().strip()
# print(token)
# line notify APIのトークンの読み込み
line_notify_token = token
# line notify APIのエンドポイントの設定
line_notify_api = 'https://notify-api.line.me/api/notify'
# ヘッダーの指定
headers = {'Authorization': f'Bearer {line_notify_token}'}
# 送信するデータの指定
data = {'message': f'{notification_message}'}
# line notify apiにpostリクエストを送る
requests.post(line_notify_api, headers=headers, data=data)

"""
slack = slackweb.Slack(url="<Webhook URL>")
slack.notify(text=content_text)
"""
