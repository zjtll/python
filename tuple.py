#coding=UTF_8
#元组，列表值可以修改，元组的值不能修改

print("元组学习")
test=(1,2,3,4)

print(test[1])
for i in test:
    print(i)
# test[0]=1 元组不支持修改元素
# print(test)
#给存储元组变量赋值，会覆盖以前的值，相当于重新定义整个元组
test=(5,6)
print(test)

