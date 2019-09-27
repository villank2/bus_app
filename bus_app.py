import requests
from bs4 import BeautifulSoup

def main():
    payload = {'searchtype': 'view','searchquery':12}
    dbus = requests.get('https://www.dublinbus.ie/RTPI/Sources-of-Real-Time-Information/?',params=payload)
    soup = BeautifulSoup(dbus.content, 'html.parser')
    t = soup.find('table',{'id':'rtpi-results'})
    
if __name__ == '__main__':
    main()