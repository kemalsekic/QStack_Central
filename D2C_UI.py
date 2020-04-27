import os
import pprint
import subprocess
import configStuff
import deviceDetail
from os import system, name
import stagingFile
import driverThings
import wordThings

def launchSpectrumSite(theDriver, docName):
    theDriver.get('https://buy-uat.spectrummobile.com/')

#Wait for element to display then click it
def loginToAccount(theDriver):
    driverThings.waitForElementByLinkText(theDriver)
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(wordThings.docName, "Logging into site: https://buy-uat.spectrummobile.com/")
    theDriver.find_element_by_link_text('Manage Account').click()

def enterCreds(theDriver, docName):
    #Finding elements on page and type elemnts into fields
    #8245100010088504@charter.net
    #8245124000228185@charter.net
    #8345780121546034
    driverThings.waitForLoginPage(theDriver)
    theDriver.save_screenshot(docName + ".png")
    wordThings.addScreenShot(docName, "Page loaded")

    UNField = theDriver.find_element_by_id("username")
    passField = theDriver.find_element_by_id("password")

    UNField.send_keys(stagingFile.uName)
    passField.send_keys(stagingFile.pWord)
    theDriver.save_screenshot(docName + ".png")
    wordThings.addScreenShot(docName, "Entered username and password")

def clickSignInButton(theDriver, docName):
    driverThings.waitForSignInButton(theDriver)
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Clicking Sign In")
    theDriver.find_element_by_xpath(".//*[contains(@class, 'button-lbg--primary')]").click()

def clickDevicesTabButton(theDriver, docName):
    driverThings.waitForDeviceButton(theDriver)
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Click on Devices tab")
    theDriver.find_element_by_xpath(".//*[contains(@href, '/manage-account/devices')]").click()

def clickAddALineButton(theDriver, docName):
    driverThings.waitForAddALine(theDriver)
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Adding a line")
    addALineButton = theDriver.find_element_by_class_name('add-content')
    theDriver.execute_script("arguments[0].click();", addALineButton)

def loadDevicesAndClickNext(theDriver, docName):
    driverThings.waitForDeviceList(theDriver)
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Device list is displayed")
    theDriver.find_element_by_xpath(".//*[(contains(@href, '/products/phone/iphone-11-pro-apple?colorName=Midnight%20Green'))]").click()

    driverThings.waitForNextButton(theDriver)
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Clicking next button here")
    theDriver.find_element_by_xpath(".//*[contains(@class, 'button--primary next-btn')]").click()

def enterSSN(theDriver, docName):
    driverThings.waitForSSNInput(theDriver)
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "SSN Input is loaded")

    theDriver.find_element_by_id("ssn").send_keys(stagingFile.ssn)
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Entered SSN")

def enterDOB(theDriver, docName):
    theDriver.find_element_by_id("month").send_keys(stagingFile.dobMonth)
    theDriver.find_element_by_id("date").send_keys(stagingFile.dobDay)
    theDriver.find_element_by_id("year").send_keys(stagingFile.dobYear)

    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Entered date of birth: " + stagingFile.dobMonth + "/" + stagingFile.dobDay + "/" + stagingFile.dobYear)

def clickContine(theDriver, docName):
    theDriver.find_element_by_xpath("//span[text()='CONTINUE']").click()

def clickBTGPlan(theDriver, docName):
    driverThings.waitForByTheGigCard(theDriver)
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Gig Plans Loaded")

    theDriver.find_element_by_xpath(".//h3[contains(@class, 'title')]").click()
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Selected By The Gig Plan")

#driverThings.waitForKeepMyNumber()
#driver.find_element_by_id("phone-number-Keepmyphonenumber").click()
#addScreenShot(docName, "")

def enterDeviceNickName(theDriver, docName):
    driverThings.waitForDeviceNickName(theDriver)
    theDriver.find_element_by_xpath("//div[@class='personalize']//input").send_keys("HeyAll1")
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Entered Device Nick-Name")

def clickAddToCart(theDriver, docName):
    #//p[@class='customizer-plan__price']
    driverThings.waitForAddToCartButton(theDriver)
    theDriver.find_element_by_xpath("//div[@class='customizer-step']//button[contains(text(), 'Add to Cart')]").click()
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Added to Cart")

def clickContinueToCart(theDriver, docName):
    driverThings.waitForContinueToCartButton(theDriver)
    theDriver.find_element_by_xpath("//button[contains(text(), 'Continue to Cart')]").click()
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Clicked Continue to Cart")

def clickSignOutButton(theDriver, docName):
    driverThings.waitForSignOutButton(theDriver)
    theDriver.find_element_by_link_text('Sign Out').click()
    driverThings.waitForAccessLink(theDriver)
    theDriver.save_screenshot(wordThings.docName + ".png")
    wordThings.addScreenShot(docName, "Signed Out")
