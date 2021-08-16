import requests
from bs4 import BeautifulSoup



def get_citations_needed_count(url):
    response  = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    result=soup.find_all('sup',class_='noprint Inline-Template Template-Fact')
   
    return f'{len(result)} citations needed'
    

