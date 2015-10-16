'''
Created on 2015年10月16日

@author: apple
'''

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')
        
class Timer(object):
    def run(self):
        print('Start...')
        
def run_twice(animal):  #file-like object
    animal.run()
    
a = Animal()
d = Dog()
c = Cat()
t = Timer()

run_twice(c)
run_twice(t)



