'''amt=1000
max_offer=100
pct=.10
offer_amt=amt*pct
if (max_offer<offer_amt) or (max_offer==offer_amt):
    print("giving offer of ",max_offer)
    addon_offer_amt=-50
    additional_cashback=amt+addon_offer_amt if amt>100 else amt
    print("amount to pay is",additional_cashback-max_offer)
else:
    print("giving offer of ",offer_amt)
    print("amount to pay is",amt-offer_amt) '''

def swiggy(amt):
    maxx=100
    off=amt*.10
    try:
        if amt>=500:
            if (maxx<=off):
                print("Giving offer of",round(maxx))
                add=100
                cb=amt-add if amt>2000 else amt
                print("giving addition cashback of 100 for those who purchased above 2000")
                final=cb-maxx
                print(f"Amount to pay is {round(final)}")
                return round(final)
            else:
                print("Giving offer of",round(off))
                final=amt-off
                print("amount to pay is",round(final))
                return round(final)
        else:
            raise ValueError("Minimium amount required is 500")
    except ValueError as err:
            print("value is less:",err)

ip=int(input("enter ur amount"))        
swiggy(ip)


    