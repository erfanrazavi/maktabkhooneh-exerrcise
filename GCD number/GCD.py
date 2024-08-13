#function ------------>

def gcd(a , b):
    if b == 0:
        return a
    else:
        a = num
        b = num2
        if num2 > num:  #This condition is for when the user enters the number in reverse
            count = 3
            list = []
            while  count >= 0:
                c = b % a
                b = a
                a = c
                count -= 1
                list.append(c)
        else:
            count = 3
            list = []
            while  count >= 0:
                c = a % b
                a = b
                b = c
                count -= 1
                list.append(c)
            
        return f'Result(GCD) = {list[-2]}'  


#input ----------->


num = int(input('number1: '))
num2 = int(input('number2: '))


    
    
print(gcd(num , num2))
