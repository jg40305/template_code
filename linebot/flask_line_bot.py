import os
import datetime
import json
import pickle
import logging
from flask import Flask, request, make_response
from linebot.models.template import CarouselColumn, CarouselTemplate, ImageCarouselColumn, ImageCarouselTemplate

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    ImageSendMessage,
    VideoSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction,
    PostbackEvent,
    PostbackTemplateAction,
    LocationSendMessage,
    FlexSendMessage,
    BubbleContainer,
)

from linebot.models.actions import CameraAction, LocationAction, URIAction
from linebot.models.send_messages import QuickReply, QuickReplyButton

from weather import get_annoucement

# 修改 access token 與 secret
# access_token: Messaging API
# secret: Basic settings
LINE_CHANNEL_ACCESS_TOKEN = ""
LINE_CHANNEL_SECRET = ""


line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(LINE_CHANNEL_SECRET)

app = Flask(__name__)

@app.route('/callback', method=["POST"])
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        events = parser.parse(body, signature)  # 傳入的事件

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                user_id = event.source.user_id  #  取得使用者 ID
                # group_id = event.source.group_id  # 如果是群組，則取得群組 ID
                print(user_id)
                print(event.reply_token)  # 取得回傳 token
                try:
                    event.message.text = event.message.text
                except AttributeError:
                    event.message.text = str()
                print(event.message.text)

                if event.message.text == "範例文字1":
                    line_bot_api.reply_message(
                        event.reply_token,  # 回傳的 token
                        TextSendMessage(text=f"{event.message.text}")
                    )

                elif event.message.text == "天氣":
                    return_dict = get_annoucement()
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=return_dict.get("text"))
                    )

                elif event.message.text == "公車":
                    image_carousel = TemplateSendMessage(
                        alt_text='Image Carousel',
                        template=ImageCarouselTemplate(
                            columns=[
                                ImageCarouselColumn(
                                    image_url='https://i.imgur.com/aAoh7iv.jpeg',
                                    action=URIAction(
                                        label='紅37',
                                        uri='https://pda.5284.gov.taipei/MQS/route.jsp?rid=16431'
                                    )
                                ),
                                ImageCarouselColumn(
                                    image_url='https://i.imgur.com/zgGSPmD.jpeg',
                                    action=URIAction(
                                        label='紅38',
                                        uri='https://pda.5284.gov.taipei/MQS/route.jsp?rid=16282'
                                    )                                
                                ),
                                ImageCarouselColumn(
                                    image_url='https://i.imgur.com/UqiQm2D.jpeg',
                                    action=URIAction(
                                        label='紅51',
                                        uri='https://pda.5284.gov.taipei/MQS/route.jsp?rid=16397'
                                    )                                
                                ),
                                ImageCarouselColumn(
                                    image_url='https://i.imgur.com/PF4yZ1o.jpeg',
                                    action=URIAction(
                                        label='863',
                                        uri='https://pda.5284.gov.taipei/MQS/route.jsp?rid=16675'
                                    )                                
                                ),
                                ImageCarouselColumn(
                                    image_url='https://i.imgur.com/7uIBcCu.jpeg',
                                    action=URIAction(
                                        label='865',
                                        uri='https://pda.5284.gov.taipei/MQS/route.jsp?rid=16530'
                                    )                                
                                ),
                                ImageCarouselColumn(
                                    image_url='https://i.imgur.com/IAoWmY5.jpeg',
                                    action=URIAction(
                                        label='867',
                                        uri='https://pda.5284.gov.taipei/MQS/route.jsp?rid=16532'
                                    )                                
                                ),
                                ImageCarouselColumn(
                                    image_url='https://i.imgur.com/t7kRYPW.jpeg',
                                    action=URIAction(
                                        label='874',
                                        uri='https://pda.5284.gov.taipei/MQS/route.jsp?rid=16535'
                                    )                                
                                )
                            ]
                        )
                    )
                    line_bot_api.reply_message(
                        event.reply_token,
                        image_carousel
                    )
    # callback NEED Return
    return ""


if __name__ == '__main__':
    app.run(host=0.0.0.0, port=8000, debug=True)