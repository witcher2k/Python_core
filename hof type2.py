
def met(mett):
    if mett=='m1':
        def met1(a,b):
            return a+b
        return met1
    elif mett=='m2':
        def met2(a,b):
            return a-b
        return met2
        
 
print(met('m1')(5,2))

'''
var = met('m2')  # met2 function is returned and stored in var
print(var(5, 2))'''  # Directly call var(5, 2) and print the result

        
    
