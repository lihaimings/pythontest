from gc import is_finalized

import json

print("hello world")
# 你好呀
"""
nihao 
"""
print("今天的天气")
money = 50
print("钱包还有：",money)
money = money-10
print("买了冰激凌，钱包还有：",money,"元")



print(type("nihao"))
print(type(666))
print(type(11.365))

string_type = type("sdf")
int_type = type(11)
float_type = type(1.23)
print(string_type,int_type,float_type)

name = "nihao"
name_type = type(name)
print(name_type)



num_str = str(123)
print(type(num_str),num_str)


float_str = str(1.23)
print(type(float_str),float_str)


num = int(123)
print(type(num),num)

float_num = float(11.23)
print(type(float_num),float_num)

int_num = int(11.23)
print(type(int_num),int_num)


name= 'nihao'
print(type(name))

name= "hello"
print(type(name))


name ="""he
llo"""
print(type(name),name)


k = True
k = False

print(type(k),k)

k = not True
k = not False

print(type(k),k)


k = False and True
print(type(k),k)
k = False or True
print(type(k),k)




print(True+True)
print(True*8)
print(False-5)


print(0==True,1==True,0==False,1==False)

print(bool(0))
print(bool(1))
print(bool(4))
print(bool(-5))
print((0 and 1), (0 or 1),(0 and 2),(-5 or 0))

# is对比变量引用， ==对比数值
a = [1,2,3,4]
b = a
print(b is a , b == a)
b= [1,2,3,4]
print(b is a , b == a)


# 字符串可以被当作列表
print("HELLOWORD"[0])

print(len("nihao"))
name = "nihao"
print(f"{name} haha")
print(f"{name} de changdu {len(name)}")

print("{} can be {}".format("ni","niubi"))
print("{0} can be {1} hahh {0}".format("ni","niubi"))
print("{name} can be {food}".format(name="nihao",food="niubi"))


print(bool(0))
print(bool(""))

k = "hao" if 0<1 else "haha"
print(k)

li = []
other_li = [4,5,6]
li.append(1)
li.append(2)
li.append(3)
li.append(4)

print(li)

print(li.pop(),li)

li.append(4)

print(li[0],li[-1])

print(li[1:3])
print(li[2:])
print(li[:3])
print(li[::2])
print(li[::-1])

li2 = li[:]
print(li2)

print(li.remove(2),li)

print(li.insert(1,2),li)

print(li.index(2),li.index(4))

print(li+li2)

print(li.extend(li2),li)

print((1 in li))

print(len(li))


tup = (1,2,3)
print(tup[0])
# tup[0]= 3 #不可以赋值
print(len(tup),tup+(4,5,6),tup[:2],tup[1:3],tup[2:],2 in tup)

a,b,c= (1,2,3)
a,*b,c =(1,2,3,4,5)
print(a,b,c)
d,e,f=(1,2,3)
print(d,e,f)
e,d = d,e
print(d,e)

empty_dict = {}
filled_dict = {"one":1,"two":2,"three":3}
print(filled_dict)
valid_dict = {(1,2,3):[1,2,3]}

print(filled_dict["one"])

print(list(filled_dict.keys()))
print(list(filled_dict.values()))

print("one" in filled_dict)
print(1 in filled_dict)
# print(filled_dict["four"]) # 没有的key会报错，但get不会
print(filled_dict.get("one"),filled_dict.get("four",4))
print(filled_dict.setdefault("five",5))
print(filled_dict.setdefault("five",6))
print(filled_dict)
filled_dict.update({"four":4})
print(filled_dict["four"])
del filled_dict["one"]
print(filled_dict)

empty_set = set()
some_set = {1,1,2,2,3,4}
filled_set = some_set
valid_set = {(1,),1}

filled_set = some_set

filled_set.add(5)
filled_set.add(5)
other_set = {3,4,5,6}
k = filled_set & other_set
print(filled_set)
print(other_set)
print(k)

k = filled_set | other_set
print(k)

k = {1,2,3,4} - {1,2}
print(k)

# "^" 取异或集（对称差）
k = {1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}
print(k)

# 判断左边的集合是否是右边集合的超集
k ={1, 2} >= {1, 2, 3} # => False
print(k)

# 判断左边的集合是否是右边集合的子集
k = {1, 2} <= {1, 2, 3} # => True
print(k)


# in 测试集合是否包含元素
k = 2 in filled_set   # => True
print(k)
k = 10 in filled_set   # => False
print(k)

# 单层集合的深度复制
k= filled_set = some_set.copy()  # filled_set 是 {1, 2, 3, 4, 5}
print(k)
k =filled_set is some_set        # => False
print(k)

####################################################
## 3. 流程控制和迭代器
####################################################

# 先随便定义一个变量
some_var = 5
# 这是个if语句。注意缩进在Python里是有意义的！
# 缩进要使用 4 个空格而不是 tabs。
# 这段代码会打印 "some_var is smaller than 10"
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:    # elif 语句是可选的
    print("some_var is smaller than 10.")
    print(":hahhaa")
