import requests
from pandas import DataFrame
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os


#date = str(datetime.now())
#date = date[:date.rfind(':')].replace(' ', '_')
#date = date.replace(':', '시') + '분'

query = input('지역을 입력하세요 : ')
query = query + ' + 코로나 | 확진 | 백신'
news_num = int(input('총 필요한 뉴스기사 수를 입력해주세요(숫자만 입력) : '))
query = query.replace(' ', ' ')

news_url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}'

req = requests.get(news_url.format(query))
soup = BeautifulSoup(req.text, 'html.parser')

news_dict = {}
news_dict2 = {}
idx = 0
idx2 = 0
cur_page = 1

print('크롤링 중...')

while idx < news_num:
    ### 네이버 뉴스 웹페이지 구성이 바뀌어 태그명, class 속성 값 등을 수정함(20210126) ###

    table = soup.find('ul', {'class': 'list_news'})
    li_list = table.find_all('li', {'id': re.compile('sp_nws.*')})

    area_list = [li.find('div', {'class': 'news_area'}) for li in li_list]
    a_list = [area.find('a', {'class': 'news_tit'}) for area in area_list]

    area2_list = [li.find('div', {'class': 'news_wrap api_ani_send'}) for li in li_list]
    img_list = [area.select_one('div > a > img') for area in area2_list]

    for n in a_list[:min(len(a_list), news_num - idx)]:

        news_dict[idx] = {'title': n.get('title'),
                          'url': n.get('href')}
        idx += 1

    for n in img_list[:min(len(img_list), news_num - idx2)]:

        news_dict2[idx2] = {'img': n.get('src')}
        idx2 += 1

    cur_page += 1

print('크롤링 완료')
print('데이터프레임 변환')

news_df = DataFrame(news_dict).T
news_df2 = DataFrame(news_dict2).T

for x in range(0,news_num):
    print("사진 : ",news_dict2[x]['img'])
    print("제목 : ",news_dict[x]['title'])
    print("링크 : ",news_dict[x]['url'])
    print("===================================================================================")

#folder_path = os.getcwd()
#xlsx_file_name = '네이버뉴스_{}_{}.xlsx'.format(query[0:2], date)

#news_df.to_excel(xlsx_file_name)

#print('엑셀 저장 완료 | 경로 : {}\\{}'.format(folder_path, xlsx_file_name))
#os.startfile(folder_path)

### 네이버 뉴스 웹페이지 구성이 바뀌어 태그명, class 속성 값 등을 수정함(20210126) ###