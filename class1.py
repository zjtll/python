#coding=UTF_8
#类用来描述具有相通属性的方法和集合
"""
1、命名方式为首字母大写 驼峰法
2、见名思意
3、区分大小写
4、类里面的变量为属性，类里面的函数称为方法

"""

#__init__是一个特殊的方法，每次创建新实例的时候都会自动执行
#类中的方法都必须有形参"self","他是一个指向实例本身的引用，让实例能够访问类中的属性和方法"
#以self开头的变量名可以被类中所有的方法使用
#python 2.7中创建类需要再（）内加入object
class Dog(object):
    def __init__(self,name,age):
        self.names = name
        self.ages = age
    def sit(self):
        print(self.names)
    def over(self):
        print(self.ages)
#创建实例
my_dog=Dog("wang","2")

#通过实例名调用类中的方法
my_dog.sit()
my_dog.over()

#通过实例名访问类中的属性
print("my dog name is: "+my_dog.names)
print("my dog age is: "+ my_dog.ages)

#car 类
class Car(object):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.ss=0  #设置属性初始值为0
    def get_describe(self):
        test = str(self.year)+ ' ' + str(self.make) + ' '+ str(self.model)
        return test.title()
    def tank(self):
        print("100L油")
my_car=Car('audi','a6','2017')
print(my_car.get_describe())
my_car.ss=1 #修改属性的值
print(my_car.ss)
print("===============")

#继承，super()表示调用父类的方法，python3中直接使用super().xx即可，python2.7中super()的括号中需要添加俩个参数 子类名和对象self

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super(ElectricCar,self).__init__(make,model,year)
        self.sudu=70    #定义子类属性
    def su(self):      #定义子类方法
        print(str(self.model)+"最高速度为："+str(self.sudu))
    def tank(self):    #重写父类方法
        print("电动汽车没有油箱")
ele=ElectricCar('tesla','model s','2020') #实例化子类
print(ele.get_describe())
ele.su()
ele.tank()

#类的导入时使用和函数的类似

#9*9 python2.7再print()后加“，”表示不换行，在python3中使用print(i*j,end=" ")
for i in range(1,10):
    for j in range(1,i+1):
        print ("%d*%d=%d"%(i,j,i*j)),
    print ("")

print("%d==%d"%(1,1.0))