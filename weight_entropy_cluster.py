import os

os.environ["OMP_NUM_THREADS"] = '1'
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans


def entropy_weight_kmeans(data):
    # 将NaN替换为0
    data[np.isnan(data)] = 0
    temp, k_temp = -1, 0
    # 标准化处理，使得不同指标的数据具有可比性
    data = (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))
    # 使用Kmeans++聚类方法将指标分为k个类别
    for k in range(2, 8):
        kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=0)
        kmeans.fit(data)
        labels = kmeans.labels_
        from sklearn.metrics import silhouette_score
        # X为数据集，labels为样本所属的簇标签
        score = silhouette_score(X, labels)
        if score > temp:
            temp = score
            k_temp = k
    k = k_temp
    print("最佳聚类为：", k)
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=0)
    kmeans.fit(data)
    labels = kmeans.labels_
    # 计算各类别的数据熵
    entropy = np.zeros(k)
    for i_tag in range(k):
        # 获取属于当前类别的样本
        samples = data[labels == i_tag, :]
        # 计算当前类别的数据熵
        epsilon = 1e-8  # 设置一个很小的数，避免出现0值
        entropy[i_tag] = np.sum(-samples * np.log(samples + epsilon), axis=0).sum()
    # 计算各指标的权重
    weight = (1 - entropy) / np.sum(1 - entropy)

    return weight


lab_times = 20
for i in range(lab_times):
    print("第{}次实验".format(i + 1))
    # 生成样本数据
    X, _ = make_blobs(n_samples=300, n_features=8)
    # 使用Kmeans++聚类优化熵权法计算指标权重
    weights = entropy_weight_kmeans(X)
    # 输出指标权重
    print("Weights:", weights)
