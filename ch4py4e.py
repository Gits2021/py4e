#Exercise 1 
import random

for i in range(10):
    x = random.random()
    print(x) 


#Exercise 2/3

def repeat_lyrics(): 
        print_lyrics()
        print_lyrics() 
    
def print_lyrics():
    print("Yelling at the sky")
    print('Screaming at the world')
    print("Baby why'd you go away?")
    print("I'm still your girl")


print_lyrics() 
repeat_lyrics()
#Exercise 4
# B, C 
#Exercise 5
# D 
def fluff(): 
     print('woof') 

def ruff(): 
     print('squeak') 

ruff()
fluff()
ruff() 
#Exercise 6 
hours_q = input('How many hours do you work per week?')
rate_q = input('How much do you make per hour?/n') 
def addTwo(a, b): 
     added = 5 + 8
     return added

def computePay(hours_q, rate_q):  
     pay = 0 
     hours = int(hours_q)
     rate  = int(rate_q) 
     if hours <=40: 
         pay = hours * rate 
         return pay 
     else:  
          overtime = hours - 40
          payover = overtime * (rate * 1.5) 
          regPay = hours * rate 
          pay = regPay + payover 
          return pay 
#Testing 
biWeekly = computePay(hours_q,rate_q)
print(biWeekly)
#Exercise 7
grade = input('Please enter a grade between 0.0 and 1.0/n')
def computeGrade(grade):
     score = float(grade)
     if score < 0.0 or score > 1.0: 
          print('Invalid score')
     elif score >= 0.9: 
          print("A") 
     elif score >= 0.8: 
          print("B")
     elif score >= 0.7: 
          print("C")
     elif score > 0.6: 
         print('D')
     elif score < 0.6: 
          print('F') 


computeGrade(grade)