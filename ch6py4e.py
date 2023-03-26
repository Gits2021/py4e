#Exercise 1 
fruit = 'mango'
length = len(fruit)
index = length - 1
while index >= 0: 
    letter = fruit[index]
    print(letter)
    index = index - 1
#Exercise 2 
char = fruit[:]
print(char) 
# Var[:] outputs the entire string because it's unbound 
#Exercise 3 
string = input('Enter the string you want to count\n')
char = input('Enter the letter you want to count in the string\n')
def count(string,char):
    count = 0 
    for letter in string: 
        if letter == char:
            count = count + 1
            print(count) 
count(string, char)
# Don't give the character in the for loop the same name as your parameter. 
#Exercise 4
line = 'Miss Mississippi'
total = line.count('s')
print(total) 
#Exercise 5
str = 'x-DSPAM-Confidence:0.8475'
poscol = str.find(':')
print(poscol)
confidence = str[poscol + 1:]
print(confidence)
prob = float(confidence)