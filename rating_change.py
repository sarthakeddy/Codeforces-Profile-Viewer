import requests
import json

c=0
while True:
	if c==0:
		cf_id=input("Enter your codeforces id :")
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

contest_no=(input("Enter valid contest number :"))
link="https://codeforces.com/api/contest.ratingChanges?contestId="+contest_no
js_object=requests.get(link)
py_dict=json.loads(js_object.text)

#result from api
p=py_dict['result']

#traverse to find id
found=1
i=0
for t in p:
	temp=p[i]['handle']
	if temp==cf_id:
		print("Contest Details:",p[i]['contestName'])
		print("Rank:",p[i]['rank'])
		print("Old Rating:",p[i]['oldRating'])
		print("New Rating:",p[i]['newRating'])
		print("Change in Rating:",p[i]['newRating']-p[i]['oldRating'])
		found=0
		break
	i+=1

if found == 1:
	print(cf_id,"You didn't participate in this contest")