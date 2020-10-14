#coding=UTF_8
#函数学习和使用,使用def来定义一个函数
def test():
    print("定义函数")
test()
#函数传递参数
def user(username,password):
    print("hello, " + username.title()+"=="+password)
user("zjt","123")
user("abc","666")
#实参和形参区别，上述代码中实参就是"zjt""123"调用函数时传递给函数的信息，形参就是username password用于存放实参的值,实参和形参一一对应
#关键字实参，在实参中将名称和值关联起来避免传递实参混淆
def pet(a,b):
    print(a+b)
pet(a=7,b=8)
a=[i**2 for i in range(1,5)]
print(a)

#return 语句就是将结果返回到调用的地方，并把程序的控制权一起返回,程序运行到所遇到的第一个return即返回（退出def块），不会再运行第二个return。
def a(x,y):
    if x==y:
        return x,y
    else:
        return 2,65
print a(3,4)
def test(ee):
    print(ee)
    return 1
test(22)
def fff():
    return 77
print fff()

#让实参变成可选的，如果定义了三个实参只传递了俩个参数此程序不能正确运行，可以通过给实参指定一个默认值--空字符串解决这个问题
def get_name(first_name,middle_name,last_name=''):
    if last_name:  #Python将非空字符串解读为True ，因此如果函数调用中提供了last_name，if last_name 将为True
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+middle_name
    return full_name.title()
print(get_name("aa","bb"))
print(get_name("aa","bb","cc"))

#return返回字典
def person(a,b):
    ppp={"first":a,"last":b}
    return ppp
print(person("z3","L4"))

#传递列表
def user(name):
    for i in name:
        msg=i.title()
        print("hello, " + msg)
username=["hehe","lll","sdd"]
print user(username)
print("=-==========================")
#传递任意数量的实参,形参名前面的*号可以让python创建一个名为top的空元组并将所有收到的值都分装到这个元组中
def make(*top):
    print(top)
make("aa","bb")
make(1,2,3,4,5)

#传递任意数量的实参，形参前面的**可以让python创建一个空字典，并将所有收到的k-v都封装到这个字典中
def profile(first,last,**info):
    pro = {}
    pro['first_name'] = first
    pro['last_name'] = last
    for k,v in info.items():
        pro[k] = v
    return pro
print profile("albert","einsten",local='princeton',field='physics')






