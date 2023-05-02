import string 
import operator

eng2sp = {}

print(eng2sp)
eng2sp['one'] = 'uno'
print(eng2sp)
eng2sp = {'one': 'uno', 'two':'dos', 'three':'tres'}
print(eng2sp)
print(eng2sp['three'])
#Exercise 1 
wordlist = {}
fname = input('Please enter a file name: ')
try: 
    fhandle = open(fname)
except Exception:
    print('File not found')
    exit()

for line in fhandle:
    words = line.split()
    for word in words: 
        wordlist[word] = 1 if word not in wordlist else wordlist[word] + 1
print(wordlist) 

text = 'tyrannosurus rex'
d = {}
for t in text: 
    if t not in d:
     d[t] = d.get(t, 0) + 1
    else:
        d[t] = d[t] + 1 
print(d)

names = {'chuck': 1, 'annie' : 42, 'jan': 100}
print(names.get('chuck', 0))
print(names.get('Mary', 0)) 
for key in names: 
    print(key, names[key])

fname = input('Please enter a file name: ')
try: 
   fhandle =  open(fname)
except Exception: 
    print('File not found!', fname)
    exit() 

counts = {}
for line in fhandle: 
    line =  line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split() 
    for word in words: 
        counts[word] = counts.get(word, 0) + 1 

print(counts) 

def day_of_week():
    dow = {} 
    fname = input('Please enter a file name: ',)
    try: 
        fhand = open(fname)
    except Exception:
        print('File not found!', fname)
        exit() 
    for line in fhand: 
        words = line.split()
        if len(words) == 0: continue
        if words[0] != 'From': continue
        dow[words[2]] = dow.get(words[2], 0) + 1
    print(dow)

day_of_week() 

def new_phone_who_dis():  # sourcery skip: do-not-use-bare-except
 sent = {}
 try: 
  file_name = input('Please enter the file name: ')
  file_handler = open(file_name)
 except:
  print('File could not be opened', file_name)
  exit()  
 for line in file_handler:
    text = line.split()
    if len(text) == 0: continue
    if text[0] != 'From': continue
    sent[text[1]] = sent.get(text[1], 0) + 1

 print(sent) 
 #Exercise 5
 #Operater offers an iterable to use the max function and get the highest value 
 highest = max(sent.items(), key=operator.itemgetter(1))[0]
 print(highest)

new_phone_who_dis() 

def where_its_at():
   domain = {}
   files = input('Enter the file name: ')
   mail = open(files)
   for line in mail:
      dom = line.split()
      if len(dom) == 0: continue
      if dom[0] != 'From': continue
      email = dom[1] 
      institution = email.split('@')
      domain[institution[1]] = domain.get(institution[1], 0) + 1

   print(domain)

where_its_at()