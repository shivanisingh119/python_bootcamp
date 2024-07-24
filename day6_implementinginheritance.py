'''implementing inheritance'''
#single level inheritance
# class Animal:
#       def Speak():
#             return "animal is speaking"
      


# class Dog(Animal):
#       def bark():
#             return "bow..!!"
# obj1=Animal
# obj2=Dog
# print(obj2.Speak())
# print(obj2.bark())


#multilevel inheritance

class Animal:
      def Speak():
            return "animal is speaking"
      
      
      

class Dog(Animal):
      def Bark():
            return "bow..!!"
class puppy(Dog):
      def puppy_speak():
            return "i'm puppy"
obj1=Animal
obj2=Dog
obj3=puppy
print(obj2.Speak())
print(obj2.bark())
print(obj3.Speak())
print(obj3.bark())

print(obj3.puppy_speak())




#multiple inheritance:-
# class Father:
#       def father_speak():
#             return "father class"
# class Mother:
#       def mother_speak():
#             return "mother class"
# class kid(Father,Mother):
#       def kid_speak():
#             return "i'm kid. i am having properties of both"
# obj1=kid
# print(obj1.father_speak())
# print(obj1.mother_speak())
# print(obj1.kid_speak())





#heirarchial inheritance







      


