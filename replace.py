import urllib2

def html(url, old, new):
    code = str(urllib2.urlopen(url).read())
    return code.replace(old, new)
