 
import requests
from  bs4 import BeautifulSoup
import json
URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')



def get_citations_needed_count(url):
    Num_Citation_needed = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")    

    return len(Num_Citation_needed)
    
def  get_citations_needed_report(URL):
     paragraphs =soup.find_all('sup', class_="noprint Inline-Template Template-Fact") 
    
     for par in paragraphs:
            pa=par.parent.text
            print (par.parent.text)
    
 
 

print(get_citations_needed_count(URL))


get_citations_needed_report(URL)
# for par in all_paragraphs:
#     pa=par.parent.text
#     print (par.parent.text)
# print(needed_report)


# data_count = json.dumps(len(needed_count))
# dete_paragraphs=json.dumps(pa)
# with open ('result.json','w') as file:
#     file.write(data_count)
#     file.write(pa)