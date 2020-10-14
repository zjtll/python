#coding=UTF_8
#print("hello world")
#变量学习
message="hello python world"
print(message)

# 字符串使用引号("xxx")括起来的都是都是字符串可以是单引号也可以是双引号
name="ada loVelace"
#输出时首字母大写
print(name.title())
#全部转换为大写
print(name.upper())
#全部转换为小写
print(name.lower())
#合并字符串用+号
a="123"
b="abc"
c=a+" "+b
print(c.upper()+"haha")
print(a,b,c)
#换行符用\n 制表符用\t
print ("languages:\n\tpython\n\tjava\n\tc++")
#删除空白
ttt="   python   "
print(ttt.rstrip()) #删除结尾端空格
print(ttt.lstrip()) #删除开头端空格
print(ttt.strip())  #删除俩端空格
print("leaned'sfasd")
print(3.1*1.2)
age=24
mess="happy"+str(age)
print(mess)
