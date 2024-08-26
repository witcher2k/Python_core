val1=int(input("enter the number1"))
val2=int(input("enter the number2"))
password='hduser'
while val1<=val2:
    enteredpassword=input("enter the password")
    if enteredpassword==password:
        print("login sucessfull")
    else:
        val1+=1