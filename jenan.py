# 재난문자 API 받아오기

import requests
import xmltodict
import json


# url의 numOfRows 파라미터 조절시 한번에 보여지는 양 설정, 많을 시 로딩시간 오래걸림
def jenan_all():
    print("재난문자를 로딩중입니다. (최대 1분 소요)")
    url = 'http://apis.data.go.kr/1741000/DisasterMsg3/getDisasterMsg1List?serviceKey=tL8DvlXmKWq0V7ralHks5bdaNOVJ4Y1yMkYncaEWfjTO%2F3bobA%2FuSCSDuVBxesTC%2F3lbC8JcFJZJJe9j9GoPgQ%3D%3D&pageNo=1&numOfRows=300&type=xml'

    res = requests.get(url)
    if res.status_code == 200:
        # Ordered dictionary type
        result = xmltodict.parse(res.text)
        dd = json.loads(json.dumps(result))

        i = 0
        for num in dd['DisasterMsg']['row']:
            if dd['DisasterMsg']['row'][i]['msg'].find("검사") != -1:
                print('발령시간 : %s' % dd['DisasterMsg']['row'][i]['create_date'])
                print('지역 : %s' % dd['DisasterMsg']['row'][i]['location_name'])
                print('내용 : %s' % dd['DisasterMsg']['row'][i]['msg'])
                print()

            i += 1
    else:
        print('res.status_code is NOT ok')


def jenan_area(area):
    print("재난문자를 로딩중입니다. (최대 1분 소요)")
    url = 'http://apis.data.go.kr/1741000/DisasterMsg3/getDisasterMsg1List?serviceKey=tL8DvlXmKWq0V7ralHks5bdaNOVJ4Y1yMkYncaEWfjTO%2F3bobA%2FuSCSDuVBxesTC%2F3lbC8JcFJZJJe9j9GoPgQ%3D%3D&pageNo=1&numOfRows=1000&type=xml'

    res = requests.get(url)
    if res.status_code == 200:
        # Ordered dictionary type
        result = xmltodict.parse(res.text)
        dd = json.loads(json.dumps(result))
        i = 0 # 전체 재난문자 카운트
        k = 0 # 코로나 관련 재난문자 카운트
        for num in dd['DisasterMsg']['row']:
            if dd['DisasterMsg']['row'][i]['msg'].find("검사") != -1:
                if dd['DisasterMsg']['row'][i]['location_name'].find(area[0:2]) != -1:
                    if k == 0:
                        print(area, "지역의 최신 코로나 관련 재난문자입니다.")
                    print('발령시간 : %s' % dd['DisasterMsg']['row'][i]['create_date'])
                    print('지역 : %s' % dd['DisasterMsg']['row'][i]['location_name'])
                    print('내용 : %s' % dd['DisasterMsg']['row'][i]['msg'])
                    print()
                    k += 1
            i += 1
        if k == 0:
            print(area,"지역에 대한 최근 코로나 관련 재난문자가 없습니다.\n")

    else:
        print('res.status_code is NOT ok')


if __name__ == "__main__":
    print("로딩중... ")
    # jenan_all()
    # jenan_area("대구")