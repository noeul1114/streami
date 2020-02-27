from tkinter import *
import random
import numpy as np
from collections import deque
import os


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def check(elem, list):
    for i in range(len(list)):
        if list[i].x == elem.x and list[i].y == elem.y:
            return True
    return False


class PlayManager3:
    def __init__(self, **kwargs):
        try:
            self.point_list = kwargs['list']
            self.width = kwargs['width']
            self.height = kwargs['height']
            self.limit_gen = kwargs['gen']
        except (ValueError, Exception):
            raise Exception("Incorrect input with kwargs")

        self.grid = np.zeros([self.width, self.height])
        self.grid_pad = np.zeros([self.width+2, self.height+2])

        # counter 설정.
        self.c = 0

        # point list 들 초기화
        self.point_list_temp = deque()
        if not self.point_list:
            self.point_list_init()

        self.tick()

    # main tick function
    def tick(self):
        if self.c != 0:
            # 메인 루프
            self.accumulate()       # 모든 점들에 대해서 neighbor 검사 진행
            self.trim()             # neighbor 이 있는 점들을 기존의 populated 와 empty 로 분리
            self.populated()        # populated 점들에 대해 생존 검사 진행
            self.empty()            # empty 점들에 대해 populated 검사 진행

        self.c += 1
        if self.c == self.limit_gen:                     # 카운터가 10000초에 도달하면 정지.
            print("Counter reached.... Exporting txt file")
            open(os.path.join())
        else:
            self.canvas.after(1, self.tick)

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
                    self.grid_pad[p.x+x+1][p.y+y+1] += 1
            self.grid_pad[p.x+1][p.y+1] -= 1

    # 그리드의 값이 1 이상인 모든 칸을 검사하며,
    # 기존의 Point list 에 존재하지 않는 포인트들 수집
    def trim(self):
        self.point_list_temp = deque()
        for x in range(self.width):
            for y in range(self.height):
                if self.grid_pad[x+1][y+1] > 0:
                    if not check(Point(x,y), self.point_list):
                        self.point_list_temp.append(Point(x,y))

    # Populated 된 점들의 생존 여부를 검사
    def populated(self):
        temp = deque()
        for p in range(len(self.point_list)):
            t = self.point_list.pop()
            x, y = t.x, t.y
            if self.grid_pad[x+1][y+1] <= 1:
                pass
            if self.grid_pad[x+1][y+1] >= 4:
                pass
            if self.grid_pad[x+1][y+1] == 2 or self.grid_pad[x+1][y+1] == 3:
                temp.append(t)
        self.point_list = temp

    # 1 이상의 값을 가지는 모든 empty 점들에 대해서
    # populate 되는지 검사
    def empty(self):
        for p in range(len(self.point_list_temp)):
            t = self.point_list_temp.pop()
            x, y = t.x, t.y

            if self.grid_pad[x+1][y+1] == 3:
                self.point_list.append(t)
