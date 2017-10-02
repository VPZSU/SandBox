class Super2(object):
    pass

class Super1(object):
    pass

class ToAnalyze(Super1, Super2):
    def method1(self):
        pass
    def method2(self):
        a = 10
        print(a)
        self.b = 10
        
class Sub1(ToAnalyze):
    pass