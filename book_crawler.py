import matplotlib.pyplot as plt
import matplotlib
from urllib.request import urlopen
from bs4 import BeautifulSoup


html=urlopen("http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=06")
soup=BeautifulSoup(html, "lxml")
#print(soup)
book_table=soup.find_all('table', {'id': 'category_layout'},{'class':'list'})
#print(book_table)

book_title_list=[]
kind_list=[]
price_list=[]
for data in book_table:
    #제목 수집
    data2=data.find_all('tr')
    for Acontent in data2:
        Acontent = Acontent.find_all('td', {'class': 'goodsTxtInfo'})
        for Acontent2 in Acontent:
            Acontent2=Acontent2.find_all('a',limit=1)
            for Acontent3 in Acontent2:
                book_title_list.append(Acontent3.get_text())
    #장르 수집
    for Bcontent in data2:
        Bcontent = Bcontent.find_all('td', {'class': 'goodsTxtInfo'})
        for Bcontent2 in Bcontent:
            Bcontent2=Bcontent2.find_all('p',limit=1)
            for Bcontent3 in Bcontent2:
                Bcontent3=Bcontent3.get_text().split()
                kind_list.append(Bcontent3[0])
    #가격 수집
    for Ccontent in data2:
        Ccontent = Ccontent.find_all('td', {'class': 'goodsTxtInfo'})
        for Ccontent2 in Ccontent:
            Ccontent2=Ccontent2.find_all('p')

            for Ccontent3 in Ccontent2:
                Ccontent3 = Ccontent3.find_all('span',limit=1)
                for Ccontent4 in Ccontent3:
                    price_list.append(Ccontent4.get_text())

book_ranking=dict()
for i in range (len(book_title_list)):
    book_ranking[str(i+1)+'위']=book_title_list[i]+':'+kind_list[i]+'/'+price_list[i]
#print(book_ranking)

print('--yes24 국내도서 종합 베스트셀러--')
for rank,info in book_ranking.items():
    print(rank,'-',info)

#print(kind_list)
#print(book_title_list)
#print(price_list)


import matplotlib.font_manager as fm
font_fname = 'C:/Windows/Fonts/NanumGothic.ttf'
font_family = fm.FontProperties(fname=font_fname).get_name()
plt.rcParams["font.family"] = font_family
plt.rcParams['font.size'] = 15.
plt.rcParams['xtick.labelsize'] = 6.
plt.rcParams['ytick.labelsize'] = 6.
plt.rcParams['axes.labelsize'] = 10.

money=[]

for i in soup.find(id='category_layout').find_all('td', {'class': 'goodsTxtInfo'}):
    for price in i.find_all('span', {'class': 'priceB'}):
        money.append(price.get_text())

money=list(money)

r_money=[]

for i in money:
    i=list(i)
    if "," in i:
        i.remove(",")
    if "원" in i:
        i.remove("원")
    i=str(i)
    if len(i)==25:
        i=i[2]+i[7]+i[12]+i[17]+i[22]
    else:
        i = i[2] + i[7] + i[12] + i[17]
    i=int(i)

    r_money.append(i)

r_money=list(r_money)
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
title=book_title_list

plt.bar(x,r_money)


plt.bar(x,r_money)
plt.suptitle('yes24 국내도서 종합 베스트셀러 20위까지의 가격')
plt.xticks(x,title,rotation='vertical')
plt.show()