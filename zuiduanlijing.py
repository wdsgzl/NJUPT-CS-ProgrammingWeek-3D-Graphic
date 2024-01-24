import operator
import heapq

from matplotlib import pyplot as plt

import lei
import sys
import rabbit

import numpy as np
sys.setrecursionlimit(100000)  #修改最大递归深度
x = []
y = []
z = []
dx=[]
dy=[]
dz=[]
wby=[]
sw=[]
wxx=[]
zcy=[]
sort=[]
already=[]#已经遍历过的
remain=[]#未遍历的
#length=[]#存入的长度

i = 0
try:
    file = open('Bunny.off', 'r')#打开文件
except FileNotFoundError:
    print('File is not found')#若文件不存在则爆错
else:#若文件打开成功则
    count = 0#使用判标跳过OFF头两行文件，方便读取
    judge = 0#使用判标获得3D图形的顶点数
    index = 0#使用判标获得3D图形的面数
    while count < 2:#代码实现跳过OFF文件前两行
        count = count + 1
        lines = file.readline()#读取一行信息
        lines = lines.split()#讲文件中的文本通过空格分隔开，成为独立元素
    #print(lines)
    judge = int(lines[0])
    index=int(lines[1])
    #print(judge)

    while count<2+judge:#代码实现跳过点的定义环节，本部分用于绘图此处无用
        count = count + 1
        lines = file.readline()
        lines = lines.split()
        dx.append(float(lines[0]))#获取a点
        dy.append(float(lines[1]))#获取b点
        dz.append(float(lines[2]))#获取c点

    while count < 2 + judge+index:#代码实现获取邻接点，具体为一个平面分为abc三点，分别获取该面所包含的点

        count = count + 1
        lines = file.readline()
        lines = lines.split()
        #print(lines)
        sort.append(i)
        x.append(float(lines[1]))#获取a点
        y.append(float(lines[2]))#获取b点
        z.append(float(lines[3]))#获取c点
        i = i + 1


    #square=[[0]*judge]*judge
    #print(square)
    # dot=input("请输入想要查找的点序号")
    # N1=[]
    # N2=[]
    N3=[[]for i in range(0,judge)]
    # N4=[]
    # j=0
    # for ct in x:
    #     if ct==int(dot):
    #         N1.append(int(y[j]))
    #         N1.append(int(z[j]))
    #         wby.append([int(x[j]),int(y[j]),int(z[j])])
    #     j=j+1
    # j=0
    # for ct in y:
    #     if ct==int(dot):
    #         N1.append(int(x[j]))
    #         N1.append(int(z[j]))
    #         wby.append([int(x[j]), int(y[j]), int(z[j])])
    #     j=j+1
    # j = 0
    # for ct in z:
    #     if ct==int(dot):
    #         N1.append(int(y[j]))
    #         N1.append(int(x[j]))
    #         wby.append([int(x[j]), int(y[j]), int(z[j])])
    #     j=j+1
    #
    # N1 = list(set(N1))
    # N1.sort()
    # # print("第一邻接点")
    # # print(N1)
    # # print(wby)
    #
    #
    # for diyi in N1:
    #     j = 0
    #
    #     for ct in x:
    #         if ct == diyi:
    #             N2.append(int(y[j]))
    #             N2.append(int(z[j]))
    #             sw.append([int(x[j]), int(y[j]), int(z[j])])
    #         j = j + 1
    #     j = 0
    #     for ct in y:
    #         if ct == diyi:
    #             N2.append(int(x[j]))
    #             N2.append(int(z[j]))
    #             sw.append([int(x[j]), int(y[j]), int(z[j])])
    #         j = j + 1
    #     j = 0
    #     for ct in z:
    #         if ct == diyi:
    #             N2.append(int(x[j]))
    #             N2.append(int(y[j]))
    #             sw.append([int(x[j]), int(y[j]), int(z[j])])
    #         j = j + 1
    #     #print(j)
    # # print("第二邻接点")
    # N2=list(set(N2))
    # N2.sort()


    # print(N2)
    # print(sw)
    #print(x)
    #print(y)
    #print(z)

    #对每个三角形的数据进行遍历，求得各点的邻接点，存入二维列表N3
    j=0
    for ct in x:
            N3[int(ct)].append(int(y[j]))
            N3[int(ct)].append(int(z[j]))
            j = j + 1
    j = 0
    for ct in y:
            N3[int(ct)].append(int(x[j]))
            N3[int(ct)].append(int(z[j]))
            j = j + 1

    j = 0
    for ct in z:
            N3[int(ct)].append(int(y[j]))
            N3[int(ct)].append(int(x[j]))
            j = j + 1
    l=0
    #整理N3,去除重复元素
    for k in range(judge):
      N3[l] = list(set(N3[l]))
      l=l+1
    #print(N3[0])
    count=0
    length=[int(10000)]*judge
    measure =[int(10000)] * judge


    # min_index=int(input("请输入你要查找最短路径的点"))
    # i = 0
    # already.append(min_index)
    #
    # for count in range(judge):
    #
    #
    #     for j in N3[min_index]:
    #         print(N3[min_index])
    #
    #
    #
    #         if j not in already:
    #
    #
    #             #计算距离
    #             lengthx =abs((float(lei.D[min_index].x) - float(lei.D[j].x)) * (float(lei.D[min_index].x) - float(lei.D[j].x)))
    #             lengthy=abs((float(lei.D[min_index].y)-float(lei.D[j].y))*(float(lei.D[min_index].x)-float(lei.D[j].x)))
    #             lengthz=abs((float(lei.D[min_index].z)-float(lei.D[j].z))*(float(lei.D[min_index].z)-float(lei.D[j].z)))
    #             #length[i][j]=[(float(lei.D[i].x)-float(lei.D[j].x))*(float(lei.D[i].x)-float(lei.D[j].x))+(float(lei.D[i].y)-float(lei.D[j].y))*(lei.D[i].y-lei.D[j].y)+(lei.D[i].z-lei.D[j].z)*(lei.D[i].z-lei.D[j].z)]
    #
    #             #计算长度
    #             if length[min_index]!= int(10000):
    #                 lengthl = length[min_index]+length[i]+(lengthx + lengthy + lengthz)**0.5
    #             else:
    #                 lengthl = length[i] + (lengthx + lengthy + lengthz) ** 0.5
    #             if lengthl<=measure[j]:
    #             # Lin = {i: np.nonzero(row)[0].tolist() for i,row in enumerate(sort)}
    #
    #                 #print(lengthl)
    #                 measure[j]=lengthl
    #
    #                 length[j]=measure[j]
    #
    #     length[min_index]=10000
    #     min_index=np.argmin(length)
    #     min_number =min(length)
    #     already.append(min_index)
    #     #print()
    #     print(already)
    #     length[min_index]=0
    # print(length)
    #     #print(min_index,min_number)


    # x = [3, 2.2, 7.4, 6, 4]
    # min_index, min_number = min(enumerate(x), key=operator.itemgetter(1))
    # # 输出 1   2.2
    #
    # max_index, max_number = max(enumerate(x), key=operator.itemgetter(1))
    # # 输出 2   7.4

    #print(length)
        #
    # print(Lin)
    #
    # sw1=[]*judge        #DFS/BFS:判定下个节点是否已经遍历过的辅助列表5
    # sw2 = [] * judge    #DFS/BFS:序列列表
    # sw3=[]              #BFS:待遍历列表
    # step=-1             #BFS:广度遍历索引
    # def DFS(list1,val):
    #     global sw1,sw2
    #     for ev in list1[val]:
    #          sw1.append(ev)
    #          if len(sw1) == len(list(set(sw1))):    #判定下个节点是否已经遍历过
    #            sw2.append(ev)
    #            DFS(list1,ev)
    #          else:
    #            sw1=list(set(sw1))                   #在辅助列表中将已被遍历的节点去重
    #
    #
    # def BFS(list1,val):
    #     global sw1,sw2,step
    #     step=step+1                           #每次递归推进待遍历列表索引
    #     sw1.append(val)
    #     if len(sw1) == len(list(set(sw1))):   #判断该节点是否已经遍历过
    #       sw2.append(val)                     #储存当前节点值
    #       for ev in list1[val]:               #将当前节点的所有邻接点加入待遍历列表
    #         sw3.append(ev)
    #     else:
    #         sw1 = list(set(sw1))              #在辅助列表中将已被遍历的节点去重
    #     while step+1<len(sw3):                #遍历完所有待遍历节点
    #         BFS(list1,sw3[step])
    #
    # # DFS启动！
    # sw1.append(int(dot))         #第一次递归设置列表初值
    # sw2.append(int(dot))
    # DFS(N3,int(dot))
    # print(sw2)
    # print(len(sw2))
    #
    # #BFS启动！
    # #BFS(N3,int(dot))               #第一次递归设置列表初值
    # #print(sw2)
    # #print(len(sw2))

