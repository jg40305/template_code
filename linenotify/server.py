from flask import Flask, request
import json
import requests
import urllib

# Get parameters of server
with open("config.json", "r") as fopen:
    config = json.load(fopen)

# Declare LINE Notify Client Config
CLIENT_ID = config.get("client_id")
CLIENT_SECRET = config.get("client_secret")
LINE_NOTIFY_BOT = config.get("line_notify_bot")
LINE_NOTIFY_API = config.get("line_notify_api")
REDIRECT_URI = config.get("redirect_uri")

# Server Entrypoint
app = Flask()


def get_access_token():
    with open("code-state.txt", "r") as fopen:
        content = json.load(fopen)
        code = content.get("code")
    urlencode_uri = urllib.parse.quote_plus(REDIRECT_URI)
    payload = (
        f"grant_type=authorization_code"
        f"&code={code}"
        f"&redirect_uri={urlencode_uri}"
        f"&client_id={CLIENT_ID}"
        f"&client_secret={CLIENT_SECRET}"
    )
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(
        f"{LINE_NOTIFY_BOT}/oauth/token", data=payload, headers=headers
    )
    with open("log.txt", "a") as fwrite:
        fwrite.write(
            f"status_code:{response.status_code}, text: {response.text}, payload: {payload}"
        )
    if response.status_code >= 400:
        raise Exception
    with open("access_token", "w") as fw:
        fw.write(response.json().get("access_token"))
    return response.json().get("access_token")


def check_expired_access_token():
    status_uri = "api/status"
    with open("access_token", "r") as fop:
        access_token = fop.read().strip()
    return access_token


@app.post("/callback")
def callback():
    code = request.params.get("code")
    state = request.params.get("state")
    with open("code-state.txt", "w") as fwrite:
        json.dump({"code": code, "state": state}, fwrite)
    get_access_token()
    return "success"


@app.get("/get_notify_regis_url")
def get_notify_regis_url():
    return (
        f"{LINE_NOTIFY_BOT}"
        f"/oauth/authorize"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=notify"
        f"&state=SomethingPreventCSRF"
        f"&response_mode=form_post"
    )


if __name__ == '__main__':
    app.run(host=0.0.0.0, port=8000, debug=True)