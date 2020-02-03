class Circle(object):
   pi = 3.14  # 类属性

   def __init__(self, r):
       self.r = r  # 实例属性

   def get_area(self):
       """ 圆的面积 """
       #return self.r**2 * Circle.pi # 通过实例修改pi的值对面积无影响，这个pi为类属性的值
       return self.r**2 * self.pi  # 通过实例修改pi的值对面积我们圆的面积就会改变

circle1 = Circle(2)
circle1.pi = 9
print(circle1.get_area())  # 调用方法 self不需要传入参数，不要忘记方法后的括号  输出 3.14