'''ABC, 4 STEPSIZE=4 .
OUTPUT:=EFG

TESTCASE2:-
XYZ STEPSIZE 4
BCD
'''
# try this homework using encoding and decoding

s=input()
p=s.upper()
for i in p:
    print(chr(ord(i)+4),end="")
print()

'''xyz
x=120+4=124-----> D=98
y=121+4=125------> C=99
z=122+4=126------> B=100'''

    



