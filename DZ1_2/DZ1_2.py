# Задача 2.
# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = False
y = False
z = False
result = True


def chek(x, y, z):
    if (not (x or y or z)) == (not x and not y and not z):
        result = True
        print(1)
    else:
        result = False
        print(0)
    return result


chek(x, y, z)

# resultLeft = True
# resultRight = True
# if x != True:
#     if y != True:
#         if z != True:
#             resultLeft = True
#             print(1)
# else:
#     resultLeft = False


# if not x == True:
#     if not y == True:
#         if not z == True:
#             resultRight = False
#             print(0)
# else:
#     resultRight = True
# if resultLeft == resultRight:
# if (not (x or y or z)) == (not x and not y and not z):
#     print('1 ')
# else:
#     print('0 ')
