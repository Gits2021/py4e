#Exercise 3 
punked_message = 'NA NA BOO BOO TO YOU - you have been punked'
file_name = input('Please enter a file name:\n')  
if file_name == 'na na boo boo':
    print(punked_message)
    exit()
try:
    open_file = open(file_name)
except:
   print('File cannot be opened, ', file_name) 
subject_count = 0
for line in open_file:
    if line.startswith('Subject:'):
        subject_count = subject_count + 1
print('There were', subject_count, 'subject lines in: ', file_name)