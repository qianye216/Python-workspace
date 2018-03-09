import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq

keyword='beauty'
headers={
 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'accept-encoding':'gzip, deflate,sdch,br',
 'cookie':'__cfduid=d3e43ad7f4bb07152deb3e9b4ca571b271505889614; locale=en; _ga=GA1.2.127776053.1505890636; _gid=GA1.2.783458515.1505890636; _gat=1',
 'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def get_index(url):
    response=requests.get(url,headers=headers)
    try:
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def parse_index(html):
    doc=pq(html)
    links=doc('.photos .photo-item a img')
    for link in links:
        # title=link.attr('alt').replace(',','')
        url=link.attr('data-pin-media').replace('images','static').split('?')[0]
        yield url

def main(page):
    url = 'https://www.pexels.com/search/'+keyword+'/?page='+str(page)
    html=get_index(url)
    if html:
        urls=parse_index(html)
        print(urls)

if __name__=='__main__':
      main(1)