else:                  # else 也是可选的
    print("some_var is indeed 10.")

"""
用 for 循环语句遍历列表
打印:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # 你可以使用 format() 格式化字符串并插入值
    print("{} is a mammal".format(animal))

# d = ["dog","cat"]
d = ("dog","cat")
for k in d:
    print(f"{k} h")

"""
"range(number)" 返回数字列表从 0 到 number 的数字
打印:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(lower, upper)" 会返回一个包含从 lower 到 upper 的数字迭代器
prints:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)

"""
"range(lower, upper, step)" 会返回一个，从 lower 到 upper、并且间隔值为 step 的迭代器。
如果 step 未传入则会使用默认值 1
prints:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)

"""
遍历列表，并且同时返回列表里的每一个元素的索引和数值。
prints:
    0 dog
    1 cat
    2 mouse
"""
animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)



"""
while 循环直到条件不满足
打印:
    0
    1
    2
    3
"""

x = 0
while x < 4:
    print(x)
    x += 1  # x = x + 1 的简写

# 用 try/except 块处理异常状况
try:
    # 用 raise 抛出异常
    raise IndexError("This is an index error")
except IndexError as e:
    pass    						 # pass 是无操作，但是应该在这里处理错误
except (TypeError, NameError):
    pass    						 # 可以同时处理不同类的错误
else:                    # else语句是可选的，必须在所有的except之后
    print("All good!")   # 只有当try运行完没有错误的时候这句才会运行
finally:								 # 在任何情况下都会执行
 	print("We can clean up resources here")


# 你可以使用 with 语句来代替 try/finally 对操作进行结束的操作
with open("myfile.txt", "w+") as file:
    file.write(str("NIHAO"))  # 写入字符串到文件

with open("myfile.txt") as f:
    for line in f:
        print(line)


# 写入文件
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w+") as file:
    file.write(str(contents))  # 写入字符串到文件

with open("myfile2.txt", "w+") as file:
    file.write(json.dumps(contents)) # 写入对象到文件

# Reading from a file
with open("myfile1.txt", "r+") as file:
    contents = file.read()           # 从文件读取字符串
print(contents)
# print: {"aa": 12, "bb": 21}

with open("myfile2.txt", "r+") as fileS:
    contents = json.load(fileS)       # 从文件读取 json 对象
print(contents)
# print: {"aa": 12, "bb": 21}

# Windows 环境调用 open() 读取文件的默认编码为 ANSI，如果需要读取 utf-8 编码的文件，
# 需要指定 encoding 参数:
# open("myfile3.txt", "r+", encoding = "utf-8"
#

# Python 提供一个叫做可迭代 (iterable) 的基本抽象。一个可迭代对象是可以被当作序列
# 的对象。比如说上面 range 返回的对象就是可迭代的。
filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) # => dict_keys(['one', 'two', 'three'])，是一个实现可迭代接口的对象

# 可迭代对象可以遍历
for i in our_iterable:
    print(i)    # 打印 one, two, three

# 但是不可以随机访问
# our_iterable[1]  # 抛出TypeError

# 可迭代对象知道怎么生成迭代器
our_iterator = iter(our_iterable)

# 迭代器是一个可以记住遍历的位置的对象
# 用 "next()" 获得下一个对象
next(our_iterator)  # => "one"

# 再一次调取 "next()" 时会记得位置
next(our_iterator)  # => "two"
next(our_iterator)  # => "three"

# 当迭代器所有元素都取出后，会抛出 StopIteration
# next(our_iterator) # 抛出 StopIteration

# 我们还可以通过遍历访问所有的值，实际上，for 内部实现了迭代
our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i)  # 依次打印 one, two, three

# 可以用 list 一次取出迭代器或者可迭代对象所有的元素
list(filled_dict.keys())  # => 返回 ["one", "two", "three"]
list(our_iterator)  # => 返回 [] 因为迭代的位置被保存了

####################################################
## 4. 函数
####################################################

# 用def定义新函数
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y    # 用 return 语句返回

# 调用函数
add(5, 6)   # => 打印 "x is 5 and y is 6" 并且返回 11
# 也可以用关键字参数来调用函数
add(y=6, x=5)   # 关键字参数可以用任何顺序

# 我们可以定义一个可变参数函数
def varargs(*args):
    return args

varargs(1, 2, 3)   # => (1, 2, 3)


# 我们也可以定义一个关键字可变参数函数
def keyword_args(**kwargs):
    return kwargs

# 我们来看看结果是什么：
print(keyword_args(big="foot", loch="ness"))   # => {"big": "foot", "loch": "ness"}

# 这两种可变参数可以混着用
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""
# 调用可变参数函数时可以做跟上面相反的，用 * 展开元组，用 ** 展开字典。
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)   # 相当于 all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)   # 相当于 all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)   # 相当于 all_the_args(1, 2, 3, 4, a=3, b=4)

# 使用返回多个数值（返回值为元组类型）
def swap(x, y):
    return y, x  # 用不带括号的元组的格式来返回多个数值
                 # (注意: 括号不需要加，但是也可以加)

x = 1
y = 2
x, y = swap(x, y)     # => x = 2, y = 1
print(x, y)
# (x, y) = swap(x,y)  # 同上，括号不需要加，但是也可以加

# 函数作用域
x = 5

def setX(num):
    # 局部作用域的 x 和全局域的 x 是不同的
    x = num # => 43
    print (x) # => 43

def setGlobalX(num):
    global x
    print (x) # => 5
    x = num   # 现在全局域的 x 被赋值
    print (x) # => 6

print(setX(43))
print(setGlobalX(6))


# 函数在 Python 是一等公民
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
print(add_10(3))  # => 13

# 也有匿名函数
print((lambda x: x > 2)(3))                # => True
print((lambda x, y: x ** 2 + y ** 2)(2, 1))  # => 5

# 内置的高阶函数
print(list(map(add_10, [1, 2, 3])))         # => [11, 12, 13]
print(list(map(max, [1, 2, 3], [4, 2, 1])))  # => [4, 2, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]

# 用列表推导式可以简化映射和过滤。列表推导式的返回值是另一个列表。
K = [add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
print(k)
k = [x for x in [3, 4, 5, 6, 7] if x > 5]   # => [6, 7]
print(k)

# 你也可以用这种方式实现对集合和字典的构建
K= {x for x in 'abcddeef' if x not in 'abc'}  # => {'d', 'e', 'f'}
print(k)
k={x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(k)

####################################################
## 5. 模块
####################################################
# 导入模块
import math
print(math.sqrt(16))  # => 4.0

# 你可以导入模块中具体的函数
from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0

# 你可以对模块名进行简化
import math as m
   # => True
print(math.sqrt(16) == m.sqrt(16))


# Python 模块实质上是 Python 文件
# 你可以自己编写自己的模块，然后导入
# 模块的名称和文件名相同
# 你可以用 "dir()" 查看模块中定义的函数和字段
import math
print(dir(math))

# 当你的脚本文件所在的文件夹也包含了一个名为 math.py 的 Python 文件
# 这个 math.py 文件会被代替引入，而不是引入 Python 內建模块中的 math
# 出现这个情况的原因是本地文件夹的引入优先级要比 Python 內建库引入优先级要高


####################################################
## 6. 类
####################################################

# 我们使用 "class" 语句来创建类
class Human:

    # 一个类的字段。 这个字段共享给这个类的所有实例。
    species = "H. sapiens"

    # 构造方法，当实例被初始化时被调用。注意名字前后的双下划线，这是表明这个属性
    # 或方法对 Python 有特殊意义，但是允许用户自行定义。
    # 方法(可能是对象或者属性) 类似: __init__, __str__,__repr__ etc
    # 都是特殊的方法
    # 你自己取名时不应该用这种格式
    def __init__(self, name):
        # 将参数赋值给实例的 name 字段
        self.name = name

        # 初始化属性
        self._age = 0

    # 实例方法，第一个参数总是self，也就是这个实例对象
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # 另一个实例方法
    def sing(self):
        return 'yo... yo... microphone check... one two... one two...'

    # 类方法，被所有此类的实例共用。
    # 第一个参数是这个类对象。
    @classmethod
    def get_species(cls):
        return cls.species

    # 静态方法。调用时没有实例或类的绑定。
    @staticmethod
    def grunt():
        return "*grunt*"

    # property 有点类似 getter
    # 它把方法 age() 转换为同名并且只读的属性
    # 通常情况下，可以不需要编写复杂的 getter 和 setter。
    @property
    def age(self):
        return self._age

    # 允许属性被修改
    @age.setter
    def age(self, age):
        self._age = age

    # 允许属性被删除
    @age.deleter
    def age(self):
        del self._age

# 当 Python 解释器在读取源文件的时候，就会执行文件中所有的代码
# 对 __name__ 的检查可以保证这块代码只会在这个模块是主程序的情况下被运行（而不是在引用时运行）
if __name__ == '__main__':
    #
    i = Human(name="Ian")
    i.say("hi")                     # "Ian: hi"
    j = Human("Joel")
    j.say("hello")                  # "Joel: hello"
    # i 和 j 都是 Human 实例化后的对象，换一句话说，它们都是 Human 实例

    # 运行类方法 (classmethod)
    i.say(i.get_species())          # "Ian: H. sapiens"
    # 修改共享的类属性
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())          # => "Ian: H. neanderthalensis"
    j.say(j.get_species())          # => "Joel: H. neanderthalensis"

    # 运行静态方法 (staticmethod)
    print(Human.grunt())            # => "*grunt*"

    # 实例上也可以执行静态方法
    print(i.grunt())                # => "*grunt*"

    # 更新实例的属性
    i.age = 42
    # 访问实例的属性
    i.say(i.age)                    # => "Ian: 42"
    j.say(j.age)                    # => "Joel: 0"
    # 删除实例的属性
    del i.age
    # i.age                         # => 这会抛出一个错误: AttributeError

