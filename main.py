from search import setup, search_functions, element_functions
from download import file_functions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def main():
    try:
        driver = setup.setup_webdriver()
        # Takes in user input as stores it to be used in our search
        search_term = input("Please input a search query...\n")
        driver.get("https://www.google.com/imghp")
        m = driver.find_element(By.NAME, "q")

        # We search for the user input we got
        search_functions.input_search(search_term, m)
        # We use the Keys import to act as a keyboard input to the browser
        # This can be used as a replacement to clicking the search button for a text search
        search_functions.input_search(Keys.ENTER, m)
        # We issue a find_elements to return an array of images through their class name
        images = driver.find_elements(By.CLASS_NAME, "rg_i")

        # Retrieve a requested amount of urls
        # The input is a string so must be converted to int in order to use in the function
        urls = element_functions.get_attr_elements(images, int(input("How many images would you like to download?\n")))
        counter = 0

        for url in urls:
            counter += 1
            file_functions.save_text(f"{search_term}_img_url.txt", url)
            response = search_functions.get_response(url)
            file_functions.save_image(response, f"{search_term}_{counter}.jpg")

        print("Done!")

    finally:
        driver.close()


if __name__ == '__main__':
    main()
