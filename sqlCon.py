import mysql.connector

db = mysql.connector.connect(
	host = "database3.cydji51bekub.us-east-2.rds.amazonaws.com",
	user = "admin",
	passwd = "todorovo",
	auth_plugin='mysql_native_password',
	database = "database33"
	)

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE testdb")

#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("CREATE TABLE Testertest (firstName VARCHAR(25), lastName VARCHAR(25), pID VARCHAR(25), pw VARCHAR(25), personID int PRIMARY KEY AUTO_INCREMENT)")
	
#mycursor.execute("DESCRIBE Person")

#mycursor.execute("INSERT INTO Person(name, age) VALUES(%s, %s)", ("Kemal", 26))
def register_user_to_db(firstName, lastName, pID, pw):
	#mycursor.execute("CREATE TABLE Testertest (firstName VARCHAR(25), lastName VARCHAR(25), pID int, pw VARCHAR(25), personID int PRIMARY KEY AUTO_INCREMENT)")
	#mycursor.execute("CREATE TABLE NameChecker (pID int, personID int PRIMARY KEY AUTO_INCREMENT)")
	
	mycursor.execute("INSERT INTO Testertest(firstName, lastName, pID, pw) VALUES(%s, %s, %s, %s)", (firstName, lastName, pID, pw))
	db.commit()

def findUser(userCheck):
	mycursor.execute("SELECT firstName FROM Testertest WHERE firstName userCheck")

#register_user_to_db("Kemal", "Sekic", "personsID", "Password!")

def nameCheckers(pID):
	#mycursor.execute("CREATE TABLE Testertest (firstName VARCHAR(25), lastName VARCHAR(25), pID int, pw VARCHAR(25), personID int PRIMARY KEY AUTO_INCREMENT)")
	#mycursor.execute("CREATE TABLE NameChecked (pID VARCHAR(15), personID int PRIMARY KEY AUTO_INCREMENT)")
	mycursor.execute("INSERT INTO NameChecked(pID) VALUES(%s)", (pID,))
	db.commit()

def updateNameCheckers(pid):
	mycursor.execute("UPDATE NameChecked SET pID = %s WHERE pID = %s", (pid))
#mycursor.execute("DESCRIBE NameChecked")
#nameCheckers("5")
#findUser("Kemal")
#mycursor.execute("SELECT * FROM NameChecked WHERE pID=5")

#for x in mycursor:
#	print(x)

#db.close()