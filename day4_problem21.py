   #
'''lcm and gcd/hcf'''

  #GCD OF GIVEN 2 NUMBERS

  #USING EUCLIDIAN ALGORITHMS

# a,b=map(int,input().split())      #5 15   
# while b!=0:                       #15!=0      #5!=0
#     a,b=b,a%b                     #15 5     #5 0
# print(a)                 #5           mod is used to reduce the number size



#LCM

a,b=map(int,input().split())
c,d=a,b
while b!=0:
     a,b=b,a%b
gcd=a       
print((c*d)//gcd)

#lcm*gcd =a*b

