import urllib3

def get_response(url):
    # A http object is created using urllib3
    http = urllib3.PoolManager()
    # A response object is received using the http object
    r = http.request('GET', url)
    if r.status == 200:
        return r
    else:
        return None