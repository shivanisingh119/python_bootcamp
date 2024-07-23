'''remove all the brackets from the given algebraic expression'''

s=input()
r={"]","[","(",")","{","}"}
for i in s:
    if i not in r:
    
       print(i,end="")


       #ascii of } ==125
                #    {==123
                #  [==91
                # ]==93
                # (==40
                # )==41

#pass method

inp=input()
for i in inp:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end="")
    print()