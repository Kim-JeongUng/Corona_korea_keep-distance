# 좌표로 시 찾기
# 카카오 API 활용

import requests
import json
import GPS_searchLat_Lng

# 매일 GPS 기록 저장
import pandas as pd
import datetime


APP_KEY = 'b3c7423bf62d904aad46bea35d6db181'    # 발급받은 키 입력

url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=%s&y=%s"%(GPS_searchLat_Lng.my_lng, GPS_searchLat_Lng.my_lat)
headers = {"Authorization": "KakaoAK b3c7423bf62d904aad46bea35d6db181"}
api_test = requests.get(url, headers=headers)
url_text = json.loads(api_test.text)

my_region2 = url_text['documents'][0]['region_2depth_name']
my_region3 = url_text['documents'][0]['region_3depth_name']


# GPS 기록저장

df = pd.read_excel('areaLog.xlsx', index_col =[0])

today = datetime.datetime.now()
today = today.strftime("%Y%m%d")

# 만약 마지막에 저장한 값과 달라질경우(지역의 이동 또는 날짜의 변경) 엑셀 저장
if not (df.iloc[-1]['my_region3'] == my_region3 or df.iloc[-1]['date'] == today):
    data ={
        'date': [today],
        'my_region2': [my_region2],
        'my_region3': [my_region3]
    }

    new_df = pd.DataFrame(data)

    # 이전 데이터와 새로운 데이터를 합침
    df = pd.concat([df,new_df])

    df.to_excel('areaLog.xlsx')




