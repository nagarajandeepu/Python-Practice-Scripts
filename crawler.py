from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = "https://www.flipkart.com/laptops/pr?sid=6bo,b5g"

response=requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,'lxml')
print("soup",soup)
i = 0
for item in soup.select('_1AtVbE'):
    try:
        print('----------------------------------------')
        #print(item)
        i=i+1
        print(i)
        print(item.select('_4rR01T')[0].get_text().strip()) #Name of Product
        print(item.select('_30jeq3 _1_WHN1')[0].get_text().strip()) #Price
    #print(item.select('.a-icon-row i')[0].get_text().strip())
    #print(item.select('.a-icon-row a')[1].get_text().strip())
    #print(item.select('.a-icon-row a')[1]['href'])
        print(item.select('_396cs4 _3exPp9')[0]['src']) #image
    except Exception as e:
    #raise e
        print('')