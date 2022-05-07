def save_image(response, image_name):
    with open(image_name, "wb") as f:
        # we write the contents of the file using the r.data to get the contents of the
        # response object from the url
        f.write(response.data)
    print('Image was downloaded!')


def save_text(file_name, text):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(text + '\n')

