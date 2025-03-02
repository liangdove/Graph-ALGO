# 图算法

### 图卷积网络（GCN）
GCN是一种基于谱图理论的图神经网络，它通过聚合节点的邻接信息来更新节点的特征表示。核心思想是将卷积操作从欧几里得空间推广到图结构数据上，通过图拉普拉斯矩阵的特征分解来定义图上的卷积操作。对于第 $l$ 层的节点特征更新，其公式为 $H^{(l + 1)} = \sigma(\tilde{D}^{-\frac{1}{2}}\tilde{A}\tilde{D}^{-\frac{1}{2}}H^{(l)}W^{(l)})$，其中 $\tilde{A}=A + I$ 是添加自环后的邻接矩阵，$\tilde{D}$ 是 $\tilde{A}$ 的度矩阵，$H^{(l)}$ 是第 $l$ 层的节点特征矩阵，$W^{(l)}$ 是第 $l$ 层的可学习权重矩阵，$\sigma$ 是激活函数。

### 图注意力网络（GAT）
GAT引入了注意力机制，允许节点在聚合邻接信息时为不同的邻居分配不同的权重，从而能够自适应地捕捉图中节点之间的重要性。注意力系数 $\alpha_{ij}$ 表示节点 $i$ 对其邻居节点 $j$ 的关注程度，计算公式为 $\alpha_{ij}=\frac{\exp(\text{LeakyReLU}(a^T[W h_i||W h_j]))}{\sum_{k\in\mathcal{N}_i}\exp(\text{LeakyReLU}(a^T[W h_i||W h_k]))}$，其中 $h_i$ 和 $h_j$ 分别是节点 $i$ 和 $j$ 的特征向量，$W$ 是可学习的权重矩阵，$a$ 是注意力机制的可学习参数向量。节点 $i$ 的新特征表示为 $h_i'=\sigma(\sum_{j\in\mathcal{N}_i}\alpha_{ij}W h_j)$。

### GraphSAGE
GraphSAGE（Graph Sample and Aggregate）是一种归纳式的图神经网络，它通过采样和聚合邻居节点的信息来学习节点的嵌入表示，能够处理动态图数据，即可以对未在训练过程中出现的节点进行特征学习。


### GGNN
GGNN将门控循环单元（GRU）的思想引入到图神经网络中，通过门控机制来控制信息在图中的传播，能够更好地捕捉图中的长距离依赖关系。
