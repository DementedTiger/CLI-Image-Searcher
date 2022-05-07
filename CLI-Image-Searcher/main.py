from search import setup
from download import file_functions, downloading
from page_object_models.google_image import GoogleImage


def main():
    try:
        # We use the user created setup function to organize the process of
        # Making the driver. Look at the setup file to see how this is done
        driver = setup.setup_webdriver()
        driver.get("https://www.google.com/imghp")

        # We use an Object to store the Page representation
        # This is useful, incase the page changes in the future we only have to
        # Update it one location (the class) but the functions remain the same
        # In our code
        image_home = GoogleImage(driver)

        # Takes in user input as stores it to be used in our search
        search_term = input("Please input a search query...\n")

        # We search for the user input we got
        image_home.search(search_term)
        
        # The object method get_images() returns an array of images searched
        images = image_home.get_images()

        # We ask the user how many images they want to download
        # The input is a string so must be converted to int in order to use as
        # a number
        image_number = int(input("How many images do you want to download?\n"))

        # We get the urls of the images using the user made function element_function
        # Look at how it is implemented to know how this is done
        urls = image_home.get_urls(images, image_number)

        for i in range(image_number):
            file_functions.save_text(f"{search_term}_img_url.txt", urls[i])
            response = downloading.get_response(urls[i])
            file_functions.save_image(response, f"{search_term}_{i+1}.jpg")

        print("Done!")
    finally:
        driver.close()


if __name__ == '__main__':
    main()
