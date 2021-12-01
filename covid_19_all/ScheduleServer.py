# 서버에서 실행됨
import schedule
import time

import CovidCountSmallArea
import JenanMessage
import Schedule_CovidPatientRoute

CovidCountSmallArea.CovidCountSave()
# 매일 오전 10시마다 코로나증감수치 엑셀저장 실행
schedule.every().day.at("10:00").do(CovidCountSmallArea.CovidCountSave)
#schedule.every(3).hours.do(CovidCountSmallArea.CovidCountSave)

# 매 5분마다 재난메세지 저장
schedule.every(5).minutes.do(JenanMessage.jenan_all)

# 매 1시간 마다 확진자 위치 엑셀 저장 실행
schedule.every(1).hours.do(Schedule_CovidPatientRoute.SavePatientRoute)

while True:
    schedule.run_pending()
    time.sleep(1)
