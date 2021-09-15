# 소분류 지역별 코로나 확진자
# 서버 내 동작기능

# 김정웅 210915

import requests
from bs4 import BeautifulSoup
import json

# 매일 GPS 기록 저장
import pandas as pd
import datetime

import re

# 좌표 찾기 api
url = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=')
CovidCountURL = BeautifulSoup(url.content, "html.parser")




# GPS 기록저장

df = pd.read_excel('CovidCount.xlsx', index_col =[0])

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(1)
today = today.strftime("%Y%m%d")
yesterday = yesterday.strftime("%Y%m%d")
print(yesterday)

# 만약 마지막에 저장한 값과 날짜가 변경될경우 엑셀 저장
# 어제 데이터와 비교해야함, 시트 두개 필요
if not (df.iloc[-1]['date'] != today):
    # 이부분에 이전 Today자료를 YesterDay시트로 옮겨줘야함
    print("날짜가 바뀌어 데이터를 저장합니다.")
    for i in range(0,18,1):
        regionData = CovidCountURL.select("#zone_popup"+str(i)+" > div > table > tbody > tr")

        for rgn in regionData:
            #콤마 제거
            rgn= rgn.text.replace(',','')
            data ={
                'date': [today],
                'region': [rgn],
            }

            new_df = pd.DataFrame(data)

            df = pd.concat([df,new_df])
            # 엑셀 저장
            df.to_excel('CovidCount.xlsx')
