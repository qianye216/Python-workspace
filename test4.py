from pyquery import PyQuery as pq
import requests

doc = pq(url='http://www.ygdy8.com/html/gndy/dyzz/20180306/56451.html')

print(doc('title'))