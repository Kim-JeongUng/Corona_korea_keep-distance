import pandas as pd
import Main
# 행정구역 엑셀읽어오기
df = pd.read_excel('행정구역.xlsx')

do = df['시도명'].loc[df['시군구명'].str.contains(Main.my_area) == True]
dov = ""

for val in do:
    dov = val