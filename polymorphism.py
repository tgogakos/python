#!/usr/bin/python
#polymorphism
class Animal():
     def talk(self):
         print("i have smth to say")

     def walk(self):
         print("hey i m walking")

     def clothes(self):
         print("i have clothes")

class Duck(Animal):
    def quack(self):
        print("i quack")

    def walk(self):
        super().walk()
        print("walk")

    def bark(self):
        print("the duck can tbark")

    def fur(self):
        print("only feathers")

            

class Dog(Animal):
    def fur(self):
        print(" i have brwon faur")

    def bark(self):
        print("woof")

    def quack(self):
        print("only bark")

    def walk(self):
        print("walk on 4")

def main():
    donald = Duck()
    fido = Dog()
    for o  in (donald, fido):
        in_the_forest(o)
        in_the_lake(o)

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_lake(duck):
    duck.quack()
    duck.walk()



if __name__ == "__main__":main()
