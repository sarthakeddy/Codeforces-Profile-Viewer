import requests
import json
import xlsxwriter 

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

link="https://codeforces.com/api/user.rating?handle="+cf_id
js_object=requests.get(link)
py_dict=json.loads(js_object.text)

#loading new workbook
wb = xlsxwriter.Workbook(cf_id+'.xlsx')
sheet = wb.add_worksheet()

#result from api
p=py_dict['result']

#initialising heading
sheet.write('A1',"S No.")
sheet.write('B1',"Contest ID")
sheet.write('C1',"Contest Name")
sheet.write('D1',"Rank")
sheet.write('E1',"Old Rating")
sheet.write('F1',"New Rating")
sheet.write('G1',"Change in Rating")

#traverse to display recent submissions
i=0 
for temp in p:
	sheet.write('A'+str(i+3),i+1)
	sheet.write('B'+str(i+3),p[i]['contestId'])
	sheet.write('C'+str(i+3),p[i]['contestName'])
	sheet.write('D'+str(i+3),p[i]['rank'])
	sheet.write('E'+str(i+3),p[i]['oldRating'])
	sheet.write('F'+str(i+3),p[i]['newRating'])
	sheet.write('G'+str(i+3),p[i]['newRating']-p[i]['oldRating'])
	i+=1;
wb.close()