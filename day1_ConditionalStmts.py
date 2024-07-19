'''we will see different conditions:they are 
if,elif,else'''
#write a code for driving licence aligibilty
# age=int(input())
# if age>18:
#     print("eligible")
# else:
#     print("not eligible")
#     #take a name from user check whether he is eligible for voting or not

name=input()
age=int(input())
if age>18:
    print(f"{name} is eligible for voting beacuse her age is {age}")
else:
    print(f"{name} is  not eligible for voting beacuse her age is {age}")
