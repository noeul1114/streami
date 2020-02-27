from tkinter import *
import random
import numpy as np
from collections import deque


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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
        self.grid = np.zeros([80,40])

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
        print(self.grid)
        self.tick()
        self.root.mainloop()

    # main tick function
    def tick(self):
        self.canvas.create_rectangle(5+self.c*10,
                                     5+self.c*10,
                                     5+self.c*10+7,
                                     5+self.c*10+7,
                                     fill='red')
        self.c += 1
        if self.c == 10000:
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