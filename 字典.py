#coding=UTF_8
print("字典学习")
#字典 是一系列键—值对 。每个键 都与一个值相关联，你可以使用键来访问与之相关联的值。
#与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。
test = {"a":1,"b":2}
print(test["a"])
#增加键值
test["c"]=3
print(test["c"])
#修改键值
test["a"]="change"
print(test["a"])
print(test)
#删除键值
del test["b"]
print(test)
#创建空字典
alien={}
print(alien)

alien["color"]="green"
alien["points"]=10

print(alien)
print("=================")

#for 遍历字典--遍历所有键值对
info={"username":"zjt","password":"123","vcode":"xxx"}
for k,y in info.items():
    print(k+" === "+y+"\n")

#for遍历字典所有的键
for k in info.keys():
    print(k)

#for遍历字典所有的值
for v in info.values():
    print(v)

#使用集合set可以剔除重复的值
lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for v in set(lang.values()):
    print(v)
print("嵌套--可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典")
#列表中存放字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#字典中存放列表
languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}
print(languages)
for k,y in languages.items():
    print(k)
    for y in y:
        print(y)
    print("\n")
#字典中存储字典
users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
}
for ae,mc in users.items():
    print(ae)
    for kk,mm in mc.items():
        print(kk+"---"+mm)
print(users['mcurie']['location'])