#     class Graph:
#         def __init__(self):
#             self.edges = {}
#
#         def add_edge(self, from_vertex, to_vertex, weight):
#             # 确保顶点存在于图中
#             if from_vertex not in self.edges:
#                 self.edges[from_vertex] = []
#             if to_vertex not in self.edges:
#                 self.edges[to_vertex] = []
#
#             # 添加边
#             self.edges[from_vertex].append((to_vertex, weight))
#
#         def dijkstra(self, start_vertex):
#             # 初始化距离表，所有顶点距离为无穷大
#             verts=[]
#             distances = {vertex: float('infinity') for vertex in self.edges}
#             # 起始顶点到自身的距离为0
#             distances[start_vertex] = 0
#
#             # 优先队列初始化
#             pq = [(0, start_vertex)]
#             while len(pq) > 0:
#                 current_distance, current_vertex = heapq.heappop(pq)
#                 #verts.append(current_vertex)
#                 # 如果当前处理的顶点距离大于已知最短距离，则跳过
#                 if current_distance > distances[current_vertex]:
#                     continue
#
#                 # 遍历当前顶点的邻接顶点
#                 for neighbor, weight in self.edges.get(current_vertex, []):
#                     distance = current_distance + weight
#
#                     # 如果计算出的距离小于已知距离，则更新距离表
#                     if distance < distances[neighbor]:
#                         distances[neighbor] = distance
#                         heapq.heappush(pq, (distance, neighbor))
#                         verts.append(neighbor)
#             print(verts)
#             return distances
#
#         # def shortest_path(self, start_vertex, end_vertex):
#         #     distances, previous_vertices = self.dijkstra(start_vertex)
#         #     path = []
#         #     current_vertex = end_vertex
#         #     while current_vertex is not None:
#         #         path.append(current_vertex)
#         #         current_vertex = previous_vertices[current_vertex]
#         #     path = path[::-1]  # Reverse the list
#         #     return path, distances[end_vertex]
#
# #    lengthx = (abs((float(lei.D[i].x) - float(lei.D[j].x)) * (float(lei.D[i].x) - float(lei.D[j].x)))+lengthy=abs((float(lei.D[i].y)-float(lei.D[j].y))*(float(lei.D[i].x)-float(lei.D[j].x)))+lengthz=abs((float(lei.D[i].z)-float(lei.D[j].z))*(float(lei.D[i].z)-float(lei.D[j].z))))
#
#
#     # 示例使用
#     start=input("请输入你想查找的最短路径开始点")
#     end=input("请输入你想查找的最短路径结束点")
#
#     graph = Graph()
#     for i in range(judge):
#         for j in N3[i]:
#             #graph.add_edge("A", "B", (abs((float(lei.D[i].x) - float(lei.D[j].x)) * (float(lei.D[i].x) - float(lei.D[j].x)))+abs((float(lei.D[i].y)-float(lei.D[j].y))*(float(lei.D[i].x)-float(lei.D[j].x)))+abs((float(lei.D[i].z)-float(lei.D[j].z))*(float(lei.D[i].z)-float(lei.D[j].z))))**0.5)
#             graph.add_edge(f"{i}", f"{j}", (abs((float(lei.D[i].x) - float(lei.D[j].x)) * (float(lei.D[i].x) - float(lei.D[j].x)))+abs((float(lei.D[i].y)-float(lei.D[j].y))*(float(lei.D[i].x)-float(lei.D[j].x)))+abs((float(lei.D[i].z)-float(lei.D[j].z))*(float(lei.D[i].z)-float(lei.D[j].z))))**0.5)
#     start_vertex = f'{start}'
#     # distances = graph.dijkstra(start)
#     # path, distance = graph.shortest_path(start_vertex, end_vertex)
#     #print(f"The shortest distances from {start} to {end}  vertices are: {distances}")
#     print(f"The shortest distances from {start} to {end}  length are: {distances[end]}")



