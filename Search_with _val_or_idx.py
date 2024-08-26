lstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"]]

#idx to value
def idd(lst,*args):
    try:
        value=lst
        for i in args:
            value=value[i]
        return value
    except (ValueError,IndexError) as err:
        return None
        
print(idd(lstlst,0,1,1))

#value to idx
def val(lst,value):
    for i,item in enumerate(lst):
        if isinstance(item,list) or isinstance(item,tuple):
            for j,sitem in enumerate(item):
                if sitem==value:
                    return(i,j)
                elif isinstance(sitem,(list,tuple)) and value in sitem:
                    return (i,j,sitem.index(value))
    return -1
    
print(val(lstlst,"Bala"))

                
    