#method_over_riding-----run time

# class Animal:
#     def Speak():
#         return "Speaking...."
# class Dog(Animal):
#     def Speak():
#         return "Dog is speaking"
# class puppy(Dog):
#     def Speak():
#         return "puppy is speaking"
    
# obj1=puppy
# print(obj1.Speak())



#method over loading:-the most effient mwthod to achieve method overloading is variablea length arguments----compile time


class cal:
    def add(self,*args):
        # return sum(args)
       sum=0
       for i in args:
           sum+=i
       return sum
    
obj1=cal()   #if dynamic we need to keep brackets but in statics it is not required
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))


 
