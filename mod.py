#coding=UTF_8
#函数模块定义
#形参名称*topp中的星号让python创建一个空元组，将收集所有的值都封装到这个元组中，可以传递任意数量的实参
def make_pizza(size,*topp):
    print("披萨的大小为："+str(size))
    print("披萨种类有：")
    for i in topp:
        print(i)

def names(name):
    print("my name is :" + name)
import datetime
date_long = datetime.datetime.utcnow().strftime('%Y%m%dT000000Z')
print(date_long)
