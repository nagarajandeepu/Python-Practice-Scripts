from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://www.amazon.in/gp/browse.html?node=1375424031&ref_=nav_em_sbc_mobcomp_laptops_0_2_8_15'
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,'lxml')
i = 0
for item in soup.select('.zg-item-immersion'):
  try:
    print('----------------------------------------')
    #print(item)
    i=i+1
    print(i)
    print(item.select('.p13n-sc-truncate')[0].get_text().strip())
    print(item.select('.p13n-sc-price')[0].get_text().strip())
    #print(item.select('.a-icon-row i')[0].get_text().strip())
    #print(item.select('.a-icon-row a')[1].get_text().strip())
    #print(item.select('.a-icon-row a')[1]['href'])
    print(item.select('img')[0]['src'])
  except Exception as e:
    #raise e
    print('')