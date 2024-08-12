import random

a  = 1
b = 99

a = 1
b = 99 


while a <= b:
        rand = random.randint(a,b)
        print(rand)    
        user = input('--->')
        
        if user == 'k':
            b = rand - 1  
            
        if user == 'b':
            a = rand + 1
            
        if user == 'd':
            print('hooora')
            break 
        
        else:
            print('Please enter correct number')
            
            

