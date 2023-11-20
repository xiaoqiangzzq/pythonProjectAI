import numpy as np

from sklearn.linear_model  import LinearRegression


# pip install -U scikit-learn

# 正规方程

# 二元一次方程
#   x + y = 14
#   2x - y = 10


if __name__ == '__main__':

    x = np.array([[1,1],[2,-1]])
    print(x)
# [[ 1  1]
#  [ 2 -1]]
    y = np.array([14, 10])
    w = np.linalg.solve(x, y)
    print('正常求救：')
    print(w)
# [8. 6.]


    print(x.T)
    # y = w0.x1 + w1 .x2
    # w = (xt.x)-1 . (xt.y)

    A = x.T.dot(x)
    print(A)

    # 逆矩阵
    B = np.linalg.inv(A)
    print("B is :")
    print(B)

    re = B.dot(x.T).dot(y)
    print('矩阵求救:')
    print(re)

# sklean算法

    # fit_intercept 不计算截距
    model = LinearRegression(fit_intercept=False)
    f = model.fit(x,y)
    print("sklean算法求救：")
    # coef 斜率
    print(model.coef_)



