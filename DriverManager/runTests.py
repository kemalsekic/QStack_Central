import os
import pprint
import subprocess
import config.configStuff as configStuff
import deviceDetails.deviceDetail as deviceDetail
from os import system, name
import deviceDetails.stagingFile as stagingFile
import config.driverThings as driverThings
import Reporting.wordThings as wordThings

#Wait for element to display then click it
#wordThings.addScreenShot(docName, "Logging into site: https://chtrgwy-uat.corp.chartercom.com/static/impersonation-portal/current/")
#loginPage.loginToSite()

def clickRetailButton(theDriver, docName):
    driverThings.NDEL_RetailWait(theDriver)
    theDriver.save_screenshot(docName + ".png")
    wordThings.addScreenShot(docName, "Page loaded")
    theDriver.find_element_by_id("user-input-id").send_keys("retail")
    driverThings.NDEL_RetailWaitButton(theDriver)
    theDriver.find_element_by_xpath("//*[@id='AP-CHTRGWY-Retail-SDP--card']/div[2]/div[2]/button[1]").click()

def goToGateway(theDriver, docName):
    theDriver.get('https://chtrgwy-uat.corp.chartercom.com/static/gateway/beta/#/dashboard')
    driverThings.waitForSearchButton(theDriver)
    theDriver.save_screenshot(docName + ".png")
    wordThings.addScreenShot(docName, "Clicking Search Button")
    theDriver.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiButton-root jss159 MuiButton-text']").click()

def enterAccountNum(theDriver, docName):
    driverThings.waitForAccountNumButton(theDriver)
    theDriver.find_element_by_id("billerAccountNumber").send_keys(stagingFile.accNum)

    theDriver.save_screenshot(docName + ".png")
    wordThings.addScreenShot(docName, "Entered Account Number")

def clickFindAccButton(theDriver, docName):    
    driverThings.waitForGWFindAccButton(theDriver)
    theDriver.find_element_by_xpath("/html/body/div[6]/div[3]/div/div[2]/div/div/form/fieldset/div[3]/button[1]").click()
    
    theDriver.save_screenshot(docName + ".png")
    wordThings.addScreenShot(docName, "Clicked Find Account Button")

def clickVerifyButton(theDriver, docName):
    driverThings.wfverifyButton(theDriver)
    theDriver.find_element_by_xpath(driverThings.verifyButton).click()

    theDriver.save_screenshot(docName + ".png")
    wordThings.addScreenShot(docName, "Clicked Verify Button")

"""
driverThings.wfMobileButton()
driver.find_element_by_xpath(driverThings.mobileButton).click()

driverThings.wfTasksDD()
driver.find_element_by_xpath(driverThings.tasksDropDown).click()

driverThings.wfManageLinesSelect()
driver.find_element_by_xpath(driverThings.manageLinesSelect).click()

#driverThings.wfShopSelect()
#driver.find_element_by_xpath(driverThings.shopSelect).click()
"""