#overriding and overloading
#same name but same number of parameter
class A:
    def disp(self):
        print("class A")
class B(A):
    def disp(self):
        print("class B")
class C(B):
    def disp(self):
        print("class C")
z=C()
z.disp()
z.disp()
z.disp()

#Using super() in Overriding
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()

#another example for overriding
class Animal:
    def sound(self):
        print("different animals make different sounds")
class Cat(Animal):
    def sound(self):
        print("The cat says meow")
z=Cat()
z.sound()
z.sound()

#same name but diff number of parameter(python not support overloading)
class A:
    def dis(self,a,b,c):
        print(a)
        print(b)
        print(c)
class B(A):
    def dis(self,a,b):
        print(a)
        print(b)
class C(B):
    def dis(self,a):
        print(a)

x=C()
x.dis(10)
x.dis(10,20)
x.dis(10,20,30)
