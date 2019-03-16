import sys
import importlib
importlib.reload(sys)

import csv
import requests
from bs4 import BeautifulSoup


y = ':1:US'
outfile = open("./Weather.csv","w")


for x in range(1100,1200):
	url = 'https://weather.com/weather/today/l/USTX'
	url = url + str(x) + y
	response =  requests.get(url)
	html= response.content
	soup = BeautifulSoup((html),"lxml")
	list_of_cells=""
	divs= soup.find('h1', attrs={'classname':'h4 today_nowcard-location'})
	divs = str(divs)
	loc= divs[divs.find('classname = "h4 today_nowcard-location">')+38:divs.find('<span class ="icon-font iconset')]
	divs = soup.find('div', attrs={'class':'today_nowcard-temp'})
	divs = str(divs)
	temp = divs[divs.find('class="today_nowcard-temp">')+42:divs.find('<sup>')]
	divs= soup.find('div',attrs={'class' : 'today_nowcard-phrase'})
	divs = str(divs)
	phrase = divs[divs.find('class="today_nowcard-phrase">')+29:divs.find('</div>')]
	divs= soup.find('span', attrs={'id':'dp0-details-wind'})
	divs = str(divs)
	wind = divs[divs.find('<span id ="dp0-details-wind">')+43:divs.find('</span>')]
	list_of_cells= list_of_cells + loc + "," + temp + "," + phrase + "," + wind +"\n";
	outfile.write(list_of_cells)
	