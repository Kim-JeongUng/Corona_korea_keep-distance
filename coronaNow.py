# 코로나 현재 증가 추이 확인

import requests
import xmltodict
import json
import datetime


# 데이터셋 : 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=tL8DvlXmKWq0V7ralHks5bdaNOVJ4Y1yMkYncaEWfjTO%2F3bobA%2FuSCSDuVBxesTC%2F3lbC8JcFJZJJe9j9GoPgQ%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20210809&endCreateDt=20210810'
# data.go.kr

def getCovidKR(end_day, start_day):
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=tL8DvlXmKWq0V7ralHks5bdaNOVJ4Y1yMkYncaEWfjTO%2F3bobA%2FuSCSDuVBxesTC%2F3lbC8JcFJZJJe9j9GoPgQ%3D%3D&pageNo=1&numOfRows=10'
    # ServiceKey는 url decode 한 값임.
    payload = {'startCreateDt': start_day, 'endCreateDt': end_day, }

    res = requests.get(url, params=payload)
    if res.status_code == 200:
        # Ordered dictionary type
        result = xmltodict.parse(res.text)
        dd = json.loads(json.dumps(result))

        print('%s 기준' % (dd['response']['body']['items']['item'][0]["stdDay"]))

        i = len(dd['response']['body']['items']['item'])
        for area in dd['response']['body']['items']['item']:
            i -= 1
            print('%s 지역' % dd['response']['body']['items']['item'][i]['gubun'])
            print('누적 확진자:', dd['response']['body']['items']['item'][i]['defCnt'])
            print('추가 확진자:', int(dd['response']['body']['items']['item'][i]['incDec']))
            print()
    else:
        print('res.status_code is NOT ok')


def CovidAll():
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=tL8DvlXmKWq0V7ralHks5bdaNOVJ4Y1yMkYncaEWfjTO%2F3bobA%2FuSCSDuVBxesTC%2F3lbC8JcFJZJJe9j9GoPgQ%3D%3D&pageNo=1&numOfRows=10'
    res = requests.get(url)
    result = xmltodict.parse(res.text)
    dd = json.loads(json.dumps(result))

    print("%s기준 신규 확진자 및 누적 확진자" % (dd['response']['body']['items']['item'][0]["stdDay"]))

    i = len(dd['response']['body']['items']['item'])
    for a in dd['response']['body']['items']['item']:
        i -= 1
        if dd['response']['body']['items']['item'][i]['gubun'].find("합계") != -1:
            print('신규 확진자:', int(dd['response']['body']['items']['item'][i]['incDec']))
            print('누적 확진자:', dd['response']['body']['items']['item'][i]['defCnt'])
            print()


def CovidArea(area):
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=tL8DvlXmKWq0V7ralHks5bdaNOVJ4Y1yMkYncaEWfjTO%2F3bobA%2FuSCSDuVBxesTC%2F3lbC8JcFJZJJe9j9GoPgQ%3D%3D&pageNo=1&numOfRows=10'
    res = requests.get(url)

    if res.status_code == 200:
        # Ordered dictionary type
        result = xmltodict.parse(res.text)
        dd = json.loads(json.dumps(result))

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

    # 전 날과 비교는 필요없을듯
    # d2 = yesterday.strftime("%Y%m%d")

    d2 = today.strftime("%Y%m%d")
