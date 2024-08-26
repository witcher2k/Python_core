'''factoria 5!=5x4x3x2x1 '''

def fac(n):
    if n==0 or n==1:
        return n 
    else:
        return n*fac(n-1) 
    
print(fac(5))
    