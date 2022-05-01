import requests
from bs4 import BeautifulSoup

class build:
    def build_champ(nome_champ):
        try:
            url, headers = f'https://probuildstats.com/champion/{nome_champ}', {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.68'}

            r = requests.get(url, headers=headers)
            build_1 = BeautifulSoup(r.content, 'html.parser').find_all('div', class_='side-column_grid-item top-items')
            build_2 = BeautifulSoup(r.content, 'html.parser').find_all('div', class_='item-image completed-item')
            print(build_1[0].find('img').get('alt', ''))
            for build in range(6):
                print(build_2[build].find('img').get('alt', ''))
        except IndexError:
            print('Nome invalido !')
class runas:
    def runas_champ(nome_champ):
        try:
            url, headers = f'https://u.gg/lol/champions/{nome_champ}/build', {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.68'}

            r = requests.get(url, headers=headers)

            soup = BeautifulSoup(r.content, 'html.parser')

            runa = soup.find('div', class_='perk keystone perk-active')
            keystone = runa.find('img')
            print(keystone.get('alt', '').replace('The Keystone', ''))

            other_runes = soup.find_all('div', class_='perk perk-active')
            f = len(other_runes)/2
            for i in range(int(f)):
                print(other_runes[i].find('img').get('alt', '').replace('The Rune', ''))
        except IndexError:
            print('Nome invalido !')


