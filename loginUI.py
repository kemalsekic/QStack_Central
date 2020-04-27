from tkinter import *
from tkinter import ttk
import apiTester
import wordThings
import runTests
import D2C_UI
import d2cDriver
import retailUIController
from configparser import ConfigParser
import os
import sqlCon

dbCursor = sqlCon.mycursor

global uiSettings 
uiSettings = ConfigParser()
global docName
docName = wordThings.docName

def createTab():
    global rows
    rows = 0
    while rows < 50:
        screen.rowconfigure(rows, weight=1)
        screen.columnconfigure(rows, weight=1)
        rows += 1

    nb = ttk.Notebook(screen)
    nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

    global page1
    page1 = ttk.Frame(nb)
    nb.add(page1, text='Home')
    global page2
    page2 = ttk.Frame(nb)
    nb.add(page2, text='Test Controls')
    global page3
    page3 = ttk.Frame(nb)
    nb.add(page3, text='Account Settings')

def setScreen(screenToSet, title, geoX):
    screenToSet.title(title)
    screenToSet.geometry(geoX)

def login_success(screenClose):
    #screen.hide()
    screenClose.destroy()
    #session()

def register_user(event=None):
    username_info = username.get()
    password_info = password.get()

    sqlCon.register_user_to_db("Kemal", "Sekic", username_info, password_info)
    Label(registerScreen, text="Registration Successfull!", fg="green", font=("calibri", 11)).pack()

