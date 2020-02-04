import bs4
import requests
from bs4 import BeautifulSoup as soup
import json

c=0
while True:
	if c==0:
		cf_id=input("Enter your codeforces id\n")
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

link="https://codeforces.com/api/user.info?handles="+cf_id
ml=requests.get(link)
p=json.loads(ml.text)
dic=p['result']

for p in dic:
	print(dic[p])

#user-id
print("User-ID : ",cf_id)

#User Name
print("Name : ",dic[9]," ",dic[0])