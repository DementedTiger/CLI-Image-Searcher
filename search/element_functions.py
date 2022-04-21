import search.search_functions as search


def get_attr_elements(elements, limit):
    # An empty list is used to store the image urls from the search
    attributes = []
    count = 0
    # A for loop iterates through each element of the array
    for element in elements:
        attr = search.get_attribute(element, 'src')
        if attr.startswith("https"):
            count += 1
            attributes.append(attr)
        if count >= limit:
            break
    return attributes
