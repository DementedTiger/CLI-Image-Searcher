import urllib3
import time


def get_response(url):
    # A http object is created using urllib3
    http = urllib3.PoolManager()
    # A response object is received using the http object
    r = http.request('GET', url)
    if r.status == 200:
        return r
    else:
        return None


def input_search(string, element):
    element.send_keys(string)
    # A small wait is issued to prevent any mismatch in browser response to selenium request
    time.sleep(0.2)


def get_attribute(element, attr):
    value = element.get_attribute(attr)
    return value


