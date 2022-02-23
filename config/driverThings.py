import os
import pprint
import subprocess
import webbrowser
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

def waitForAccessLink(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH,"//*[contains(@href, '/support/article/360000718907/accessibility-options')]")))

def waitForElementByLinkText(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "Manage Account")))

def waitForSignOutButton(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign Out")))
    
def waitForSignInButton(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH,".//*[contains(@class, 'button-lbg--primary')]")))

def waitForDeviceButton(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH,".//*[contains(@href, '/manage-account/devices')]")))

def waitForLoginPage(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.ID,"username")))

def waitForAddALine(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"add-content")))

def waitForDeviceList(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH,".//*[contains(@href, '/products/phone/iphone-11-pro-apple?colorName=Midnight%20Green')]")))
    
def waitForNextButton(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH,".//*[contains(@class, 'button--primary next-btn')]")))

def waitForSSNInput(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.ID,"ssn")))

def waitForByTheGigCard(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH, ".//h3[contains(@class, 'title')]")))

def waitForKeepMyNumber(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.ID, "phone-number-Keepmyphonenumber")))
    
def waitForDeviceNickName(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='personalize']//input")))

def waitForAddToCartButton(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='customizer-step']//button[contains(text(), 'Add to Cart')]")))

def waitForContinueToCartButton(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Continue to Cart')]")))

def NDEL_RetailWait(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.ID, "user-input-id")))

def NDEL_RetailWaitButton(theDriver):
    WebDriverWait(theDriver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='AP-CHTRGWY-Retail-SDP--card']/div[2]/div[2]/button[1]")))

###Gateway
def waitForSearchButton(theDriver):
    WebDriverWait(theDriver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root jss159 MuiButton-text']")))

def waitForAccountNumButton(theDriver):
    WebDriverWait(theDriver, 10).until(EC.presence_of_element_located((By.ID, "billerAccountNumber")))

def waitForGWFindAccButton(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div/div/form/fieldset/div[3]/button[1]")))

#gateway
verifyButton = "//div[6]/div[3]/div[3]/div/div[1]/button"
mobileButton = '//*[@id="container"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[3]/div/button[6]'
tasksDropDown = "//*[@id='container']/div/div[2]/div[1]/div[1]/div[2]/div/div[6]/div/div/div/div/div[1]/div[4]/div/div[1]/div/div/div[2]/div/button"
manageLinesSelect = "//*[@id='container']/div/div[2]/div[1]/div[1]/div[2]/div/div[6]/div/div/div/div/div[1]/div[4]/div/div[1]/div/div/div[2]/div/ul/div/span[1]"
shopSelect = "//*[@id='container']/div/div[2]/div[1]/div[1]/div[2]/div/div[6]/div/div/div/div/div[1]/div[4]/div/div[1]/div/div/div[2]/div/ul/div/span[2]"

#Store Detail
storeName = "//div/div/my-store-address/div/form/div[1]/div[1]/my-input/label/input"
storeNum = "//div/div/my-store-address/div/form/div[1]/div[2]/my-input/label/input"
storeAdd = "//div/div/my-store-address/div/form/div[2]/div/my-input/label/input"
storeCity = "//div/div/my-store-address/div/form/div[3]/div/my-input/label/input"
storeState = "//div/div/my-store-address/div/form/div[4]/div[1]/my-select/div/ul/li[45]/a"
storeZip = "//div/div/my-store-address/div/form/div[4]/div[2]/my-input/label/input"
storeTerminalID = "//div/div/my-store-address/div/form/div[4]/div[3]/my-input/label/input"
storeIDType = "//div/div/div[1]/div/form/div/div/my-radio-btn/form/div/div[1]/label"
storeSubmitButton = "//div/div/div[2]/div/my-btn[2]/button"

def wfverifyButton(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH, verifyButton)))

def wfMobileButton(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH, mobileButton)))

def wfTasksDD(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH, tasksDropDown)))

def wfManageLinesSelect(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH, manageLinesSelect)))
    
def wfShopSelect(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH, shopSelect)))


####Retail UI Stuff
def waitForStoreDetailsPageToLoad(theDriver):
    WebDriverWait(theDriver, 30).until(EC.presence_of_element_located((By.XPATH,"//div/div/div[1]/div/form/div/div/my-radio-btn/form/div/div[1]/label")))
