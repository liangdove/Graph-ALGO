import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import Vertex, vals_to_vets

class GraphAdjList:
    def __init__(self, edges:list[list[Vertex]]):
        self.adj_list = dict[Vertex, list[Vertex]]()
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])
            
    def size(self):
        return len(self.adj_list)
            
    def add_vertex(self, vet:Vertex):
        if vet in self.adj_list:
            return
        self.adj_list[vet] = []
        
    def remove_vertex(self, vet: Vertex):
        if vet not in self.adj_list:
            raise ValueError()
        # 在邻接表中删除顶点 vet 对应的链表
        self.adj_list.pop(vet)
        # 遍历其他顶点的链表，删除所有包含 vet 的边
        for vertex in self.adj_list:
            if vet in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vet)
    
    
    def add_edge(self, vet_i:Vertex, vet_j:Vertex):
        if vet_i not in self.adj_list or vet_j not in self.adj_list or vet_j == vet_i:
            raise ValueError()
        self.adj_list[vet_i].append(vet_j)
        self.adj_list[vet_j].append(vet_i)
        
    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError()
        # 删除边 vet1 - vet2
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)
        
    def print(self):
        """打印邻接表"""
        print("邻接表 =")
        for vertex in self.adj_list:
            tmp = [v.val for v in self.adj_list[vertex]]
            print(f"{vertex.val}: {tmp},")

import deque
def graph_bfs(graph:GraphAdjList, start_vet:Vertex) -> list[Vertex]:
    res = []
    visited = set[Vertex]([start_vet])
    que = deque[Vertex]([start_vet])
    while len(que) > 0:
        vet = que.popleft()
        res.append(vet)
        for adj_vet in graph.adj_list[vet]:
            if adj_vet in visited:
                continue
            que.append(adj_vet)
            visited.add(adj_vet)
    return res

def dfs(graph:GraphAdjList, visited:set[Vertex], res:list[Vertex], vet:Vertex):
    res.append(vet)
    visited.add(vet)
    for adj_vet in graph.adj_list[vet]:
        if adj_vet in visited:
            continue
        dfs(graph, visited, res, adj_vet)

def graph_dfs(graph:GraphAdjList, start_vet:Vertex) -> list[Vertex]:
    res = []
    visited = set[Vertex]([start_vet])
    dfs(graph, visited, res, start_vet)
    return res


"""Driver Code"""
if __name__ == "__main__":
    # 初始化无向图
    v = vals_to_vets([1, 3, 2, 5, 4])
    edges = [
        [v[0], v[1]],
        [v[0], v[3]],
        [v[1], v[2]],
        [v[2], v[3]],
        [v[2], v[4]],
        [v[3], v[4]],
    ]
    graph = GraphAdjList(edges)
    print("\n初始化后，图为")
    graph.print()

    # 添加边
    # 顶点 1, 2 即 v[0], v[2]
    graph.add_edge(v[0], v[2])
    print("\n添加边 1-2 后，图为")
    graph.print()

    # 删除边
    # 顶点 1, 3 即 v[0], v[1]
    graph.remove_edge(v[0], v[1])
    print("\n删除边 1-3 后，图为")
    graph.print()

    # 添加顶点
    v5 = Vertex(6)
    graph.add_vertex(v5)
    print("\n添加顶点 6 后，图为")
    graph.print()

    # 删除顶点
    # 顶点 3 即 v[1]
    graph.remove_vertex(v[1])
    print("\n删除顶点 3 后，图为")
    graph.print()
 
        