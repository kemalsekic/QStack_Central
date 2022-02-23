from tkinter import *
import Reporting.wordThings as wordThings
import DriverManager.runTests as runTests
import Views.D2C_UI as D2C_UI

def launchSite(siteName): 
    wordThings.addDetailToWord()
    import config.driverConfig as driverConfig
    global drivers
    drivers = driverConfig.Driver
    drivers.get(siteName)

def loginToAccount():
    D2C_UI.loginToAccount(drivers)

def enterCreds():
    D2C_UI.enterCreds(drivers, wordThings.docName)

def clickSignInButton():
    D2C_UI.clickSignInButton(drivers, wordThings.docName)

def clickDevicesTab():
    D2C_UI.clickDevicesTabButton(drivers, wordThings.docName)

def clickAddALineButton():
    D2C_UI.clickAddALineButton(drivers, wordThings.docName)
    
def loadDevicesAndClickNext():
    D2C_UI.loadDevicesAndClickNext(drivers, wordThings.docName)

def enterSSN():
    D2C_UI.enterSSN(drivers, wordThings.docName)

def enterDOB():
    D2C_UI.enterDOB(drivers, wordThings.docName)

def clickContine():
    D2C_UI.clickContine(drivers, wordThings.docName)
    
def clickBTGPlan():
    D2C_UI.clickBTGPlan(drivers, wordThings.docName)
    
def enterDeviceNickName():
    D2C_UI.enterDeviceNickName(drivers, wordThings.docName)

def clickAddToCart():
    D2C_UI.clickAddToCart(drivers, wordThings.docName)
    
def clickContinueToCart():
    D2C_UI.clickContinueToCart(drivers, wordThings.docName)

def clickSignOutButton():
    D2C_UI.clickSignOutButton(drivers, wordThings.docName)

def runE2ETest():
    D2C_UI.loginToAccount(drivers)
    D2C_UI.enterCreds(drivers, wordThings.docName)
    D2C_UI.clickSignInButton(drivers, wordThings.docName)
    D2C_UI.clickDevicesTabButton(drivers, wordThings.docName)
    D2C_UI.clickAddALineButton(drivers, wordThings.docName)
    D2C_UI.loadDevicesAndClickNext(drivers, wordThings.docName)
    D2C_UI.enterSSN(drivers, wordThings.docName)
    D2C_UI.enterDOB(drivers, wordThings.docName)
    D2C_UI.clickContine(drivers, wordThings.docName)
    D2C_UI.clickBTGPlan(drivers, wordThings.docName)
    D2C_UI.enterDeviceNickName(drivers, wordThings.docName)
    D2C_UI.clickAddToCart(drivers, wordThings.docName)
    D2C_UI.clickContinueToCart(drivers, wordThings.docName)
    D2C_UI.clickSignOutButton(drivers, wordThings.docName)


def runD2CScreen(screen):
    d2cScreen = Toplevel(screen)
    d2cScreen.title("D2C Controls")
    d2cScreen.geometry("700x500")
    Label(d2cScreen, text = "QStack - D2C Controls", bg = "blue", width = "300", height = "2", font = ("Calibri", 16)).pack()
    
    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Run E2E Test", bg="orange", width=17, height=1, command = runE2ETest).pack()

    Label(d2cScreen, text = "").pack()
    Label(d2cScreen, text = "Individual Test Steps").pack()

    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Login", width=17, height=1, command = loginToAccount).pack()

    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Enter Creds", width=17, height=1, command = enterCreds).pack()

    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Click Sign In Button", width=17, height=1, command = clickSignInButton).pack()
    
    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Click Devices tab", width=17, height=1, command = clickDevicesTab).pack()
    
    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Click Add A Line", width=17, height=1, command = clickAddALineButton).pack()
    
    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Click Next Button", width=17, height=1, command = loadDevicesAndClickNext).pack()

    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Enter SSN", width=17, height=1, command = enterSSN).pack()

    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Enter Date of Birth", width=17, height=1, command = enterDOB).pack()

    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Click Continue", width=17, height=1, command = clickContine).pack()

    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Click BTG Plan", width=17, height=1, command = clickBTGPlan).pack()

    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Enter Device Nick Name", width=17, height=1, command = enterDeviceNickName).pack()

    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Click Add To Cart", width=17, height=1, command = clickAddToCart).pack()


    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Click Continue To Cart", width=17, height=1, command = clickContinueToCart).pack()
      
    Label(d2cScreen, text = "").pack()
    Button(d2cScreen, text = "Click Sign Out Button", width=17, height=1, command = clickSignOutButton).pack()

    launchSite('https://buy-uat.spectrummobile.com/')
    