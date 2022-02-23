import config.driverConfig as driverConfig

driver = driverConfig.Driver

def loginToSite():
    manageAcc = driver.find_element_by_link_text('Manage Account')
    manageAcc.click()