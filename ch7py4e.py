fhand = open('mbox-short.txt')
print(fhand) 
for line in fhand: 
    str = line.upper()
    print(str)
#Exercise 2 
total = 0 
count = 0
fsesame = input("Please enter the file name:\n")
try: 
    fhandle = open(fsesame)  
except: 
    print('File cannot be opened.', fsesame)
    exit()
for line in fhandle: 
    if line.startswith('X-DSPAM-Confidence'):
        fcolon = line.find(':')
        strcon = line[fcolon + 1:]
        confidence = float(strcon)
        count = count + 1
        total = total + confidence 

print("This is the total of all spam confidence emails:\n", total)
print("This is how many lines were marked with a  measurable spam confidence:\n", count)
print("This is the average spam confidence for the given file:\n", total/count)  


