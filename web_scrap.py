import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
# Send an HTTP Get requests to the url
response = requests.get(url)
#Check if the request was successful.(Status code 200)

if response.status_code==200:
        soup = BeautifulSoup(response.text,"html.parser")
        find_article = soup.find_all("div",class_="medium-widget blog-widget")
        latest_articles = []
        
for article in find_article:
    article_name = article.text
    latest_articles.append(article_name)
    print(latest_articles)
    final_article_name = ''.join(latest_articles)
print(final_article_name)
        
    
    
          
        
        
