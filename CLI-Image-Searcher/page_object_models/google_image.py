from image_interaction import element_functions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class GoogleImage():
    def __init__(self, driver):
        self.driver = driver
        self.search_input = driver.find_element(By.NAME, "q")

    def search(self, input):
        # We use the Keys import to act as a keyboard input to the browser
        # This can be used as a replacement to clicking the search button for a text search
        self.search_input.send_keys(input)
        self.search_input.send_keys(Keys.ENTER)

    def get_images(self):
        # We issue a find_elements to return an array of images through their class name
        return self.driver.find_elements(By.CLASS_NAME, "rg_i")

    def get_urls(self, images, image_number):
        # An empty list is used to store the image urls from the search
        urls = []
        count = 0
        # A for loop iterates through each element of the array
        # We have to iterate through each element as not every image will have
        # a https url, so we only count up and break when we reach the wanted
        # amount 
        for image in images:
            attr = image.get_attribute('src')
            if attr.startswith("https"):
                count += 1
                urls.append(attr)
            if count >= image_number:
                return urls