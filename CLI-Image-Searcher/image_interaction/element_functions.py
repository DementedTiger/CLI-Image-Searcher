def get_attr_elements(elements, limit):
    # An empty list is used to store the image urls from the search
    attributes = []
    count = 0
    # A for loop iterates through each element of the array
    # We have to iterate through each element as not every image will have
    # a https url, so we only count up and break when we reach the wanted
    # amount 
    for element in elements:
        attr = get_attribute(element, 'src')
        if attr.startswith("https"):
            count += 1
            attributes.append(attr)
        if count >= limit:
            break

    return attributes

def get_attribute(element, attr):
    value = element.get_attribute(attr)
    print(value)
    return value