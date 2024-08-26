
euser=["naveen","hari","prasana"]
epass='hduser'
att=0 
maxatt=4
username=input("enter the username")

while True:
    if euser.count(username)==1:
        print("user present")
        pas=input("enter the pass")
        if epass==pas:
            print("login sucess")
            break
        else:
            print("incorrect password")
            att+=1 
            if att >= maxatt:
                print("max attempts reached exiting")
                break
    else:
        print("user not present")
        break