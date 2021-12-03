# 정부 뉴스

import requests
from bs4 import BeautifulSoup

def gnews():
    news_url = 'http://www.whosaeng.com/search.html?submit=submit&search=%EB%B0%A9%EC%97%AD%EB%8B%B9%EA%B5%AD&imageField3.x=0&imageField3.y=0&search_and=2&search_exec=all&search_section=sc1&news_order=1&search_start_day=&search_end_day=20211108'

    news_num = 10#뉴스 개수 default 10
    newsReq = requests.get(news_url)
    soup = BeautifulSoup(newsReq.text, 'html.parser')

    temp = soup.find_all('div', {'class': 'search_result_list_box'})

    title = []
    msg = []
    url = []
    img = []
    for i in range(0,news_num):
        title.append(temp[i].select("dl > dt")[0])
        msg.append(temp[i].select("dl > dd.sbody > a")[0])
        try:
            img.append(temp[i].select("div.img_file>a>p>img")[0].get("src"))
        except:
            img.append("https://user-images.githubusercontent.com/82865325/143685603-f168ff67-6f3d-425b-84d3-8b93d2b6a69a.png")
        url.append("http://www.whosaeng.com" + msg[i].get("href"))
    newslist = []
    for i in range(0, news_num):
        newslist.append("""
            <article class="post">
            <header>
                <div class="meta">
                <a href="#"><img src="{:}" alt="" /></a>
    									</div>
    									<div class="title">
    										<h3><a href="{:}">{:}</a></h3>
    										<h4><a href="{:}">{:}</a></h4>
    									</div>
            </header>
            </article>
                """.format(img[i], url[i], title[i].text.replace('\xa0', ''),url[i], msg[i].text.replace('\xa0', '')))

    return newslist


# 과거버전 현재 사용 X gnews()를 사용하세요
def pastGnews():
    news_num = 10#뉴스 개수 default 10
    news_url = 'http://www.whosaeng.com/search.html?submit=submit&search=%EB%B0%A9%EC%97%AD%EB%8B%B9%EA%B5%AD&imageField3.x=0&imageField3.y=0&search_and=2&search_exec=all&search_section=sc1&news_order=1&search_start_day=&search_end_day=20211108'
    req = requests.get(news_url)
    soup = BeautifulSoup(req.text, 'html.parser')

    # 제목
    title= soup.select("#search_result > div.search_result_list > div > dl > dt")
    # 내용               #search_result > div.search_result_list > div > dl > dt > a
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
            <div class="meta">
            <a href="#"><img src="https://user-images.githubusercontent.com/82865325/143685603-f168ff67-6f3d-425b-84d3-8b93d2b6a69a.png" alt="" /></a>
									</div>
									<div class="title">
										<h3><a href="{:}">{:}</a></h3>
									</div>
        </header>
        </article>
            """.format(url[x],title[x].text.replace('\xa0','')))

    return newslist





print(gnews())