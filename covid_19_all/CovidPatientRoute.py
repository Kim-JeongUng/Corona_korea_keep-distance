# 21-11-08 - 김정웅 return 형식으로 수정
import requests
from bs4 import BeautifulSoup


# 거리두기 단계 웹 크롤링

def GetPatientRoute():
    returnroute = []
    try:
        url = requests.get(
            'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun=')
        soup = BeautifulSoup(url.content, "html.parser")
        route = soup.select("#content > div > div.box_line2 > div > div > table > tbody > tr >td")
    
        for i in range(0, len(route), 1):
            route[i] = route[i].text.replace("소독완료", "").replace("\n", " ")[1:-2]

        for i in range(0, len(route), 1):
            returnroute.append("""
                                  <header>
                                      <div>
                                           <h3>{:} : {:}</h3>
                                      </div>
                                  </header>
                                  """.format(str(i + 1), route[i]))
        # print("해당 시간대에 아래 시설을 방문하신 분은 증상이 없어도 진단검사를 꼭 받아주세요.")

    except:
        returnroute.append("GetPatientRoute err")

    return returnroute


print(GetPatientRoute())
