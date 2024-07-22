#password verifier
'''mr X IS TRYING TO  create a new password for his instagram acc this are the required conditions for creating a new password
 condition 1:- minimum length is 8 and max length is 15
   condition 2:- only @,/ is allowed in a password must 
    condition 3:- no spaces are allowed
       condition 4:- only alphanumerics are allowed
you are  supposed to print weak if length is exact 8 ,medium length is between 8 to 12 ,strong if length is between 12 to 15   '''

string=input()
p=len(string)
r="@"
s="/"
if p>=8 and p<=15:
    if r or s in string:
        if " " not in string:
            if p==8:
                print("weak")
            elif p>8 and p<=12:
                print("medium")
            elif p>12 and p<=15:
                print("strong")
    else:
        print("check the conditions")
    
else:
    print("please check the conditions")





    
         

