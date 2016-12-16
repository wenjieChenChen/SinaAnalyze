import bs4
import  requests
from urllib import request

url = request.urlopen("http://www.sina.com")

WebsiteData = url.read()

# print(WebsiteData)

result = bs4.BeautifulSoup(WebsiteData,"html.parser")

for body in result.find_all('a'):
    print(body)

