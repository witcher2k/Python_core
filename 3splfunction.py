
def allc(sal,bon,inc):
    return sal+bon+inc #higherorder 1

def calsal(sal,def1):
    bon=2000 #closure
    def sall():
        inc=1000
        return def1(sal,bon,inc)
    return sall #higherorder 2
    
print(calsal(10000, allc)())  
