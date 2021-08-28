# 재난문자 API 받아오기

import requests
import xmltodict
import json

# url의 numOfRows 파라미터 조절시 한번에 보여지는 양 설정, 많을 시 로딩시간 오래걸림
print("재난문자를 로딩중입니다. (최대 1분 소요)")
url = 'http://apis.data.go.kr/1741000/DisasterMsg3/getDisasterMsg1List?serviceKey=tL8DvlXmKWq0V7ralHks5bdaNOVJ4Y1yMkYncaEWfjTO%2F3bobA%2FuSCSDuVBxesTC%2F3lbC8JcFJZJJe9j9GoPgQ%3D%3D&pageNo=1&numOfRows=1000&type=xml'

res = requests.get(url)
if res.status_code == 200:
    # Ordered dictionary type
    result = xmltodict.parse(res.text)
    dd = json.loads(json.dumps(result))
else:
    print('res.status_code is NOT ok')

# 코로나 관련 재난문자 전체 출력
def jenan_all():
    i = 0
    for num in dd['DisasterMsg']['row']:
        # 재난문자중 "검사"내용이 들어가면 코로나라고 판별 (그나마,, 코로나로 검색하는것보다 더 나은듯 ex) ~방문자는 보건소에서 검사받으세요)
        if dd['DisasterMsg']['row'][i]['msg'].find("검사") != -1:
            print('발령시간 : %s' % dd['DisasterMsg']['row'][i]['create_date'])
            print('지역 : %s' % dd['DisasterMsg']['row'][i]['location_name'])
            print('내용 : %s' % dd['DisasterMsg']['row'][i]['msg'])
            print()
        i += 1


def jenan_area(area):
    i = 0 # 전체 재난문자 카운트
    k = 0 # 코로나 관련 재난문자 카운트
    for num in dd['DisasterMsg']['row']:
        if dd['DisasterMsg']['row'][i]['msg'].find("검사") != -1:
            # area[0:2]까지만 받는 이유 : 춘천시 등 시가 들어갔을 때 보다 춘천으로의 검색결과가 더 유효함, 수원시 장안구 등 구까지 검색에서도 큰 범위를 찾을 수 있음
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
        print(area,"지역에 대한 최근 코로나 관련 재난문자가 없습니다. \n") #, Main.dov,"로 재검색합니다
        #jenan_area(Main.dov)


if __name__ == "__main__":
    print("로딩중... ")
    # jenan_all()
    # jenan_area("대구")