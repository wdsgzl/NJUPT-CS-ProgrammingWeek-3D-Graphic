
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import pandas as pd
from bs4 import element
import matplotlib.pyplot as mp
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import sys
sys.setrecursionlimit(10000000)  #修改最大递归深度
dx=[]
dy=[]
dz=[]
x = []
y = []
z = []
wby=[]
sw=[]
wxx=[]
zcy=[]
sort=[]
dui=[]
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
    #verts = [[float(s) for s in file.readline().strip().split(' ')] for i_vert in range(index)]
    while count<2+judge:#代码实现跳过点的定义环节，本部分用于绘图此处无用
        count = count + 1
        lines = file.readline()
        lines = lines.split()
        #dui.append(i)
        dx.append(float(lines[0]))#获取a点
        dy.append(float(lines[1]))#获取b点
        dz.append(float(lines[2]))#获取c点
        #i=i+1
    #i=0
    while count < 2 + judge+index:#代码实现获取邻接点，具体为一个平面分为abc三点，分别获取该面所包含的点

        count = count + 1
        lines = file.readline()
        lines = lines.split()
        #print(lines)
        sort.append(i)
        x.append(int(lines[1]))#获取a点
        y.append(int(lines[2]))#获取b点
        z.append(int(lines[3]))#获取c点
        i = i + 1

    #square=[[0]*judge]*judge
    #print(square)
    dot=input("请输入想要查找的点序号")
    N1=[]
    N2=[]
    #N3=[]
    #N4=[]
    #N5=[]
    
    j=0
    for ct in x :
        if ct==int(dot) :
            N1.append(int(y[j]))
            N1.append(int(z[j]))
            #verts.append([int(dx[ct]),int(dy[ct]),int(dz[ct])])
            #wby.append([int(x[j]),int(y[j]),int(z[j])])
        j=j+1
    j=0
    for ct in y :
        if ct==int(dot) :
            N1.append(int(x[j]))
            N1.append(int(z[j]))
            #wby.append([int(x[j]), int(y[j]), int(z[j])])
        j=j+1
    j = 0
    for ct in z:
        if ct==int(dot) :
            N1.append(int(y[j]))
            N1.append(int(x[j]))
            #wby.append([int(x[j]), int(y[j]), int(z[j])])
        j=j+1

        #verts = [[float(s) for s in file.readline().strip().split(' ')] for i_vert in range(n_verts)]
        #faces = [[int(s) for s in file.readline().strip().split(' ')][1:] for i_face in range(n_faces)]
    N1 = list(set(N1))
    #N1.sort()
    #wby = np.array(wby)
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.add_collection3d(Poly3DCollection(huitu.verts[wby]))
    print("第一邻接点")
    print(N1)
    # print("第一邻接点所在的平面")
    # print(wby)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off()
    # ax.scatter(dx, dy, dz, s=0.1)



    for diyi in N1:
        j = 0
        Ntemp = []
        for ct in x:
            if ct == diyi :
                N2.append(int(y[j]))
                N2.append(int(z[j]))
                Ntemp.append(int(y[j]))
                Ntemp.append(int(z[j]))
                #wby.append([int(x[j]), int(y[j]), int(z[j])])
                #sw.append([int(x[j]), int(y[j]), int(z[j])])
            j = j + 1
        j = 0
        for ct in y:
            if ct == diyi :
                N2.append(int(x[j]))
                N2.append(int(z[j]))
                Ntemp.append(int(x[j]))
                Ntemp.append(int(z[j]))
                #wby.append([int(x[j]), int(y[j]), int(z[j])])
                #sw.append([int(x[j]), int(y[j]), int(z[j])])
            j = j + 1
        j = 0
        for ct in z:
            if ct == diyi :
                N2.append(int(x[j]))
                N2.append(int(y[j]))
                Ntemp.append(int(x[j]))
                Ntemp.append(int(y[j]))
                #wby.append([int(x[j]), int(y[j]), int(z[j])])
                #sw.append([int(x[j]), int(y[j]), int(z[j])])
            j = j + 1
        #print(j)

        # for j in range(len(Ntemp) - 1):
        #     if Ntemp[j] not in N1:
        #         ax.plot([dx[int(diyi)], dx[int(Ntemp[j])]], [dy[int(diyi)], dy[int(Ntemp[j])]],
        #             [dz[int(diyi)], dz[int(Ntemp[j])]],
        #             color='g')


    for i in N2:
        if i in N1:
            N2.remove(i)
    N2.sort()
    print("第二邻接点")
    N2 = list(set(N2))
    print(N2)
    # for i in range(len(N1) - 1):
    #     ax.plot([dx[int(dot)], dx[int(N1[i])]],
    #             [dy[int(dot)], dy[int(N1[i])]],
    #             [dz[int(dot)], dz[int(N1[i])]],
    #             color='r')
    # plt.show()

    N3=[[]for i in range(0,judge)]
    # 对每个三角形的数据进行遍历，求得各点的邻接点，存入二维列表N3
    j = 0
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
    l = 0
    # 整理N3,去除重复元素
    for k in range(judge):
        N3[l] = list(set(N3[l]))
        l = l + 1
    print(N3[int(dot)])

    sw1 = [] * judge  # DFS/BFS:判定下个节点是否已经遍历过的辅助列表
    sw2 = [] * judge  # DFS/BFS:序列列表
    sw3 = []  # BFS:待遍历列表
    step = -1  # BFS:广度遍历索引


    def DFS(list1, val):
        global sw1, sw2
        for ev in list1[val]:
            sw1.append(ev)
            if len(sw1) == len(list(set(sw1))):  # 判定下个节点是否已经遍历过
                sw2.append(ev)
                DFS(list1, ev)
            else:
                sw1 = list(set(sw1))  # 在辅助列表中将已被遍历的节点去重


    def BFS(list1, val):
        global sw1, sw2, step
        step = step + 1  # 每次递归推进待遍历列表索引
        sw1.append(val)
        if len(sw1) == len(list(set(sw1))):  # 判断该节点是否已经遍历过
            sw2.append(val)  # 储存当前节点值
            for ev in list1[val]:  # 将当前节点的所有邻接点加入待遍历列表
                sw3.append(ev)
        else:
            sw1 = list(set(sw1))  # 在辅助列表中将已被遍历的节点去重
        while step + 1 < len(sw3):  # 遍历完所有待遍历节点
            BFS(list1, sw3[step])

    # #DFS启动！
    # sw1.append(int(dot))         #第一次递归设置列表初值
    # sw2.append(int(dot))
    # DFS(N3,int(dot))
    #
    #BFS启动！
    BFS(N3,int(dot))               #第一次递归设置列表初值

    j=0
    count=0
    for j in range(len(sw2)-1):
        check_list=N3[sw2[j+1]]
        check_list.append(sw2[j])
        if not(len(list(set(check_list)))==len(N3[sw2[j+1]])):
            count = count + 1
            ax.plot([dx[int(sw2[j])],dx[int(sw2[j+1])]],[dy[int(sw2[j])],dy[int(sw2[j+1])]],[dz[int(sw2[j])],dz[int(sw2[j+1])]],color='g')
            if count %100==0:
                plt.draw()
                plt.pause(0.00000000000000000001)
        # print(sw2[j])
        # print(sw2[j+1])
    plt.show()


