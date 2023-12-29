- 其他範例

  - LocationSendMessage
  ```python
      latitude = violation.latitude if violation.latitude else 25.198444
      longitude = violation.longitude if violation.longitude else 121.43387
      address = violation.address if violation.address else "UNKNOWN"
      # LocationSendMessage Need address, latitude, longitude not None
      location_message = LocationSendMessage(
          title=violation.messages,
          address=address,
          latitude=latitude,
          longitude=longitude
      )
  ```

  - 傳送訊息給特定群組 or user

  ```python
  line_bot_api.push_message(to=f"{group token}", messages=location_message)
  ```

  - flex message 範例

  ```python
  message = "地點"
    msg = "範例訊息2"
    body_contents = [
        {
            "type": "text",
            "text": message,
            "weight": "bold",
            "size": "xl"
        },
        {
            "type": "box",
            "layout": "baseline",
            "margin": "md",
            "contents": [],
        },
        {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Event",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": msg,
                            "wrap": True,
                            "color": "#666666",
                            "size": "sm",
                            "flex": 5
                        },
                    ],
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Time",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": "2023-12-29 08:00:00",
                            "wrap": True,
                            "color": "#666666",
                            "size": "sm",
                            "flex": 5
                        },
                    ],
                },
            ],
        },
    ]
    location_message = message

    footer_contents = [
        {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "message",
                        "label": "前往查看",
                        "text": f"前往{location_message}查看",
                    },
                },
            ],
        },
    ]

    hero = dict()
    hero["type"] = "image"
    hero["url"] = "{url}"
    hero["size"] = "full"
    hero["aspectRatio"] = "20:13"
    hero["aspectMode"] = "cover"

    bubble_container = BubbleContainer(
                    direction='ltr',
                    hero=hero,
                    body={
                        'type': 'box',
                        "layout": "vertical",
                        "contents": body_contents,
                    },
                    footer={
                        'type': 'box',
                        "layout": "vertical",
                        "contents": footer_contents,
                    },   
                )
    flex_message = FlexSendMessage(
                    alt_text=message,
                    contents=bubble_container,
                )
  line_bot_api.push_message(to=f"{group token}", messages=flex_message)
  ```` 