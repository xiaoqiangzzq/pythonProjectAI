import matplotlib.pyplot as plt
import numpy as np


#
# lambda 是 Python 中的一个关键字，用于创建匿名函数。匿名函数是一种没有具体名称的小型、临时的函数，通常用于一次性的、简单的操作。lambda 函数的语法如下：
#
# python
# Copy code
# lambda arguments: expression
# lambda：关键字，用于声明匿名函数。
# arguments：参数列表，类似于普通函数的参数列表。
# expression：函数体，即返回值的表达式。
# 举例说明：
#
# python
# Copy code
# # 使用普通函数的方式定义
# def add(x, y):
#     return x + y
#
# # 使用 lambda 表达式定义
# add_lambda = lambda x, y: x + y
#
# # 调用普通函数
# result_normal = add(2, 3)
#
# # 调用 lambda 函数
# result_lambda = add_lambda(2, 3)
#
# print(result_normal)  # 输出：5
# print(result_lambda)  # 输出：5
# 在上面的例子中，add_lambda 是一个使用 lambda 表达式定义的匿名函数，它与普通函数 add 具有相同的功能。
#
# lambda 函数通常用于函数体比较简单的情况，例如在函数式编程、map、filter、sorted 等函数中作为参数传递。

# 构建方程
f = lambda x: (x - 3.5) ** 2 - 4.5 * x + 10

# 导函数
g = lambda x: 2 * (x - 3.5) - 4.5

x = np.linspace(0, 10, 1000)

y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the function f(x)')
plt.grid(True)
plt.show()


#常规方法：另导数为0可以求解函数,x = 5.75


#如果没有确切方程，或者无法求导，梯度下降算法


#学习率
eta = 0.3

#随机初始值
x = np.random.random_integers(0,12,1)[0]

last_x = x + 0.1

#精确度
precision = 0.00001

print('随机x为：' , x)


while True:
    if np.abs(x - last_x) < precision:
        break
    last_x = x
    x = x - eta * g(x)
    print('更新后x为',x)
