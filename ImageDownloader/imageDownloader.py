#!/usr/bin/python3

"""imageDownloader.py: Downloads all the images from a web page."""

__author__ = 'andrei.muntean.dev@gmail.com (Andrei Muntean)'

import os.path
import re
import sys
from urllib.request import urlopen, urlretrieve

IMG_EXTENSIONS = ('.gif', '.jpg', '.png')

def get_input_url():
    url = ''

    if len(sys.argv) == 3:
        url = sys.argv[1]
    else:
        print('Please specify a URL.')
        url = input('> ')

    # Defaults to HTTP if no protocol was specified.
    if not '//' in url:
        url = 'http://' + url

    return url

def get_input_destination():
    if len(sys.argv) == 3:
        return sys.argv[2]
    else:
        print('Where would you like to download the images?')
    
        return input('> ')

def get_img_urls(url):
    response = urlopen(url, timeout=5)
    html = str(response.read())
    img_urls = []

    for extension in IMG_EXTENSIONS:
        for occurrence in re.finditer(extension, html):
            # Determines whether the URL is contained within a single quote or a double quote.
            delimiter = '\'' if html[occurrence.end()] == '\'' else '"'

            # Gets the starting position of the URL.
            url_start = html[:occurrence.start()].rfind(delimiter) + 1

            # Gets the URL.
            img_url = html[url_start:occurrence.end()]

            # Turns relative paths into absolute paths.
            if img_url[0] == '/':
                img_url = url + img_url

            # Stores the URL if it hasn't already been stored.
            if not img_url in img_urls:
                img_urls.append(img_url)
    
    return img_urls

def download(img_urls, destination):
    """Downloads the images from the given URLs into the specified destination."""
    
    if not os.path.exists(destination):
        print('Creating directory \'%s\'.' % destination)
        os.makedirs(destination)

    for img_url in img_urls:
        # Sets the image name as the string that follows the last '/' in the URL.
        img_name = img_url[img_url.rfind('/') + 1:]

        try:
            # Downloads the image in the specified folder.
            urlretrieve(img_url, os.path.join(destination, img_name))
            print('Downloaded \'%s\'.' % img_name)
        except:
            pass

def run():
    """Runs the program."""

    url = get_input_url()
    destination = get_input_destination()

    try:
        download(get_img_urls(url), destination)
        print('Download complete.')
    except:
        raise SystemExit('An error has occurred. Could not download images.')

run()