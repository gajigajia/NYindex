import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.investing.com/indices/kosdaq-historical-data', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#curr_table > tbody > tr:nth-child(1) > td.first.left.bold.noWrap
#curr_table > tbody > tr:nth-child(1) > td:nth-child(2)
#curr_table > tbody > tr:nth-child(1) > td.bold.redFont


KOSPI = soup.select('curr_table > tbody > tr:nth-child(1) > td:nth-child(3)')

print(KOSPI)

#kospi2 = index.select_one('number_1')
#kospi3 = index.select_one('rate_down')
#kospi4 = index.select_one('')

#kosdaq1 = index.select_one('div.kosdaq_area.group_quot > div.heading_area > a > span > span.num')
#kosdaq2 = index.select_one('div.kosdaq_area.group_quot > div.heading_area > a > span > span.num2')
#kosdaq3 = index.select_one('div.kosdaq_area.group_quot > div.heading_area > a > span > span.num3')
#kosdaq4 = index.select_one('div.kosdaq_area.group_quot > div.heading_area > a > span > span.blind')