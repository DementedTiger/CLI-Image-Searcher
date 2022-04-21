from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def setup_webdriver():
    # Create a service object with the driver of the browser you are testing
    ser = Service("Drivers/chromedriver.exe")
    # Create an options object based on the browser type
    op = webdriver.ChromeOptions()
    # Generate the webdriver using both
    driver = webdriver.Chrome(service=ser, options=op)
    # Implicit wait directs the Selenium WebDriver to wait before an exception is thrown
    # if the element it is trying to interact with does not appear

    driver.implicitly_wait(0.5)
    return driver
