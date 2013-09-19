# web page crawler practice
import urlparse
import urllib2
import time
from bs4 import BeautifulSoup

url = "http://www.ccs.neu.edu/"

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,}

urls = [url]
visited = [url]
count = 0
while len(urls) > 0 and count < 100:
    link = urls.pop(0)
    count = count+1
    time.sleep(5) # delays for 5 seconds
    request=urllib2.Request(link,None,headers)
    response = urllib2.urlopen(request)
    data = response.read()
    
    print count
    print link
    
    soup = BeautifulSoup(data)
    
    for tag in soup.findAll('a',href = True):
        tag['href'] = urlparse.urljoin(url,tag['href'])
        if url in tag['href'] and tag['href'] not in visited:
            post = tag['href'][len(url):]
            print post
            visited.append(tag['href'])
            urls.append(tag['href'])


