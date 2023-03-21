#Exercise 1 
def enter_a_number(): 
    count = 0
    total = 0 
  
    while True: 
         line = input('Enter a number: ')
         if line == 'done': 
            break
         try: 
           val = float(line)
         except:  
           print('Invalid Input!')
           continue 
         total = total + val 
         count = count + 1 
    print('Count: ', count)
    print('Total: ', total)
    print('Average: ', total/count)     
    
    enter_a_number() 
  #Exercise 2 
def min_and_max(): 
   smallest = None
   largest = None
   while True: 
         line = input('Enter a number: ')
         if line == 'done': 
            break
         try: 
           val = float(line)
         except:  
           print('Invalid Input!') 
         if smallest is None or val < smallest: 
            smallest = val 
         
         if largest is None or val > largest: 
            largest = val 
           
   print("Smallest:", smallest)
   print('Largest:', largest)
        
min_and_max()
          
   