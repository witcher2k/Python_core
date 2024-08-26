pop=input("please give click")
opt1="upcomingbatch"
opt2="askanything"
if  pop=="click":
    print("select one of these ")
    opt=input(f"select the page from 1.{opt1} or 2.{opt2}")
    if opt=="1":
        print(f"u selected {opt1}")
        tech=input("select the tech from this options devops or data")
        if tech=="devops":
            print("upcoming batch is tmrw")
        elif tech=="data":
            print("next batch is next month")
        else:
            print(f"the course u selected '{tech}' not available")
    elif opt=="2":
        print(f"u selected {opt2}")
        contact=input("give ur phone or email to contact")
        if contact.isdigit():
            print(f"thanks for the number {contact}")
        elif '@' in contact and '.' in contact:
            print(f"thanks for ur mail {contact}")
        
    else:
        print("the option u selected not available ")
else:
    print("varata maame")
                    
        
            
       