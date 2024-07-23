'''*****
*****
*****
*****
# *****/
'''
n=int(input())
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()



# '''*
#    * *
#    * * *
#    * * * *'''

# n=int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()



'''* * * *
       * * *
       * *
       *'''
    

for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()


'''   *
    *  *   *
*   *  *   *  *'''
# for i in range

n=int(input())
for i in range(n):
    for j in range(n):
        if(i==j):
            print(" ",end=" ")
        else:
          print("*",end=" ")
    print()




    '''homework
    1.print upper trianglular matrix
    2.print lower triangular ,atrix
    3.print rhombus 
    4.print  ***
              ***
               ***
    5.print number pyramid'''
    
    '''3   *
         * * *
       * * * * *
         * * * 
           *  '''