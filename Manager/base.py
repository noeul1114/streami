from tkinter import *
import random
import numpy as np
from collections import deque


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def check(elem, list):
    for i in range(len(list)):
        if list[i].x == elem.x and list[i].y == elem.y:
            return True
    return False


class Manager:
    def __init__(self, **kwargs):
        try:
            self.point_list = kwargs['list']
            self.width = kwargs['width']
            self.height = kwargs['height']
        except:
            self.point_list = None
            self.width = 80
            self.height = 40
        self.grid = np.zeros([self.width,self.height])
        self.grid_pad = np.zeros([self.width+2,self.height+2])

        self.point_list_temp = deque()

        self.c = 0              # counter 설정.

        self.root = Tk()        # 기본 윈도우 설정
        self.root.title("Streami Back-End assignment")

        # 한칸의 크기는 7*7 이며 각각의 간격은 3픽셀로 하드코딩 되어있음.
        # 이에 따라 맞는 캔버스 크기 설정
        self.canvas = Canvas(self.root,
                             width=self.width*10+5,
                             height=self.height*10+5)
        self.canvas.pack()

        # 기본 바탕이 되는 픽셀들 그리기.
        for x in range(self.width):
            for y in range(self.height):
                self.canvas.create_rectangle(5 + x * 10,
                                             5 + y * 10,
                                             5 + x * 10 + 7,
                                             5 + y * 10 + 7,
                                             fill='grey')
        if self.point_list:
            pass
        else:
            self.point_list_init()

        # 초기화된, 혹은 입력받은 point_list로 캔버스 덮어씌우기.
        if self.point_list:
            for i in range(len(self.point_list)):
                self.grid[self.point_list[i].x][self.point_list[i].y] = 1

                self.canvas.create_rectangle(
                    self.point_list[i].x * 10 + 5,
                    self.point_list[i].y * 10 + 5,
                    self.point_list[i].x * 10 + 12,
                    self.point_list[i].y * 10 + 12,
                    fill="red")
        self.tick()
        self.root.mainloop()

    # main tick function
    def tick(self):
        self.canvas.create_rectangle(5+self.c*10,
                                     5+self.c*10,
                                     5+self.c*10+7,
                                     5+self.c*10+7,
                                     fill='red')

        self.accumulate()
        self.trim()


        self.c += 1
        if self.c == 10000:                     # 카운터가 10000초에 도달하면 정지.
            print(f"Counter {self.c} reached.")
        else:
            self.canvas.after(1000, self.tick)

    # point_list 가 존재하지 않을때 random initialize 하는 함수
    def point_list_init(self):
        self.point_list = deque()

        for x in range(self.width):
            for y in range(self.height):
                if random.random() < 0.5:
                    self.point_list.append(Point(x,y))

    # Populated point 들을 중심으로 주변 값들에 +1 씩 누적하는 프로세스
    def accumulate(self):
        self.grid_pad = np.zeros([self.width+2,self.height+2])
        for p in self.point_list:
            for x in range(-1,2):
                for y in range(-1,2):
                    print(x,y)
                    self.grid_pad[p.x+x+1][p.y+y+1] += 1
            self.grid_pad[p.x+1][p.y+1] -= 1

    def trim(self):
        self.point_list_temp = deque()
        for x in range(self.width):
            for y in range(self.height):
                if self.grid_pad[x+1][y+1] > 0:
                    if not check(Point(x,y), self.point_list):
                        self.point_list_temp.append(Point(x,y))


