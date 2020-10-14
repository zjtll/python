#coding=UTF_8
#列表,访问列表
"""
a=[1,2,3,4]
print(a)
print(a[2])
print(a[-1]) #-1表示访问最后一个元素、-2访问倒数第二个元素、-3访问倒数第三个元素、以此类推
#修改列表元素
b=["honda","yamaha","ducat"]
b[1]="xxx"
print(b)
#添加列表元素在结尾
b.append("jiewei")
print(b)
#插入列表元素
b.insert(1,"hahaa")
print(b)
#删除列表元素d
del b[0]
print(b)
#pop方法删除列表末尾元素
c=["aaa","bbb","ccc"]
print(c)
d=c.pop()
print(d)
print(c)
#pop方法弹出（删除）列表任何位置元素
motor=["honda","yamaha","suzuki"]
print(motor)
first=motor.pop(0)
print(first)
print(motor)
#根据值删除元素使用remove(),如果有多个相同的值只删除第一个,如果要全部删除需要用到循环来判断
motorcycles = ['honda11', 'yamaha11', 'suzuki11', 'ducati11','honda11']
motorcycles.remove("honda11")
print(motorcycles)

#列表排序,使用sort()对列表进行永久排序
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# cars.sort()
# print(cars)
# # reverse反转列表
# cars.sort(reverse=True)
# print(cars)
# 使用sorted临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)
# 反转列表
cars.reverse()
print(cars)
#列表长度计算
print(len(cars))
# for循环遍历列表，python根据缩进来判断代码的关系，注意缩进
for i in cars:
    print(i)
#使用range()函数,左闭右开，range(1,10)打印1--9数字
for j in range(1,10):
    print(j)
#指定步长为2
for j in range(1,10,2):
    print(j)
#使用range创建数字列表
x=list(range(1,5))
print(x)
print("---------------")
#将计算得到的平方值附加到列表
aa=[]
for val in range(1,10):
    aa.append(val**2)
print(aa)
#数字列表统计运算，找出最小值、最大值、和
print(min(aa))
print(max(aa))
print(sum(aa))
print("----")
# 列表解析，效果和上面的一样，只需一行代码即可实现
squares = [value**2 for value in range(1,10)]
print(squares)
print("-----")
lis=list(range(1,101))
s=0
for i in lis:
    print(i)
    print(min(lis))
    print(max(lis))
    print(sum(lis))
    s=s+i
print(s)
"""
# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(len(players))
print(players[0:3])  #索引为0-2的元素
print(players[:2]) #从开头到1
print(players[3:]) #3到结尾
print(players[-3:]) #倒数第三到结尾
print("----------------")
#列表复制，使用切片的方式复制，[:]表示始于第一个元素，终止于最后一个元素，即复制整个列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
my_foods.append("toto")
friend_foods.append("bobo")
print(my_foods)
print(friend_foods)
for i in my_foods:
    print(i)



aaa=[i for i in range(1,10)]

print(aaa)
for i in range(10):
    print(i)
a=list(range(1,101))
print(sum(a))