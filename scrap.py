import urllib.parse
from csv import writer

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

url = "https://www.hcpcsdata.com/Codes"
reqs = requests.get(url)
page1 = BeautifulSoup(reqs.content, "html.parser")


# tr = soup.find_all('a')
# print(tr)
#
# urls = []
# for link in tr:
#     print(link)
#     print(link.get('href'))
table_data = page1.find_all('td')
table_row = page1.findAll('tr',class_="clickable-row")
with open ('equipo.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header = ['Group','Category','Code','Long Description','Short Description']
    thewriter.writerow(header)
    for row in table_row:
        td = row.find_all('td')
        group= row.find('a').text
        if td[2]:
            category = td[2].text.strip()
        for td in table_data:
            if td.find('a'):
                link = td.find('a').get('href')
                url2 = urllib.parse.urljoin(url, link)
                reqs2 = requests.get(url2)
                page2 = BeautifulSoup(reqs2.content, "html.parser")
                table_row2 = page2.findAll('tr', class_="clickable-row")
                table_data2 = page2.find_all('td')
            for t_data in table_row2:
                code = t_data.find('a').text
                table = t_data.find_all('td')
                description = table[1].text.strip()
                info = [group,category,code,description]
                link2 = t_data.find('a').get('href')
                url3 = urllib.parse.urljoin(url, link2)
                reqs3 = requests.get(url3)
                page3 = BeautifulSoup(reqs3.content, "html.parser")
                table_row3 = page3.find('tr')
                relate_td = table_row3.find('td')
                short_des = relate_td.findNext('td').text.strip()
                info = [group,category,code,description,short_des]
                thewriter.writerow(info)














    #
#     for td in table_data:
#         if td.find('a'):
#             a = td.find('a').get('href')
#             url2 = urllib.parse.urljoin(url, a)
#             reqs2 = requests.get(url2)
#             page2 = BeautifulSoup(reqs2.content, "html.parser")
#             table_row2 = page2.findAll('tr', class_="clickable-row")
#         for t_data in table_row2:
#             code = t_data.find('a').text
#             table = t_data.find_all('td')
#
#             if table[1]:
#                 description = table[1].text.strip()
# info2 = [group,category,code,description]
            # thewriter.writerow(info2)

