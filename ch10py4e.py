#Exercise 1
import re


def websters_main():  # sourcery skip: for-append-to-extend, list-comprehension
    dom = {}
    file = input('File Name: ')
    try:
        handle = open(file)
    except Exception:
        print(f'File, {file}is unable to be opened')
        exit()
    for line in handle:
         text = line.split()
         if len(text) == 0: continue
         if text[0] != 'From': continue
         address = text[1]
         dom[address] = dom.get(address, 0) + 1
    print(dom)
    lst = []
    for key, val in list(dom.items()):
        lst.append((val,key)) 
    lst.sort(reverse=True)
    for key, val in lst[:1]:
        print(val, key)

    
    
websters_main() 

#Exercise 2 
def timeOfDay():
    tod = {}
    file = input('Please enter the file name:')
    try:
        handle = open(file)
    except Exception:
        print(f'File, {file}, is unable to be opened')
        exit()
    for line in handle:
        words = line.split()
        if len(words) == 0: continue
        if words[0] != 'From': continue
        timestamp = words[5] 
        splits = timestamp.split(':')
        hours = splits[0] 
        tod[hours] = tod.get(hours, 0) + 1
    blank_list = sorted(list(tod.items()))
    for key, val in blank_list:
        print(key, val)


timeOfDay()

#Exercise 3
def count_chars():  # sourcery skip: avoid-builtin-shadow
    char = {} 
    empty_list = []
    file = input('File name: ')

    handle = open(file)
    str = handle.read()
    string = ''.join(re.findall(r'[a-zA-Z]+', str))
    string = string.lower()
    for ch in string: 
        char[ch] = char.get(ch, 0) + 1

    print(char) 

    for key, val in list(char.items()):
        empty_list.append((val, key))
    
    empty_list.sort(reverse=True) 
    for key, val in empty_list:
        print(key,val)
  
        

count_chars()