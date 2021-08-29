# 코로나 신규 확진자 확인

import requests
import xmltodict
import json
import datetime

# 데이터셋 : 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=tL8DvlXmKWq0V7ralHks5bdaNOVJ4Y1yMkYncaEWfjTO%2F3bobA%2FuSCSDuVBxesTC%2F3lbC8JcFJZJJe9j9GoPgQ%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20210809&endCreateDt=20210810'
# data.go.kr
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(1)
d1 = today.strftime("%Y%m%d")
d2 = yesterday.strftime("%Y%m%d")

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=tL8DvlXmKWq0V7ralHks5bdaNOVJ4Y1yMkYncaEWfjTO%2F3bobA%2FuSCSDuVBxesTC%2F3lbC8JcFJZJJe9j9GoPgQ%3D%3D&pageNo=1&numOfRows=10&'
payload = {'startCreateDt': d2, 'endCreateDt': d1, }
res = requests.get(url, params=payload)
if res.status_code == 200:
    result = xmltodict.parse(res.text)
    dd = json.loads(json.dumps(result))


# 전체 지역 누적확진자 및 추가확진자
def getCovidKR(end_day, start_day):
    print('%s 기준' % (dd['response']['body']['items']['item'][0]["stdDay"]))

    i = len(dd['response']['body']['items']['item'])
    for area in dd['response']['body']['items']['item']:
        i -= 1
        print('%s 지역' % dd['response']['body']['items']['item'][i]['gubun'])
        print('누적 확진자:', dd['response']['body']['items']['item'][i]['defCnt'])
        print('추가 확진자:', int(dd['response']['body']['items']['item'][i]['incDec']))
        print()


# 전국 코로나 신규 확진자
def CovidAll():
    print("%s기준 신규 확진자 및 누적 확진자" % (dd['response']['body']['items']['item'][0]["stdDay"]))

    i = len(dd['response']['body']['items']['item'])
    for a in dd['response']['body']['items']['item']:
        i -= 1
        if dd['response']['body']['items']['item'][i]['gubun'].find("합계") != -1:
            print('신규 확진자:', int(dd['response']['body']['items']['item'][i]['incDec']))
            print('누적 확진자:', dd['response']['body']['items']['item'][i]['defCnt'])
            print()


# 특정 지역 신규 확진자
def CovidArea(area):
    print("%s지역 %s기준 신규 확진자 및 누적 확진자" % (area, (dd['response']['body']['items']['item'][0]["stdDay"])))

    i = len(dd['response']['body']['items']['item'])
    for a in dd['response']['body']['items']['item']:
        i -= 1
        if dd['response']['body']['items']['item'][i]['gubun'].find(area) != -1:
            print('신규 확진자:', int(dd['response']['body']['items']['item'][i]['incDec']))
            print('누적 확진자:', dd['response']['body']['items']['item'][i]['defCnt'])
            print()


if __name__ == "__main__":
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(1)
    d1 = today.strftime("%Y%m%d")
    d2 = yesterday.strftime("%Y%m%d")

