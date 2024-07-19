#declaration of list
#l=[1,2,3,4]
# print(*l,end="@\n")
# #l.append(9999)
# #print(*l)
# l.insert(0,9999)
# print(*l)
# l.insert(888,999)
# print(*l)
# print(len(l))
#l.pop()
#print(*l)
# l.pop(2)
# print(*l)
# l.pop(77)
# print(*l)  #index out of range
# l2=[5,6,7,8]
# print(*(l+l2)) #concatination
# new_l=l.copy()
# new_l.pop()  #it will default pop the last element
# print(*new_l)
# l3=[1,2,3,4,2,4,4,5,4]
# print(l3.count(4))
# l4=[1,-2,8,-6,9,5,4,0,-10,-4]
# l4.sort() 
'''in background it uses quick sort i.e time complexity is nlogn which is not good
so there are different methods whch takes n complexity  '''
#print(*l4) #ascending method
#list as a dynamic

# print(*l7)
# print(*l8)
# print(l6.count(4))l6=list(map(str,input().split("@"))) 
# # l7=list(map(int,input().split(","))) 
# # l8=list(map(int,input().split()))  #input().split(",")--> default  space separator
# # #int---> int type
# # #map--->to print many elements
# # #list---->list type
# # print(*l6)
# print(l6.append(67))





'''aggregate functions '''
#print(sum(l))take list from the user if user enters 1 append if user 2 pop 3 sort 4 concatatinon,good morning len

list=list(map(int,input().split()))
print('''select any choice :-
       1.append
       2.pop
       3.sort
       4.concatenation''')
choice=int(input())
if(choice==1):
    list.append(99)
    print(*list)
elif(choice==2):
    list.pop()
    print(*list)
elif(choice==3):
     list.sort()
     print(*list)
else:
    print(f"hello ,good morning length of list is {len(list)}")






