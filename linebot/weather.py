import requests
import json

CWB_OD_TOKEN = "CWB-D35B0C7F-A6E3-4B73-A819-CB292C69326F"
CWB_OD_URL = "https://opendata.cwb.gov.tw/"

def get_annoucement():
    annoucement_api_with_location = CWB_OD_URL + "api/v1/rest/datastore/W-C0033-001"
    params = {
        "Authorization": CWB_OD_TOKEN,
        "locationName": "新北市"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.get(annoucement_api_with_location, headers=headers, params=params)
    res_json = json.loads(response.text)
    return_data = list()
    for res_data in res_json['records']['location']:
        if not res_data['hazardConditions']['hazards']:
            continue
        for r in res_data['hazardConditions']['hazards']:
            announcement =   r['info']['phenomena'] + r['info']['significance']
            start_time =  r['validTime']['startTime'] 
            end_time =  r['validTime']['endTime'] 
            the_annoucement_message = "\n".join([announcement, "開始時間: " + start_time, "結束時間: " + end_time])
            return_data.append(the_annoucement_message)

    if not return_data:
        return {"text": "目前沒有天氣警特報資料"}
    return {"text": "\n\n".join(return_data)}