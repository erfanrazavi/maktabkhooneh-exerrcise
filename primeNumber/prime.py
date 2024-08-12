num = int(input('Enter yor number: '))

if num > 1:
    for i in range(2,int((num**0.5)) + 1):
        if i % 2 == 0:
            print('not prime')
            break
        else:
            print('prime')
            
#-------------------------------------------> or =>

num = int(input('Enter yor number: '))

if num > 1:
    for i in range(2,(num//2) + 1):
        if i % 2 == 0:
            print('not prime')
            break
        else:
            print('prime')