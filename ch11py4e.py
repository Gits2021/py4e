#Using regular expressions requires import re 
import re 
def simpleSearch():
    handle = open('mbox-short.txt')
    for line in handle:
        line = line.rstrip()
        if re.search('^From:', line):
            print(line) 

#simpleSearch() 

def simpleSearch_a():
    handle = open('mbox-short.txt')
    for line in handle:
        line = line.rstrip()
        if re.search('^F..m:', line):
            print('a ' ,line) 

#simpleSearch_a() 

def grep_clone(): 
    #the grep command can be used in linux to search for files 
    file = input('File name: ')
    try: 
        handle = open(file)
        string = handle.read() 
    except Exception: 
        print('File cannot be opened')
        exit() 
    
    search = input('Enter the string or digit that you want to search for: ') 
    pat = re.compile(search)
    num = re.findall(pat, string) 
    print(num)
    total = 0
    for digit in range(len(num)):
        cast = float(num[digit])
        total += cast
    print(total)
grep_clone()