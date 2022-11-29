import os
import requests
from bs4 import BeautifulSoup


def image_downloader(webpage, folder):
    illegal_chars = ['/', '\\', '*', '?', ':', '"', '<', '>', '|']

    r = requests.get(webpage)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')

    for image in images:
        name = image['alt'].lower()
        link = image['src']

        # Replace illegal characters if present
        name.translate({ord(x): '' for x in illegal_chars})

        rename_file = input(f'The image name is "{name}", would you like to rename it? (Y/N) ').lower()

        if rename_file == 'y':
            name = input('Enter new file name: ')

        # Save image in destination folder
        with open(os.path.join(folder, name + '.jpg'), 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
