import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler


def entropy_weight(data):
    # 标准化处理，使得不同指标的数据具有可比性
    data = (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))
    # 计算熵值
    entropy = np.sum(-data * np.log(data), axis=0)
    # 计算权重
    weight = (1 - entropy) / np.sum(1 - entropy)
    return weight


# 生成模拟数据
X, _ = make_blobs(n_samples=100, centers=3, n_features=5, random_state=0)
# 对数据进行标准化
X = StandardScaler().fit_transform(X)
# 调用 entropy_weight 函数，得到各个指标的权重
weights = entropy_weight(X)
print("指标权重为：", weights)
