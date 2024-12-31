from page_objects.CheckoutPage import CheckoutPage
from utilities.data_reader import read_json, read_excel
from keywords.keywords import xstr
import pytest
from time import sleep

config = read_json("D:\Selenium Practices\Week 6\config\config.json")

testDataPath = config["test_data"]["file_path"]
testDataSheet = config["test_data"]["TC_2_sheet_name"]

sleepTime = config["browser"]["sleep_time"]

def getTestData():
    return read_excel(testDataPath, testDataSheet)

@pytest.mark.parametrize("tc_id, name, password, expected, addItems, removeItems, firstName, lastName, PostalCode, ExpectedAction", getTestData())
def test_shopping(setup_browser, log, tc_id, name, password, expected, addItems, removeItems, firstName, lastName, PostalCode, ExpectedAction):
    log.info("Executing "+ tc_id + " with " + xstr(name) + " as username and " + xstr(password) + " as password..." )
    driver = setup_browser
    log.info("Starting browser session...")
    shopping = CheckoutPage(driver)
    log.info("Entering login credentials...")
    shopping.login(xstr(name), xstr(password))
    sleep(sleepTime)
    
    log.info("Validating login...")
    result = shopping.validatelogin()
    if result == "Pass":
        log.info("Logged in successfully")
    else:
        log.error(shopping.getErrorText())
    log.info("Login Check performed successfully...")
    try:
        assert expected == result
        if result == "Pass":
            log.info("Adding required items to cart..")
            itemsToAdd = xstr(addItems).split(", ")
            itemsToRemove = xstr(removeItems).split(", ")
            for item in itemsToAdd:
                log.info("Adding "+ item +" to cart..")
                shopping.addItem(item)
                sleep(sleepTime)
            log.info("Proceeding to cart..")
            shopping.proceedToCart()
            for item in itemsToRemove:
                log.info("Removing "+ item +" from cart..")
                shopping.removeItem(item)
                sleep(sleepTime)
            shopping.proceedToCheckout()
            log.info("Proceeding to checkout..")
            log.info("Entering form details..")
            sleep(sleepTime)
            shopping.formSubmit(xstr(firstName), xstr(lastName), xstr(PostalCode))
            formResult = shopping.validateForm()
            if formResult == "Pass":
                log.info("Completing the transaction...")
            else:
                log.error(shopping.getErrorText())
            try:
                assert ExpectedAction == formResult
                sleep(sleepTime)
                shopping.finishShopping()
                sleep(sleepTime)
                shoppingResult = shopping.validateShopping()
                if shoppingResult == "Pass":
                    log.info("Shopping completed successfully...")
                else:
                    log.info("Shopping is hindered...")
                    raise AssertionError("Expectation not met")
            except Exception as e:
                log.error("Something went wrong..."+ str(e))    
    except Exception as e:
        log.error("Something went wrong..."+ str(e))
    finally:
        log.info("Quitting the browser session...")