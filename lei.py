import numpy

class Dot(object):
    class Struct(object):
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    def __init__(self):
        self.z = None
        self.y = None
        self.x = None

    def make_struct(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return self.Struct(x, y, z)

    def show(self):
        print([self.x, self.y, self.z])


# D=Dot[10]
# D.show()


a = []
b = []
c = []
try:
    file = open('Bunny.off', 'r')  # 打开文件
except FileNotFoundError:
    print('File is not found')  # 若文件不存在则爆错
else:  # 若文件打开成功则
    count = 0  # 使用判标跳过OFF头两行文件，方便读取
    judge = 0  # 使用判标获得3D图形的顶点数
    index = 0  # 使用判标获得3D图形的面数
    while count < 2:  # 代码实现跳过OFF文件前两行
        count = count + 1
        lines = file.readline()  # 读取一行信息
        lines = lines.split()  # 讲文件中的文本通过空格分隔开，成为独立元素
    # print(lines)
    judge = int(lines[0])
    # index=int(lines[1])
    # print(judge)

    while count < 2 + judge:  # 代码实现跳过点的定义环节，本部分用于绘图此处无用
        count = count + 1
        lines = file.readline()
        lines = lines.split()
        a.append(lines[0])
        b.append(lines[1])
        c.append(lines[2])
    # print(a)
    D = [Dot() for i in range(0, judge)]
    for i in range(0, judge):
        D[i].x = a[i]
        D[i].y = b[i]
        D[i].z = c[i]

    #print(D[judge-1].x)

