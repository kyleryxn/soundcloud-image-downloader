import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='soundcloud_image_downloader',
                 packages=['soundcloud_image_downloader'],
                 install_requires=install_requires)
