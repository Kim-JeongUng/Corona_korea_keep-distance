# GPS로 내 좌표 찾기
# 구글 geolocation api 사용

import os
import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)

LOCATION_API_KEY = os.getenv('AIzaSyCArXnnrT7PhvZUinEuN94BRZfx5Qibyto')

url = f'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCArXnnrT7PhvZUinEuN94BRZfx5Qibyto'
data = {
    'considerIp': True,
}

result = requests.post(url, data).json()
my_lat = 37.29088909058154#result["location"]["lat"]
my_lng = 127.00763359938911#result["location"]["lng"]
#37.29088909058154, 127.00763359938911
