euser = ["naveen", "hari", "prasana"]
epass = 'hduser'
maxatt =int(input("enter the maximium attempts"))
att=0
user = input("Enter the username: ")

if user in euser:
    print("user present")
    for i in range(maxatt):
        pas=input("enter the password")
        if pas==epass:
            print("login success")
            break
        else:
            print("wrong password")
            if att==maxatt-1:
                print("max attempt reached")
else:
    print("user not present")