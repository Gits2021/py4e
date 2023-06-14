#Example exercise 
import xml.etree.ElementTree as ET
import json 
import ssl 
import urllib
import urllib.parse
import urllib.error 
import urllib.request


  #Exercise 1
def googlenav():  # sourcery skip: do-not-use-bare-except, merge-dict-assign, simplify-boolean-comparison
    api_key = False
    
    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else:
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
    # SSL Certificate Check 
    ct = ssl.create_default_context()
    ct.check_hostname = False
    ct.verify_mode = ssl.CERT_NONE
    while True: 
        address = input('Enter location ')
        if len(address) < 1:
            print('Goodbye')
            break
        params = {}
        params['address'] = address 
        if api_key is not False: params['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(params)
        print('searching ', url)
        gps = urllib.request.urlopen(url, context=ct)
        pos = gps.read().decode()
        print('Found ', len(pos), 'characters')
        try:
            js = json.loads(pos)
        except:
            js = None 
        

        if not js or 'status' not in js or js['status'] != 'OK':
            print('JSON failed to load')
            print(pos) 
            continue 
        print(json.dumps(js, indent=4))

        lat = js['results'][0]['geometry']['location']['lat']
        lng = js['results'][0]['geometry']['location']['lng']
        country = js['results'][0]['address_components'][3]['short_name']
        location = js['results'][0]['formatted_address'] 
        place_id = js['results'][0]['place_id']
        print(location) 
        print(country) 
        print(place_id)
        
googlenav()

def sum_of_all():
# Ignore SSL certificate errors
 ctx = ssl.create_default_context()
 ctx.check_hostname = False
 ctx.verify_mode = ssl.CERT_NONE 
# Create holder 
 total = 0
 while True:
    url = input('Enter url for data: ')
    if len(url) < 1:
        break 
    file = urllib.request.urlopen(url, context=ctx) 
    data = file.read()
    print('retrieved: ', len(data), 'characters')
    data.decode()
    tree = ET.fromstring(data)
    comment = tree.findall('.//count') 
    for item in range(len(comment)):
       t = int(comment[item].text)
       total += t 
    print(total)
sum_of_all()