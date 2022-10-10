
def Fibonacci():
    i = 0
    n = 1
    sum = 0
    conta = 0
    while(conta<10):    
        print(sum)
        i=n
        n=sum
        sum=i+n
        conta+=1
print(Fibonacci())
