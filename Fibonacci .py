def fib(i):
    if i==0:
        return 0
    elif i==1:
        return 1 
    else:
        return fib(i-1)+fib(i-2)

lst=[]
for i in range(0,6):
    lst.append(fib(i))
print(lst)
