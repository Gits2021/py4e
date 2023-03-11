inp = input('How many hours did you work this week?')
hours = int(inp)
overtime = hours - 40 
rate = 10 
overRate = rate * 1.5 
if hours <= 40: 
    pay = hours * rate 
    print("Your paycheck is: ")
    print(pay)
else: 
    regPay = rate * 40 
    overPay = overtime * overRate 
    grossPay = regPay + overPay 
    print('Your paycheck is: ')
    print(grossPay)
# Exercise 2
hours_worked = input('How nany hours did you work this week?')
rate_of_pay = input('What is your rate per hour?')
try: 
    workDay = int(hours_worked)
    salary = int(rate_of_pay)
    shiftDiff = workDay - 40
    shiftSalary = salary * 1.5
    if workDay <= 40:
        biWeekly = workDay * salary
        print('Your paycheck is: ')
        print(biWeekly)
    else: 
        biPay = salary * 40 
        shiftOver = shiftDiff * shiftSalary
        biOver = biPay + shiftOver
        print('Your paycheck is: ')
        print(biOver)
except: 
    print('please enter a number!') 
#Exercise 3 
grade = input('Please enter a score between 0.0 and 1.0\n')
try: 
    score = float(grade)  
    if score < 0.0 or score > 1.0: 
        print('Invalid score!')
    elif score >= 0.9:
       print('A')
    elif score >= 0.8: 
        print('B')
    elif score >= 0.7: 
        print('C')
    elif score >= 0.6: 
        print('D') 
    elif score < 0.6: 
        print('F') 
except: 
       print('Invalid score!')
   
