import bs4
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import json

c=0
while True:
	if c==0:
		cf_id=input("Enter your codeforces id : ")
		c+=1
	else:
		cf_id=input("Enter your codeforces id again\n")
	link='https://www.codeforces.com/profile/'+cf_id
	check=requests.get(link)
	display="INVALID Codeforces ID"
	if check.url == "https://codeforces.com/":
		print(display.center(40,'*'))
	else:
		break

uClient=uReq(link)
link="https://codeforces.com/api/user.info?handles="+cf_id
ml=requests.get(link)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
c=page_soup.find_all('li')
p=json.loads(ml.text)
dic=p['result']
ls=dic[0]

#user-id
print("User-ID:",cf_id)

#User Name
print("Name:",ls['firstName'],ls['lastName'])

#country
print("Country:",ls['country'])

#organisation
print("Institute:",ls['organization'])

#city
print("City:",ls['city'])

#current rating
print("Current Rating:",ls['rating'])

#current group
print("Current Group:",ls['rank'])

#contrib
print("Contribution:",ls['contribution'])

#Friends
print("Friends Count:",ls['friendOfCount'])

#max rating
print("Max Rating:",ls['maxRating'])

#max rank
print("Max Group:",ls['maxRank'])

#registered
print("Registered:",c[44].span.text.strip())