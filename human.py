####################################################
## 6.1 类的继承
####################################################

# 继承机制允许子类可以继承父类上的方法和变量。
# 我们可以把 Human 类作为一个基础类或者说叫做父类，
# 然后定义一个名为 Superhero 的子类来继承父类上的比如 "species"、 "name"、 "age" 的属性
# 和比如 "sing" 、"grunt" 这样的方法，同时，也可以定义它自己独有的属性

# 如果把 Human 类放在独立的 human.py 中，其他文件可以用以下语句导入：
# from "filename-without-extension" import "function-or-class"
# from human import Human
# 本示例把类都定义在当前文件中，直接使用即可，不要导入当前文件自身。


class Human:
    species = "H. sapiens"

    def __init__(self, name):
        self.name = name
        self._age = 0

    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    def sing(self):
        return 'yo... yo... microphone check... one two... one two...'

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def grunt():
        return "*grunt*"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age


# 指定父类作为类初始化的参数
class Superhero(Human):
    # 如果子类需要继承所有父类的定义，并且不需要做任何的修改，
    # 你可以直接使用 "pass" 关键字（并且不需要其他任何语句）
    # 但是在这个例子中会被注释掉，以用来生成不一样的子类。
    # pass

    # 子类可以重写父类定义的字段
    species = 'Superhuman'

    # 子类会自动的继承父类的构造函数包括它的参数，但同时，子类也可以新增额外的参数或者定义，
    # 甚至去覆盖父类的方法比如说构造函数。
    # 这个构造函数从父类 "Human" 上继承了 "name" 参数，同时又新增了 "superpower" 和
    # "movie" 参数:
    def __init__(self, name, movie=False,
                 superpowers=["super strength", "bulletproofing"]):
        # 新增额外类的参数
        self.fictional = True
        self.movie = movie
        # 注意可变的默认值，因为默认值是共享的
        self.superpowers = superpowers

        # "super" 函数让你可以访问父类中被子类重写的方法
        # 在这个例子中，被重写的是 __init__ 方法
        # 这个语句是用来运行父类的构造函数:
        super().__init__(name)

    # 重写父类中的 sing 方法
    def sing(self):
        return 'Dun, dun, DUN!'

    # 新增一个额外的方法
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))


if __name__ == '__main__':
    sup = Superhero(name="Tick")

    # 检查实例类型
    if isinstance(sup, Human):
        print('I am human')
    if type(sup) is Superhero:
        print('I am a superhero')

    # 获取方法解析顺序 MRO，MRO 被用于 getattr() 和 super()
    # 这个字段是动态的，并且可以被修改
    print(Superhero.__mro__)  # => (<class '__main__.Superhero'>,
    # => <class '__main__.Human'>, <class 'object'>)

    # 调用父类的方法并且使用子类的属性
    print(sup.get_species())  # => Superhuman

    # 调用被重写的方法
    print(sup.sing())  # => Dun, dun, DUN!

    # 调用 Human 的方法
    sup.say('Spoon')  # => Tick: Spoon

    # 调用 Superhero 独有的方法
    sup.boast()  # => I wield the power of super strength!
    # => I wield the power of bulletproofing!

    # 继承类的字段
    sup.age = 31
    print(sup.age)  # => 31

    # Superhero 独有的字段
    print('Am I Oscar eligible? ' + str(sup.movie))


####################################################
## 6.2 多重继承
####################################################

# 定义另一个类（如果拆成独立模块，可以放在 bat.py 中）
class Bat:
    species = 'Baty'

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # 这个类同样有 say 的方法
    def say(self, msg):
        msg = '... ... ...'
        return msg

    # 新增一个独有的方法
    def sonar(self):
        return '))) ... ((('


if __name__ == '__main__':
    b = Bat()
    print(b.say('hello'))
    print(b.fly)

# 现在我们来定义一个类来同时继承 Superhero 和 Bat。
# Superhero 和 Bat 已在上方定义，不需要从其他模块导入。


# 定义 Batman 作为子类，来同时继承 SuperHero 和 Bat
class Batman(Superhero, Bat):

    def __init__(self, *args, **kwargs):
        # 通常要继承属性，你必须调用 super:
        # super(Batman, self).__init__(*args, **kwargs)
        # 然而在这里我们处理的是多重继承，而 super() 只会返回 MRO 列表的下一个基础类。
        # 因此，我们需要显式调用初始类的 __init__
        # *args 和 **kwargs 传递参数时更加清晰整洁，而对于父类而言像是 “剥了一层洋葱”
        Superhero.__init__(self, 'anonymous', movie=True,
                           superpowers=['Wealthy'], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # 重写了 name 字段
        self.name = 'Sad Affleck'

    def sing(self):
        return 'nan nan nan nan nan batman!'


if __name__ == '__main__':
    sup = Batman()

    # 获取方法解析顺序 MRO，MRO 被用于 getattr() 和 super()
    # 这个字段是动态的，并且可以被修改
    print(Batman.__mro__)  # => (<class '__main__.Batman'>,
    # => <class '__main__.Superhero'>,
    # => <class '__main__.Human'>,
    # => <class '__main__.Bat'>, <class 'object'>)

    # 调用父类的方法并且使用子类的属性
    print(sup.get_species())  # => Superhuman

    # 调用被重写的类
    print(sup.sing())  # => nan nan nan nan nan batman!

    # 调用 Human 上的方法，(之所以是 Human 而不是 Bat)，是因为继承顺序起了作用
    sup.say('I agree')  # => Sad Affleck: I agree

    # 调用仅存在于第二个继承的父类的方法
    print(sup.sonar())  # => ))) ... (((

    # 继承类的属性
    sup.age = 100
    print(sup.age)  # => 100

    # 从第二个类上继承字段，并且其默认值被重写
    print('Can I fly? ' + str(sup.fly))  # => Can I fly? False


####################################################
## 7. 高级用法
####################################################

# 用生成器(generators)方便地写惰性运算
def double_numbers(iterable):
    for i in iterable:
        yield i + i


# 生成器只有在需要时才计算下一个值。它们每一次循环只生成一个值，而不是把所有的
# 值全部算好。
#
# range的返回值也是一个生成器，不然一个1到900000000的列表会花很多时间和内存。
#
# 如果你想用一个Python的关键字当作变量名，可以加一个下划线来区分。
range_ = range(1, 900000000)
# 当找到一个 >=30 的结果就会停
# 这意味着 `double_numbers` 不会生成大于30的数。
for i in double_numbers(range_):
    print(i)
    if i >= 30:
        break
# 你也可以把一个生成器推导直接转换为列表
values = (-x for x in [1, 2, 3, 4, 5])
gen_to_list = list(values)
print(gen_to_list)  # => [-1, -2, -3, -4, -5]

# 装饰器(decorators)
# 这个例子中，beg装饰say
# beg会先调用say。如果返回的say_please为真，beg会改变返回的字符串。
from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please


print(say())  # Can you buy me a beer?
print(say(say_please=True))  # Can you buy me a beer? Please! I am poor :(
