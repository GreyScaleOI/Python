email=input("Enter your Email :") #g@g.in , wscube@gmail.com
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".")^(email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1


                if k==1 or j==1 or d==1:
                    print("email contains blank space")
                else:
                    print("Authenticated")
            else : ("email doesn't contain a '.'")
        else:
            print("no domain address provided")
    else:
        print('''address doesn't start with an alphabet''')
else:
    print("constraint not satisfied")
