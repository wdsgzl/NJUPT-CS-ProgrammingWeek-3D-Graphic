import time

import rabbit
import dian
import zuiduanlijing
import bfsdfs
# if choice==1:
#       print("1")
#       rabbit.draw()
# # elif choice==2:
choice=0
def switch_case(case_value):
    #switcher = {
        # 1:rabbit.draw(rabbit.verts,rabbit.faces),
        # 2:dian.draw(),
        # 3: "three",
      if case_value == 1:
            rabbit.draw(rabbit.verts, rabbit.faces)
      elif case_value == 2:
            dian.draw()
      elif case_value == 3:
            zuiduanlijing.draw()
      elif case_value == 4:
            bfsdfs.RunDFS(bfsdfs.read())
      elif case_value == 5:
            bfsdfs.read()
            bfsdfs.RunBFS(bfsdfs.read())
      elif case_value == 6:
            exit()




while choice !=6:
      print(
            "1.显示三维图形\n"
            "2.显示第一第二邻接点\n"
            "3.查找最短路径\n"
            "4.进行DFS遍历\n"
            "5.进行BFS遍历\n"
            "6.退出\n"
      "请输入你想执行的操作\n")
      choice = input()
      #time.sleep(3)
      switch_case(int(choice))
      print(chr(27) + "[2J")
      # 输出 "one"
#print(switch_case(4))  # 输出 "nothing"

