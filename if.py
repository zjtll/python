#coding=UTF_8
print("if条件语句")
print("一个'='代表赋值，俩个'='用于判断是否相等")
cars = ['audi', 'bmw', 'subaru', 'toyota']
print(cars)
for i in cars:
    if i == "bmw":
        print(i.upper())
    else:
        print(i.title())
a=1
b=2
if a==b:
    print("a等于b")
elif a < b:
    print("a小于b")
else:
    print("a大于b")

x="haha"
if x != "1haha":
    print("1")
else:
    print("2")
#条件表达式 与（and）、或（or）
if a == 1 and b ==2:
    print("success")
if a == 1 or b == 1:
    print("successful")
# in | not in
top = ['cpu','mem','pid']
if 'cpu' in top:
    print("cpu 在 top中")
if 'cmd' not in top:
    print("cmd 不在top中")
a="True"
if a=='True':
    print("haha")
print(float(10)/3)