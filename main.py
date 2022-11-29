import os
from sid import downloader

if __name__ == '__main__':
    directory = 'C:/Users/Kyle/Music/Electronic/'

    url = input(f'Enter the url: ')
    destination = input(f'\nDirectory to save the image: ')

    complete_name = os.path.join(directory, destination)

    downloader.image_downloader(url, complete_name)


