# 정부 뉴스

import requests
from bs4 import BeautifulSoup

def Gnews():
    news_num = 5#뉴스 개수 default 10
    news_url = 'http://www.whosaeng.com/search.html?submit=submit&search=%EB%B0%A9%EC%97%AD%EB%8B%B9%EA%B5%AD&imageField3.x=0&imageField3.y=0&search_and=2&search_exec=all&search_section=sc1&news_order=1&search_start_day=&search_end_day=20211108'

    req = requests.get(news_url)
    soup = BeautifulSoup(req.text, 'html.parser')

    # 제목
    title= soup.select("#search_result > div.search_result_list > div > dl > dt")
    # 내용
    msg =  soup.select("#search_result > div.search_result_list > div> dl > dd.sbody > a")
    # 기사 링크
    url = []
    for m in msg:
        url.append("http://www.whosaeng.com"+m.get("href"))

    newslist = []
    for x in range(0, news_num):
        newslist.append("""
            <article class="post">
            <header>
                <div class="meta" OnClick="location.href ={:}" style="cursor:pointer;">
                     <h2>{:}</h2>
                     <h3>{:}</h3>
                </div>
            </header>
            </article>
            """.format(url[x],title[x].text.replace('\xa0',''), msg[x].text.replace('\xa0','')))

    return newslist
