import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("apiCreds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("lucidapitester").sheet1

data = sheet.get_all_records()

row = sheet.row_values(2)
col = sheet.col_values(1)
cell = sheet.cell(1,2).value

insertRow = ["hello", 5, "red", "blue"]
sheet.insert_row(insertRow, 4)

#sheet.update_cell(2,2, "CHANGED")
#sheet.delete_row(3)
pprint(cell)

