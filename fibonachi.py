n=int(input('Enter number:'))
x=[]
def fib(i):
    if i==0:
        return 0
    if i==1:
        return 1
    else:
        return fib(i-1)+fib(i-2)   
for i in range(n):
    fib(i)
    x.append(fib(i))
print(x)             


