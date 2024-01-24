#import huitu
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
dx=[]
dy=[]
dz=[]
x = []
y = []
z = []
sort=[]
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
    judge = int(lines[0])
    index=int(lines[1])
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
        sort.append(i)
        x.append(int(lines[1]))#获取a点
        y.append(int(lines[2]))#获取b点
        z.append(int(lines[3]))#获取c点
        i = i + 1
    def draw():
        j=0
        N1 = []
        N2 = []
        dot = input("请输入想要查找的点序号")
        for ct in x :
            if ct==int(dot) :
                N1.append(int(y[j]))
                N1.append(int(z[j]))
            j=j+1
        j=0
        for ct in y :
            if ct==int(dot) :
                N1.append(int(x[j]))
                N1.append(int(z[j]))
            j=j+1
        j = 0
        for ct in z:
            if ct==int(dot) :
                N1.append(int(y[j]))
                N1.append(int(x[j]))
            j=j+1
        N1 = list(set(N1))
        print("第一邻接点")
        print(N1)
        # print("第一邻接点所在的平面")
        # print(wby)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_axis_off()
        ax.scatter(dx, dy, dz, s=0.1)



        for diyi in N1:
            j = 0
            Ntemp = []
            for ct in x:
                if ct == diyi :
                    N2.append(int(y[j]))
                    N2.append(int(z[j]))
                    Ntemp.append(int(y[j]))
                    Ntemp.append(int(z[j]))
                j = j + 1
            j = 0
            for ct in y:
                if ct == diyi :
                    N2.append(int(x[j]))
                    N2.append(int(z[j]))
                    Ntemp.append(int(x[j]))
                    Ntemp.append(int(z[j]))
                j = j + 1
            j = 0
            for ct in z:
                if ct == diyi :
                    N2.append(int(x[j]))
                    N2.append(int(y[j]))
                    Ntemp.append(int(x[j]))
                    Ntemp.append(int(y[j]))
                j = j + 1

            for j in range(len(Ntemp) - 1):
                if Ntemp[j] not in N1:
                    ax.plot([dx[int(diyi)], dx[int(Ntemp[j])]], [dy[int(diyi)], dy[int(Ntemp[j])]],
                        [dz[int(diyi)], dz[int(Ntemp[j])]],
                        color='g')


        for i in N2:
            if i in N1:
                N2.remove(i)
        N2.sort()
        print("第二邻接点")
        N2 = list(set(N2))
        print(N2)
        for i in range(len(N1) - 1):
            ax.plot([dx[int(dot)], dx[int(N1[i])]],
                    [dy[int(dot)], dy[int(N1[i])]],
                    [dz[int(dot)], dz[int(N1[i])]],
                    color='r')
        plt.show()