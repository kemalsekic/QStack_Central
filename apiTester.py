import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from datetime import datetime
from datetime import date

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("apiCreds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("lucidapitester").get_worksheet(0)
data = sheet.get_all_records()
authSheet = client.open("lucidapitester").get_worksheet(1)
authData = authSheet.get_all_records()

def getDateTime(timeStamp, todaysDate):
	todaysDate = date.today()
	now = datetime.now()
	timeStamp = now.strftime("%H:%M:%S")

def testGet():
	payload = {'page': 2, 'count': 25}
	r = requests.get('https://httpbin.org/get', params = payload)

	timeStamp = ''
	todaysDate = ''
	getDateTime(timeStamp, todaysDate)

	rows = sheet.col_values(1)
	newRowCount = len(rows)

	insertRow = [1, "get", r.status_code, r.status_code, r.url, timeStamp, todaysDate]
	sheet.insert_row(insertRow, 2)
	sheet.update_cell(3,1, newRowCount)

def testPOST():
	payload = {'username': 'corey', 'password': 'testpass'}
	r = requests.post('https://httpbin.org/post', data = payload)

	print('Status code:', r.status_code)
	print(r.json())
	r_dict = r.json()

	print('')
	print('Form entry --- ', r_dict['form'])

def testAUTH():
	r = requests.get('http://httpbin.org/basic-auth/corey/testing', auth = ('corey', 'testing'))
	print(r)

def testTimeout():
	r = requests.get('http://httpbin.org/delay/6', timeout = 3)
	print(r)

def testSheets():
	pprint(data)

def failedAPICall():
	payload = {'username': 'coreys', 'passwords': 'testpass'}
	r = requests.post('https://httpbin.org/post', data = payload)
	r = requests.get('http://httpbin.org/basic-auth/corey/testings', auth = ('corey', 'testing'))

	timeStamp = ''
	todaysDate = ''
	getDateTime(timeStamp, todaysDate)

	rows = authSheet.col_values(1)
	newRowCount = len(rows)

	insertRow = [1, "get", r.status_code, r.status_code, r.url, timeStamp, todaysDate]
	authSheet.insert_row(insertRow, 2)
	authSheet.update_cell(3,1, newRowCount)

testGet()
failedAPICall()
#testPOST()
#testAUTH()
#testTimeout()
#testSheets()
#getDateTime()