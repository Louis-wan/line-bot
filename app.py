

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('lP2nHXZoYCZCJO5HZjjkxbbDeTenaAECcNKw1TPCm4hzUOg5EcONHym8oIc3QtQeWqkAkE4sJG0wtHrHHEov649JMrkroxyXvitbU1KSNvXCbmZib+YU0ThzdqsUsv3l/chInb4je7YcfwAJ7Sk3QgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9f73d9affc4e1b17eac7fc375553b6d2')


@app.route("/callback", methods=['POST'])
def callback(): 
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()