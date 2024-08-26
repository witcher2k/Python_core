def days(wd):
    c=31-wd
    return c 

def sal(spd,wd):
    nonwork=days(wd)
    d=spd*nonwork 
    return (spd*31)-d 
    
print(days(20))
print(sal(1000,20))