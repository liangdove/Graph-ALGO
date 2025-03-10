import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from modules import Vertex, print_matrix

class GraphAdjMat:
    def __init__(self, vertices:list[int], edges:list[list[int]]):
        # 顶点列表，元素代表“顶点值”，索引代表“顶点索引”
        self.vertices: list[int] = []
        # 邻接矩阵，行列索引对应“顶点索引”
        self.adj_mat: list[list[int]] = []
        for val in vertices:
            self.add_vertex(val)
        for e in edges:
            self.add_edge(e[0], e[1])
    
    def size(self):
        return len(self.vertices)
    
    def add_vertex(self, val:int):
        n = self.size()
        self.vertices.append(val)
        new_row = [0] * n
        self.adj_mat.append(new_row)
        for row in self.adj_mat:
            row.append(0)
    
    def remove_vertex(self, index:int):
        if index > self.size():
            raise IndexError()
        self.vertices.pop(index)
        self.adj_mat.pop(index)
        for row in self.adj_mat:
            row.pop(index)
            
    def add_edge(self, i:int, j:int):
        if i < 0 or j < 0 or i > self.size() or j > self.size() or j == i:
            raise IndexError()
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1
        
    def remove_edge(self, i: int, j: int):
        """删除边"""
        # 参数 i, j 对应 vertices 元素索引
        # 索引越界与相等处理
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0
        
    def print(self):
        """打印邻接矩阵"""
        print("顶点列表 =", self.vertices)
        print("邻接矩阵 =")
        print_matrix(self.adj_mat)
