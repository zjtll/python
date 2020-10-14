#coding=UTF_8
#导入模块调用函数,import mod 表示导入名为mod.py文件中的整个模块，里面所有的函数都可以直接调用
import mod
mod.make_pizza(10,"aa","bb","cc")
mod.make_pizza(15,"hello")

#导入特定的函数,导入mod模块的names函数，后面通过“，”号分割可以指定多个。这种方法就调用时不需要通过mod.函数名来调用直接使用就行
from mod import names
names("fattar")

#使用 as 给函数指定别名为mp,直接使用mp等于使用make_pizza
from mod import make_pizza as mp
mp(23,"dfffff")

#使用as给模块指定别名为fn
import mod as fn
fn.names("模块别名")

#导入模块中所有函数,不推荐使用这种方式（要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法。这能让代码更清晰，更容易阅读和理解）
#from mod import *
from class1 import Dog
dog=Dog("sd",4)
