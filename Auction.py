from bs4 import BeautifulSoup
import requests
import smtplib


HEADERS = ({'User-Agent':'Mozilla/5.0'})



url = 'https://www.treasury.gov/auctions/treasury/rp/realprop.shtml'
#url = 'https://automatetheboringstuff.com/2e/chapter10/'

#url = 'https://datascienceatthecommandline.com/2e/chapter-2-getting-started.html'


data = requests.get(url, headers = HEADERS,verify=False)




soup = BeautifulSoup(data.content,"html.parser")

data = soup.find_all('span', class_='style12')

addresses = []
for line in data:
    addresses.append(f'{line} \n')
new_address = []
for address in addresses:
    new_address.append(address[44:])

count = 1
with open('Auctions.txt', 'w') as f:
        for line in new_address:
            f.write(f'\n\n{count}: {line[:-16]} \n')
            count += 1

print(f'finished creating auction list with a total of {count} entries')
