# num=int(input())
# if num%400==0 or (num%4==0 and num%100!=0):
#     print("year is leap")
# else:
#     print("year is not a leap year")

# print year in range

a,b = map(int,input().split())
for i in range(a,b+1):

        if i%400==0 or (i%4==0 and i%100!=0):
            print(i)