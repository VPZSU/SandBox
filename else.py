# try:
#     print(1)
#     print(1 + "1" == 2)
#     print(2)
# except TypeError:
#     print(3)
# else:
#     print(4)

for i in range(10):
    try:
        if 10 / i == 2.0:
            break
    except ZeroDivisionError:
        print(1)
    else:
        print(2)
