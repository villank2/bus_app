import requests
from bs4 import BeautifulSoup
import sys
def main():
    num = sys.argv[1]
    resp = fetch(num)
    table = cook_soup(resp)
    output = (table.find_all('td'))
    show(output)
    

def fetch(stop_num):
    payload = {'searchtype':'view','searchquery':stop_num}
    dbus = requests.get('https://www.dublinbus.ie/RTPI/Sources-of-Real-Time-Information/?',params=payload)
    return dbus.content

def cook_soup(content):
    soup = BeautifulSoup(content,'html.parser')
    table = soup.find('table',{'id':'rtpi-results'})
    return table

def show(output):
    string = ''
    for out in output:
        string += '-' + (str(out.string).strip()) 
    li = (string.split('None'))
    for real_time in li:
        print(real_time)
if __name__ == '__main__':
    main()