#Exercise 1 
# Whrite a function called chop that removes the beginning and end of a list and returns None 

def chop(t):
    del t[1:-1]


numbers = [0,1, 2, 3, 4, 5, 6]
truncated = chop(numbers)
print(truncated) 

def middle(z):
    return z[1:-1] 

letters = ['a', 'b', 'c', 'd', 'e', 'f']
meet = middle(letters)
print(meet)
#Exercise 2
fhandled = open('mbox-short.txt')
count = 0
for line in fhandled: 
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    count = count + 1
print(count) 

#Exercise 4 
def romeo():
 empty = []
 i = 0
 file_name = input('Enter file: ')
 f_open = open(file_name, 'r')
 for line in f_open: 
    line.rstrip()
    for word in line.split(' '):
        if word not in empty:
            empty.append(word)

 full = empty[:] 
 print(sorted(full)) 

#Exercise 5
def who_from():
 handlef = open('mbox-short.txt')
 count = 0
 for line in handlef:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    print(words[2])
    count = count + 1
print('Words that start with "From"', count) 

#who_from() 


numlist = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break

    val = float(inp)
    
    numlist.append(val) 
    least = min(numlist)
    greatest = max(numlist) 
print(least)
print(greatest) 

  