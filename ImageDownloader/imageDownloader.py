#!/usr/bin/python3

"""imageDownloader.py: Downloads all the images from a web page."""

__author__ = 'andrei.muntean.dev@gmail.com (Andrei Muntean)'

import os.path
import sys
from urllib.request import urlopen, urlretrieve

def get_input_url():
    if len(sys.argv) == 3:
        return sys.argv[1]
    else:
        print('Please specify a URL.')
    
        return input('> ')

def get_input_destination():
    if len(sys.argv) == 3:
        return sys.argv[2]
    else:
        print('Where would you like to download the images?')
    
        return input('> ')

def get_img_urls(html):
    """Returns a list that contains every image URL from the specified HTML string."""
    
    return []

def download(img_urls, destination):
    """Downloads the images from the given URLs into the specified destination."""
    
    if not os.path.exists(destination):
        os.makedirs(destination)

    for img_url in img_urls:
        urlretrieve(img_url, destination + '/' + img_url)

def run():
    """Runs the program."""

    url = get_input_url()
    destination = get_input_destination()

    try:
        response = urlopen(url, timeout=5)
        html = response.read()
        download(get_img_urls(html), destination)
    except:
        print('An error has occurred. Could not download images.')

run()