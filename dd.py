
# class OnlyOne:
#     class __OnlyOne:
#         def __init__(self, arg):
#             self.val = arg
#             
#         def __str__(self):
#             return repr(self) + self.val
#         
#     instance = None
#     
#     def __init__(self, arg):
#         if not OnlyOne.instance:
#             OnlyOne.instance = OnlyOne.__OnlyOne(arg)
#         else:
#             OnlyOne.instance.val = arg
#     def __getattr__(self, name):
#         return getattr(self.instance, name)
#     
# 
# x = OnlyOne('eggs')
# print(x)
# y = OnlyOne('spam')
# print(y)
# 
# #print(x.val)
class SingleTone(object):
    __instance = None
    def __new__(cls, val):
        if SingleTone.__instance is None:
            SingleTone.__instance = object.__new__(cls)
        SingleTone.__instance.val = val
        return SingleTone.__instance
    
a = SingleTone('zzz')
print(a)
b = SingleTone('zzz')
print(b)
print(a == b)


