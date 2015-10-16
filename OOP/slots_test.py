'''
Created on 2015年10月16日

@author: apple
'''
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
    
s = Student()
s.name  ='kw'
s.score = 66
print(s.name)
# print(s.score)

class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 99

print(g.score)