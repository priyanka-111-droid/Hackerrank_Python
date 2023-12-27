cube = lambda x: pow(x,3)# complete the lambda function 
def fibonacci(n):
    # return a list of fibonacci numbers
    fib=[]
    a=0
    b=1
    fib.append(a)
    fib.append(b)
    if(n==0):
        return []
    if(n==1):
        return [a]
    elif(n==2):
        return [a,b]
    else:
        while n!=2:
            c=a+b
            fib.append(c)
            a=b
            b=c
            n-=1
            
    return (fib)
    
        
        