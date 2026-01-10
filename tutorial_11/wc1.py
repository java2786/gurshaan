import requests
from bs4 import BeautifulSoup

# url = "https://en.wikipedia.org/wiki/India"
# url = "https://www.flipkart.com/"
url = "https://example.com/"

# send request to url
response = requests.get(url)

print("Status code:", response.status_code)

if(response.status_code==200):
    # print("Res is there")
    # print(response.text)
    # convert / parse html
    soup = BeautifulSoup(response.text, 'html.parser')
    
    heading = soup.find('h1')
    print(heading.text if heading else "No H1 tag found")
    
    links = soup.find_all('a')
    print(len(links))
    for link in links:
        url = link.get("href")
        text = link.string 
        print("Link:",url,", Text:",text)
else:
    print("Server is not allowing the request")
    