def register():
    global registerScreen
    registerScreen = Toplevel(screen)
    setScreen(registerScreen, "Register", "300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(registerScreen, text = "Please enter details below").pack()
    Label(registerScreen, text = "").pack()

    Label(registerScreen, text = "Username * ").pack()
    username_entry = Entry(registerScreen, textvariable = username)
    username_entry.focus()
    username_entry.pack()

    Label(registerScreen, text = "Password * ").pack()
    password_entry = Entry(registerScreen, textvariable = password)
    password_entry.pack()
    registerScreen.bind('<Return>', register_user)

    Button(registerScreen, text = "Register", width=10, height=1, command = register_user).pack()

def login_verify(event=None):
    username1 = username_verify.get()
    password1 = password_verify.get()
    checkUser = ""
    checkPass = ""

    screen.deiconify()
    login_success(loginScreen)
    """
    dbCursor.execute("SELECT pID and pw FROM Testertest WHERE pID='" + username1 + "' and pw='" + password1 + "'")
    data = dbCursor.fetchone()

    if data is None:
        Label(loginScreen, text="Username or Password is incorrect.").pack()
        Label(loginScreen, text="Please try again.").pack()
    if username1 == checkUser and password1 == checkPass:
        screen.deiconify()
        login_success(loginScreen)
    else:
        Label(loginScreen, text="Username or Password is incorrect.").pack()
        Label(loginScreen, text="Please try again.").pack()

    

    if username1 == "":
        Label(loginScreen, text="Username is missing.", width=20, height=1).pack()
    elif password1 == "":
        Label(loginScreen, text="Password is missing.", width=20, height=1).pack()
    elif username1:
        #dbCursor.execute("SELECT pID FROM Testertest WHERE pID='" + username1 + "'")
        dbCursor.execute("SELECT pID FROM Testertest WHERE pID=%s", (username1,))
        #record = dbCursor.fetchone()
        for x in dbCursor:
                print(x)
        if password1:
            #dbCursor.execute("SELECT pw FROM Testertest WHERE pw='" + password1 + "'")
            dbCursor.execute("SELECT pw FROM Testertest WHERE pw=%s", (password1,))
            #record = dbCursor.fetchone()
            
            for x in dbCursor:
                print(x)
            #dbCursor.execute("SELECT * FROM Testertest WHERE pID=%s AND pw=%s", (username1, password1,))

        if username1 == checkUser and password1 == checkPass:
            screen.deiconify()
            login_success(loginScreen)
        else:
            Label(loginScreen, text="Username or Password is incorrect.").pack()
            Label(loginScreen, text="Please try again.").pack()
"""
"""

    list_of_files = os.listdir()
    
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        file1.close()
        if password1 in verify:
            print("Login Success!")
            screen.deiconify()
            login_success(loginScreen)
        else:
            print("Password not recognized")
            password_not_recognized()
    else:
        print("User not found")
        user_not_found()
"""

def login_verify_button():
    username1 = username_verify.get()
    password1 = password_verify.get()
    checkUser = ""
    checkPass = ""
    """dbCursor.execute("SELECT pID and pw FROM Testertest WHERE pID='" + username1 + "' and pw='" + password1 + "'")
    data = dbCursor.fetchone()

    if data is None:
        Label(loginScreen, text="Username or Password is incorrect.").pack()
        Label(loginScreen, text="Please try again.").pack()
    if username1 == checkUser and password1 == checkPass:
        screen.deiconify()
        login_success(loginScreen)
    else:
        Label(loginScreen, text="Username or Password is incorrect.").pack()
        Label(loginScreen, text="Please try again.").pack()
"""
    

    if username1 == "":
        Label(loginScreen, text="Username is missing.", width=20, height=1).pack()
    elif password1 == "":
        Label(loginScreen, text="Password is missing.", width=20, height=1).pack()
    elif username1:
        #dbCursor.execute("SELECT pID FROM Testertest WHERE pID='" + username1 + "'")
        dbCursor.execute("SELECT pID FROM Testertest WHERE pID=%s", (username1,))
        #record = dbCursor.fetchone()
        for x in dbCursor:
                print(x)
        if password1:
            #dbCursor.execute("SELECT pw FROM Testertest WHERE pw='" + password1 + "'")
            dbCursor.execute("SELECT pw FROM Testertest WHERE pw=%s", (password1,))
            #record = dbCursor.fetchone()
            
            for x in dbCursor:
                print(x)
            #dbCursor.execute("SELECT * FROM Testertest WHERE pID=%s AND pw=%s", (username1, password1,))

        if username1 == checkUser and password1 == checkPass:
            screen.deiconify()
            login_success(loginScreen)
        else:
            Label(loginScreen, text="Username or Password is incorrect.").pack()
            Label(loginScreen, text="Please try again.").pack()
"""

    list_of_files = os.listdir()
    
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        file1.close()
        if password1 in verify:
            print("Login Success!")
            screen.deiconify()
            login_success(loginScreen)
        else:
            print("Password not recognized")
            password_not_recognized()
    else:
        print("User not found")
        user_not_found()
"""

def close():
    screen.destroy()

def login():
    screen.withdraw()
    global loginScreen
    loginScreen = Toplevel(screen)
    setScreen(loginScreen, "Login", "300x250")
    Label(loginScreen, text="Enter your creds below").pack()
    Label(loginScreen, text="").pack()

    global username_verify
    global password_verify
    global username_entry
    global password_entry

    username_verify = StringVar()
    password_verify = StringVar()

    Label(loginScreen, text="Username*").pack()
    username_entry1 = Entry(loginScreen,textvariable=username_verify)
    username_entry1.pack()
    username_entry1.focus()
    Label(loginScreen, text="").pack()
    Label(loginScreen, text="Password*").pack()
    password_entry1 = Entry(loginScreen,textvariable=password_verify)
    password_entry1.pack()
    Label(loginScreen, text="").pack()
    loginButton = Button(loginScreen, text = "Login", width=10, height=1, command=login_verify_button)
    loginButton.pack(side = RIGHT)
    loginScreen.bind('<Return>', login_verify)
    Label(loginScreen, text="").pack(side = RIGHT)
    Button(loginScreen, text="Close", width=10, height=1, command=close).pack(side = RIGHT)                  

def add_button():
    Button(screen, text='New Button', command=add_button).pack()
    
def launchSite(siteName): 
    wordThings.addDetailToWord()
    import driverConfig
    global driver
    driver = driverConfig.Driver
    driver.get(siteName)

def takeScreenshot():
    screenshot = "hellooo"
    driver.save_screenshot(screenshot + ".png")
    wordThings.addScreenShot(screenshot,"Manual Screenshot")

def quitDriver():
    driver.quit()

def testControlsScreen():
    controlsScreen = Toplevel(screen)
    setScreen(controlsScreen, "Test Controls", "700x500")
    Label(controlsScreen, text = "QStack - Test Control Screen", bg = "blue", width = "300", height = "2", font = ("Calibri", 16)).pack()

    Label(controlsScreen, text = "").pack()
    Button(page1, text = "Run NDEL", width=17, height=1).pack()

    Label(controlsScreen, text = "").pack()
    Button(controlsScreen, text = "Maximize Window", bg="green", width=17, height=1).pack()

    Label(controlsScreen, text = "").pack()
    Button(controlsScreen, text = "Run D2C", height = "2", width = "20").pack()
    
    Label(controlsScreen, text = "").pack()
    Button(controlsScreen, text = "Launch Retail UI Test Controller", height = "2", width = "30").pack()

def logout():
    print("logged out")
    login()
    screen.withdraw()

def main_screen():
    global screen
    screen = Tk()
    login()
    createTab()
    screen.geometry("700x500")
    screen.title("Notes 1")
    #Label(page1, text = dbCursor.execute("SELECT "), bg = "orange", width = "300", height = "2", font = ("Calibri", 16)).pack()

    #PAGE 1 - HOME TAB/DASHBOARD
    Label(page1, text = "QStack", bg = "orange", width = "300", height = "2", font = ("Calibri", 16)).pack()
    Label(page1, text = "").pack()

    #PAGE 2 - TEST CONTROL
    Label(page2, text = "QStack", bg = "orange", width = "300", height = "2", font = ("Calibri", 16)).pack()
    Label(page2, text = "").pack()
    Button(page2, text = "Launch Test Controls", height = "2", width = "30", command = testControlsScreen).pack()

    #PAGE 3 - ACCOUNT SETTINGS
    Label(page3, text = "QStack", bg = "orange", width = "300", height = "2", font = ("Calibri", 16)).pack()
    Label(page3, text = "").pack()
    Button(page3, text = "Register", height = "2", width = "30", command = register).pack()
    logoutButton = Button(page3, text="Logout", height = "2", width = "30", command=logout)
    logoutButton.pack()

    screen.mainloop()
main_screen()
    