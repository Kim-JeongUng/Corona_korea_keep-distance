import requests
import xmltodict
import json


# url의 numOfRows 파라미터 조절시 한번에 보여지는 양 설정, 많을 시 로딩시간 오래걸림

def jenan():
    url = 'http://apis.data.go.kr/1741000/DisasterMsg3/getDisasterMsg1List?serviceKey=tL8DvlXmKWq0V7ralHks5bdaNOVJ4Y1yMkYncaEWfjTO%2F3bobA%2FuSCSDuVBxesTC%2F3lbC8JcFJZJJe9j9GoPgQ%3D%3D&pageNo=1&numOfRows=30&type=xml'

    res = requests.get(url)
    if res.status_code == 200:
        # Ordered dictionary type
        result = xmltodict.parse(res.text)
        dd = json.loads(json.dumps(result))


        #i=len(dd['DisasterMsg']['row'])
        i=0
        for num in dd['DisasterMsg']['row']:
            if(dd['DisasterMsg']['row'][i]['msg'].find("검사")!= -1):
                print('발령시간 : %s' % dd['DisasterMsg']['row'][i]['create_date'])
                print('지역 : %s' % dd['DisasterMsg']['row'][i]['location_name'])
                print('내용 : %s' % dd['DisasterMsg']['row'][i]['msg'])
                print()

            i+=1
    else:
        print('res.status_code is NOT ok')


if __name__ == "__main__":
    print("로딩중")
    jenan()
