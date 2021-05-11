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