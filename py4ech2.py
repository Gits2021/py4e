name = input('What is your name?\n')
print("Hello, " + name)
#Exercise 2 
hours = input("How many hours did you work this week?")
rate = input("How much do you make per hour?")
pay = int(hours) * int(rate)
print("This is your gross pay: " + str(pay))
#Exercise 3 
width = 17 
height = 12.0 
print(width // 2)
print(width / 2.0)
print(height / 3)
print(1 + 2 * 5) 
# Exercise 4 
temperature = input("What is the current temperature in degrees Farenhiet?")
conversion = ((int(temperature) - 32) * (5/9 ))
print("Here is the temperaature in degrees Celcius:")
print(conversion)