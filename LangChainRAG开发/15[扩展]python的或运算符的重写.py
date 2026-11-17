class Test(object):
    def __init__(self,name):
        self.name=name

    def __or__(self, other):
        return MySequence(self.name)

    def __str__(self):
        return self.name

class MySequence(object):
    def __init__(self,*args):
        self.sequence = []
        for arg in args:
            self.sequence.append(arg)

    def __or__(self, other):
        self.sequence.append(other)
        return self

    def run(self):
        for arg in self.sequence:
            print(arg)

if __name__=="__main__":
    a = Test("a")
    b = Test("b")
    c = Test("c")
    d = Test("d")
    e = Test("e")

    k = a | b | c |d|e
    k.run()
    print(k)
