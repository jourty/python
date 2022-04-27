#逻辑运算符  and与  or或  not非
# and
# and两边的数据  必须全部都是TRUE的时候  才会返回TRUE  只要有一端返回FALSE  那么久返回FALSE
# False
print(10>20 and 10>11)
# False
print(10>5 and 10>11)
# False
print(10>11 and 10>5)
# True
print(10>5 and 10>6)

# or 或者
# False
print(10>20 or 10>21)
# True
print(10>5 or 10>20)
# True
print(10>20 or 10>5)
# True
print(10>5 or 10>6)

# not  非   取反
# False
print(not True)
# True
print(not False)
# True
print(not (10>20))