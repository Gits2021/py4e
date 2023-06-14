import xml.etree.ElementTree as ET
import json 
import ssl 
import urllib
import urllib.parse
import urllib.error 
import urllib.request



data ='''<person>
          <name>Chuck</name>
           <phone type="intl">
             +1 734 303 4456 
             </phone>
             <email hide="yes"/>
</person>''' 
tree = ET.fromstring(data)
print('name ',tree.find('name').text )
print('attr ', tree.find('email').get('hide')) 

#Example 2 
input = '''<stuff>
            <users>
            <user x="2">
            <id>001</id>
             <name>Chuck</name>
             </user>
             <user x="7">
            <id>009</id>
             <name>Brent</name>
             </user>
            </users>
 </stuff>'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('attribs: ', item.get("x"))

    #Example 3
datac = '''[
{
 "id" : "001",
  "x" : "2", 
  "name" : "Chuck"
}, 
{
 "id" : "009",
 "x" : "7", 
 "name" : "Brent"
}
]''' 

info = json.loads(datac)
print('User count, ', len(info))
for item in info:
    print('Name ', item['name'])
    print('Id ', item['id'])
    print('attribute ', item['x']) 