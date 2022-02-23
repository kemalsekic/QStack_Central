import os
import pprint
import subprocess
import config.configStuff as configStuff
import deviceDetails.deviceDetail as deviceDetail
from os import system, name
import deviceDetails.stagingFile as stagingFile
import config.driverThings as driverThings
import Reporting.wordThings as wordThings
import DriverManager.runTests as runTests

def launchSpectrumSite(theDriver, docName):
    theDriver.get('https://chtrgwy-uat.corp.chartercom.com/static/impersonation-portal/current/')

def enterStoreDetail(theDriver, docName):
    #driverThings.waitForStoreDetailsPageToLoad(theDriver)
    theDriver.find_element_by_xpath("//div[1]/div[1]/my-input/label/input").send_keys("Texas")
    theDriver.find_element_by_xpath("//div/div/my-store-address/div/form/div[1]/div[2]/my-input/label/input").send_keys("2378")
    theDriver.find_element_by_xpath("//div/div/my-store-address/div/form/div[2]/div/my-input/label/input").send_keys("2132 N Mays St")
    theDriver.find_element_by_xpath("//div/div/my-store-address/div/form/div[3]/div/my-input/label/input").send_keys("Round Rock")
    #theDriver.find_element_by_xpath("//div/div/my-store-address/div/form/div[4]/div[1]/my-select/div/ul/li[45]/a").send_keys("")
    theDriver.find_element_by_xpath("//div/div/my-store-address/div/form/div[4]/div[2]/my-input/label/input").send_keys("78664")
    theDriver.find_element_by_xpath("//div/div/my-store-address/div/form/div[4]/div[3]/my-input/label/input").send_keys("R01")
    theDriver.find_element_by_xpath("//div/div/div[1]/div/form/div/div/my-radio-btn/form/div/div[1]/label").click()
    theDriver.find_element_by_xpath("//div/div/div[2]/div/my-btn[2]/button").click()
    


#https://chtrgwy-uat.corp.chartercom.com/static/gateway/beta/#/dashboard