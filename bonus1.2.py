def divisor(n):
    array=[]
    for i in range (2,n-1):
        if n%i==0:
            array.append(i)
    if len(array)>0:
        return ' the divisors of number ',n,' in the reverse order are ',array[::-1]
    else:
        return n," is a prime number "
n = eval(input(' enter the number you want to test: '))
c=0
while c<3 and n<=1:
    n = eval(input(' please enter a positive number  '))
    c+=1
if n>1:
    print(divisor(n))
else :
    print('Wrong number, ya bro')