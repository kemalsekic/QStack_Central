import csv

stagingFile = open('stagingFile.csv')
fileReader = csv.reader(stagingFile)
stagingData = list(fileReader)

uName = stagingData[1][0]
pWord = stagingData[1][1]
accNum = stagingData[1][2]
ssn = stagingData[1][3]
firstName = stagingData[1][4]
lastName = stagingData[1][5]
dobMonth = stagingData[1][6]
dobDay = stagingData[1][7]
dobYear = stagingData[1][8]
address = stagingData[1][9]
address2 = stagingData[1][10]
city = stagingData[1][11]
state = stagingData[1][12]
zipCode = stagingData[1][13]
mdn = stagingData[1][14]
orderNum = stagingData[1][15]
invoiceNum = stagingData[1][16]