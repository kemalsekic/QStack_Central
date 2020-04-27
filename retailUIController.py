from tkinter import *
import wordThings
import runTests
import retailUITestCases

def launchSite(siteName): 
    wordThings.addDetailToWord()
    import driverConfig
    global drivers
    drivers = driverConfig.Driver
    drivers.get(siteName)

def enterStoreDetail():
    retailUITestCases.enterStoreDetail(drivers, wordThings.docName)

def goToGW():
    drivers.get("https://chtrgwy-uat.corp.chartercom.com/static/gateway/beta/#/dashboard")
    #drivers.get("https://retail-uat.spectrummobile.com/?route=manage&session=arTFLkn+P86iV9Ugfe9VhRqiM5597I/aHJUIjIr7bsBPlcq8V+BA0uO8L+WwabKJHKGYgSTBQt7v+nKzW67n/3w7m+FTOmgcW6Rd17rzpsloa+mAARih6a92JFamt+UX92wyuvX1TMmbL0XfdXO04Hb+Fx0AYR+9D8QUH/zn/MRSlLihyzAatzs1vOBm/5UimS7iBB/KYWe/IkvgbgXz6nYNYWqbNZptCn+7YAFrsh+kqHoDXQMUxuKhjFkIB3CEiSMscwxAkUdSFE5wgOYEBbzIgfXUxO2VBB1cN72ANp2kdejy2LomqU7eif4V3lxRATBrvdB8ZWrL3NFgKEOud2Eb7u0xre57H3SNpaHL+K5TMyohjm6CkOegOc7ByOjoqUJoxsL3bxTegTlKZjNqUQwl6D+k9AaHU/U0SgbI+oK3QYAF3a+CuVvdroCUzewNYqybMF3TywaD0XgBuz7Zbjer0QVwLNECnCetieYvN5lIBXEtzOQtEYJiBZonnpyYy4IQ/+D3BJRaenWWNxCswQoDa7dmjJmhp0VOCIYBHGrweHs2eeizgeYVfXzalT1MloZPspfhmqv2HN5/1XMVonZDP+RWUkYyQRYy+HyZC52d+nGmL+Q6i3jVtlLOW7Am3PhczBcHKWIeh6xjqwob1NooD9TBIaaZ+4+iaWXVd1U=&msat=eyJhbGciOiJIUzI1NiJ9.eyJjaXR5IjoiIiwiY3VzdG9tZXJWZXJpZmljYXRpb25NZXRob2RlIjoiIiwiZ3VpZCI6IlAyOTM4MjE0IiwiemlwNCI6IiIsInN0b3JlTmFtZSI6IiIsInN0b3JlU3RhdGUiOiIiLCJzdG9yZW51bSI6IiIsImV4cCI6MTU4NTI0NjQ2NCwiZGV2aWNlaWQiOiIiLCJjaGFubmVsY29kZSI6IlJFVEFJTCIsImRldmljZUlEIjoiIn0.tscU1-raoTtoKXw8ZdwWO9i8FDPoBLv_I9G23eHIVWY&accesstoken=eyJhbGciOiJIUzI1NiJ9.eyJjdXN0b21lckd1aWQiOiI4NjQ2Njg2OCIsImV4cCI6MTU4NTI0NjQ2NCwidWNhbiI6Ijg2NDY2ODY4In0.f82tBhM9brCMsior-dmavQqxxl3HRPdpw1kuF6wN4uU&agentID=P2938214&AcctGUID=86466868Comcast.RTVE")

def runRetailUIScreen(screen):
    retailUIScreen = Toplevel(screen)
    retailUIScreen.title("D2C Controls")
    retailUIScreen.geometry("700x500")
    Label(retailUIScreen, text = "QStack - D2C Controls", bg = "blue", width = "300", height = "2", font = ("Calibri", 16)).pack()
    
    Label(retailUIScreen, text = "").pack()
    Button(retailUIScreen, text = "Enter Store Details", bg="orange", width=17, height=1, command = enterStoreDetail).pack()

    Label(retailUIScreen, text = "").pack()
    Button(retailUIScreen, text = "Go to Gateway", bg="orange", width=17, height=1, command = goToGW).pack()

    launchSite('https://chtrgwy-uat.corp.chartercom.com/static/impersonation-portal/current/')