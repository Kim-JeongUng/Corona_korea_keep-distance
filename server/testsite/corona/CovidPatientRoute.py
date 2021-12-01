# 확진자 동선 출력 (저장은 ScheduleServer에서 담당)

import openpyxl


def GetPatientRoute():
    wb = openpyxl.load_workbook("PatientRoute.xlsx")
    result =""
    cnt = 0
    result+=("<p>정부 공개 확진자 이동 동선 파악 꼭 검사받으세요.<p></br>")

    for i in wb.active.rows:
        if cnt > 0:
            result += ("<article class='mini-post'><header>")
            result += ("<h3>{}<h3>".format(i[0].value))
            result += ("<h3>{}<h3>".format(i[1].value))
            result += ("<h3>{}<h3>".format(i[2].value))
            result += ("<h3>{}<h3>".format(i[3].value))

            result += ("</header></article>")
        cnt += 1
    if cnt == 0:
        print("최근 공개된 확진자 동선이 없습니다. \n")

    return result


print(GetPatientRoute())