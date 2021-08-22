# 좌표로 시 찾기
# 카카오 API 활용

import requests
import json
import GPS_searchLat_Lng

APP_KEY = 'b3c7423bf62d904aad46bea35d6db181'    # 발급받은 키 입력

url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=%s&y=%s"%(GPS_searchLat_Lng.my_lng, GPS_searchLat_Lng.my_lat)
headers = {"Authorization": "KakaoAK b3c7423bf62d904aad46bea35d6db181"}
api_test = requests.get(url,headers=headers)
url_text = json.loads(api_test.text)

my_region = url_text['documents'][0]['region_2depth_name']
print(my_region)