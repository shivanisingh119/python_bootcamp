'''and,or
'''
# age=int(input())
# if (age>18 and age<24):
#     print("allow to drive two wheeler")
# elif(age >=24 and age <45):
#     print("two and four wheeler")
# elif(age>=45):
#     print("all")
'''person x goes to market he will buy 10 apples and two dozen bananas and next he will buy 8 oranges
and next the cost of each apple is 15 rupees and cost of 1 banna is 4 rupees and cost of orange is 5
mother of x i.e y gave 700 rupees to mr x and says some amount will be left with you  '''
# cost_apples=15
# cost_bananas=4
# cost_oranges=5
# apples=int(input())
# bananas =int(input())
# oranges=int(input())

# total=(cost_apples*apples + cost_bananas*bananas + cost_oranges*oranges)
# print(total)
# if(total < 700):
#     print("shopkeeper is not cheater")
# else:
#     print("the shopkeeper is cheater")
#take a input fron user check if it is positive and even print .......if it 
# 

'''  mr z is selected for olympics is participated in swimming competition only 1 winner is selected 
among 100 of participants anyhow he got selected ...mr x and mr y are friends of z .mr x is participating 
in badminton and mr y in participating in table tennis .according to the selection committee the requirements 
for badminton players are 140 cm height and weight factors of 2 .bodyfat is less than 12% ......
acording to the selection committee requiremmnets for table tennis are height mimimum 118cm to 148cm ,
weight of numbers of medals got by mr  z,bodyfat 14%...according to the previous history z participated
in 14 games out of which having success rate of 50% .
 write a program whether mr x mr y and mr z from
india will travel in same plane or not  or write a program whether that three person will meet in olympic or not'''
height_of_x=int(input())
height_of_y=int(input()) 
weight_of_x=int(input())
weight_of_y=int(input())
x_selected=0 
y_selected=0
if (height_of_x ==140 and weight_of_x%2==0):
    x_selected+=1
    
if((height_of_y<148 and height_of_y>118) and weight_of_y%7==0):
    y_selected+=1
    
if(y_selected==1 and x_selected ==1):
    print("x,y and z will meet in airplane")
else:
    print("not meet")



    