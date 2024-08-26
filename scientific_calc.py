def add(a,b):
    return a+b 
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b 
    
def div(a,b):
    if b==0:
        return "Zero division"
    else:
        return a/b 
        
def calc(a,b,arg,mode):
    if mode=='a':
        if arg==add:
            result=arg(a,b)
            return result
        elif arg==sub:
            result=arg(a,b)
            return result
        elif arg==div:
            result=arg(a,b)
            return result
        else:
            result=arg(a,b)
            return result
    else:
        if arg=='sin':
            import math
            def sin(a):
                rad=math.radians(a)
                return math.sin(rad)
            print(sin(a))
            return sin
        elif arg=='cos':
            import math
            def cos(a):
                rad=math.radians(a)
                return math.cos(rad)
            print(cos(a))
            return cos
        elif arg=='tan':
            import math
            def tan(a):
                rad=math.radians(a)
                return math.tan(rad)
            print(tan(a))
            return tan

tann=calc(60,4,'tan','b')
print(tann)
result=tann(70)
print(result)