class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        if to_vertex not in self.edges:
            self.edges[to_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))

    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.edges}
        previous_vertices = {vertex: None for vertex in self.edges}
        distances[start_vertex] = 0
        pq = [(0, start_vertex)]
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))
        return distances, previous_vertices

    def shortest_path(self, start_vertex, end_vertex):
        distances, previous_vertices = self.dijkstra(start_vertex)
        path = []
        current_vertex = end_vertex
        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path = path[::-1]
        return path, distances[end_vertex]
def draw():
    graph = Graph()
    start=input("请输入你想查找的最短路径开始点")
    end=input("请输入你想查找的最短路径结束点")
    for i in range(judge):
            for j in N3[i]:
                 #graph.add_edge("A", "B", (abs((float(lei.D[i].x) - float(lei.D[j].x)) * (float(lei.D[i].x) - float(lei.D[j].x)))+abs((float(lei.D[i].y)-float(lei.D[j].y))*(float(lei.D[i].x)-float(lei.D[j].x)))+abs((float(lei.D[i].z)-float(lei.D[j].z))*(float(lei.D[i].z)-float(lei.D[j].z))))**0.5)
                 graph.add_edge(f"{i}", f"{j}", (abs((float(lei.D[i].x) - float(lei.D[j].x)) * (float(lei.D[i].x) - float(lei.D[j].x)))+abs((float(lei.D[i].y)-float(lei.D[j].y))*(float(lei.D[i].x)-float(lei.D[j].x)))+abs((float(lei.D[i].z)-float(lei.D[j].z))*(float(lei.D[i].z)-float(lei.D[j].z))))**0.5)


    start_vertex = f'{start}'
    end_vertex = f'{end}'
    path, distance = graph.shortest_path(start_vertex, end_vertex)

    print(f"从 {start_vertex} 开始到 {end_vertex} 的最短路径是: {path}")
    print(f"最短路径长度是: {distance}")
    #print(dx)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off()
    ax.scatter(dx, dy, dz,s=1)
    for i in range(len(path)-1):
          ax.plot([dx[int(path[i])], dx[int(path[i+1])]], [dy[int(path[i])], dy[int(path[i+1])]], [dz[int(path[i])], dz[int(path[i+1])]], color='r')
    ax.view_init(elev=10., azim=i)
    plt.show()








