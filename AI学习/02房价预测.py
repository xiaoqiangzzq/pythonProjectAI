import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression

# 指定版本才有数据集
# C:\Users\14817\PycharmProjects\pythonProject1\venv\Scripts\activate.bat
# pip install scikit-learn==1.0
# FutureWarning: Function load_boston is deprecated; `load_boston` is deprecated in 1.0 and will be removed in 1.2.

boston = datasets.load_boston()

X = boston['data']     # 数据
y = boston['target']   # 房价
feature_names = boston['feature_names']  # 具体指标

# 切分数据
index = np.array(range(506))
np.random.shuffle(index)

train_index = index[:405]
test_index = index[405:]

# 80%的训练数据
X_train = X[train_index]
y_train = y[train_index]

X_test = X[test_index]
y_test = y[test_index]

# 数据建模
np.set_printoptions(suppress=True)
model = LinearRegression(fit_intercept=True)
model.fit(X_train, y_train)

# 模型应用
y_pred = model.predict(X_test).round(2)
print(y_pred)
print(y_test)

#模型评分
#负数到1之间 ，1 最高分
score = model.score(X_test,y_test)
print(score)