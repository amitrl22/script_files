
import urllib2

import re


sock = urllib2.urlopen('http://www.google.com')

html = sock.read()

s = 'http://'

result = re.findall(s, html)

count = len(result)

sock.close()

print "number of links =",count
