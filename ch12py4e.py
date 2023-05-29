import socket, re, urllib, urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup 
import ssl

def connect_now():  # sourcery skip: use-fstring-for-concatenation
    url = input('Enter url: ')
    host = url.split('/')[2]
    tsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tsocket.connect((host, 80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    tsocket.send(cmd) 
    while True:
        data = tsocket.recv(512)
        if len(data) < 1:
            break 
        print(data.decode(), end='') 
    tsocket.close()
#connect_now() 


def show_3000():
    counts = dict()
    strong = ''
    url = input('Enter url: ')
    host = url.split('/')[2]
    tsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tsocket.connect((host, 80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    tsocket.send(cmd)
    while True:
        data = tsocket.recv(20)
        if len(data) < 1:
            break
        strong += data.decode()
        for char in strong:
            counts[char] = counts.get(char, 0) + 1
    print('Number of characters: ', len(strong))
    print(strong[:3000])
    #Note this the last 3000 characters, I wanted to spice it up
    print(counts)

    tsocket.close()

#show_3000() 

def uniform_resources():
    try: 
        count = {}
        file = input('Please enter a valid url: ')
        handle = urllib.request.urlopen(f'{file}').read()
        text = handle.decode().strip()
        for line in text:
            count[line] = count.get(line, 0) + 1

        print(text[:3000])
        print('The number of characters is:', len(text))
        print('Character frequency: ', count)
    except Exception:
        print('No valid url entered')

#uniform_resources() 

import ssl
import urllib.request
from bs4 import BeautifulSoup

def tacky_tracker():
    total = 0
    
    # Ignore SSL errors
    ct = ssl.create_default_context()
    ct.check_hostname = False
    ct.verify_mode = ssl.CERT_NONE
    
    # Get URL from user input
    url = input('Enter URL: ')
    
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    
    handle = urllib.request.urlopen(req, context=ct).read()
    bsoup = BeautifulSoup(handle, 'html.parser')
    
    # Retrieve span tags from the HTML
    anchors = bsoup.find_all('span')
    
    for anchor in anchors:
        # Extract the string content from the span tag
        strnum = anchor.contents[0]
        
        # Convert the string to an integer
        teger = int(strnum)
        
        # Add the integer to the total
        total += teger
        print(teger)

    print('Span total:', total)

tacky_tracker()

def names_inna_list():
       # Ignore SSL errors
    ct = ssl.create_default_context()
    ct.check_hostname = False
    ct.verify_mode = ssl.CERT_NONE

    # Get URL from user input 
    count = int(input('Count '))
    pos = int(input('Position '))
    url = input('Enter URL: ')

    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    handle = urllib.request.urlopen(req, context=ct).read()
    bsoup = BeautifulSoup(handle, 'html.parser')
    #anchors = bsoup('a')
    ps = 0
    cn = 0 
    while count > 0:
      file = urllib.request.urlopen(url, context=ct).read()
      soup = BeautifulSoup(file,'html.parser')
      anchors = soup('a')
      for a in anchors:
        ps += 1
        if ps == pos:
            print('Crawled to: ', a.get('href', None), a.contents[0])
            url = str(a.get('href', None))
            ps = 0
            break 
      count -= 1

 
names_inna_list()