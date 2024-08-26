opt=input(f"select the page from '1.upcoming sessions' or '2.ask anything'")
if opt=="1":
    print("u selected upcoming sessions")
    tech=input("select the tech from this options devops or data")
    if tech=="devops":
        print("upcoming batch is tmrw")
    elif tech=="data":
        print("next batch is next month")
    else:
        print(f"the course u selected '{tech}' not available")
elif opt=="2":
    print("u selected ask anything")
    contact=input("give ur phone or email to contact")
    if contact.isdigit():
        print(f"thanks for the number {contact}")
    elif '@' in contact and '.' in contact:
        print(f"thanks for ur mail {contact}")
        
else:
    print("the option u selected not available ")