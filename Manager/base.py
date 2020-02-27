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
        self.draw_base_grid()

        if self.point_list:
            pass
        else:
            self.point_list_init()

        # 초기화된, 혹은 입력받은 point_list로 캔버스 덮어씌우기.
        self.draw_point()

        self.tick()
        self.root.mainloop()

    # main tick function
    def tick(self):
        if self.c != 0:
            self.accumulate()
            self.trim()
            self.populated()
            self.empty()

            self.redraw()

        self.c += 1
        if self.c == 10000:                     # 카운터가 10000초에 도달하면 정지.
            print(f"Counter {self.c} reached.")
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
        temp = deque()
        for p in range(len(self.point_list_temp)):
            t = self.point_list_temp.pop()
            x, y = t.x, t.y

            if self.grid_pad[x+1][y+1] == 3:
                self.point_list.append(t)

    # 최종적으로 다음 generation 의 Point 들을 기반으로 캔버스를 다시 그리기
    def redraw(self):
        self.canvas.delete(ALL)

        self.draw_base_grid()
        self.draw_point()

    # 베이스가 되는 그리드 그리기
    def draw_base_grid(self):
        for x in range(self.width):
            for y in range(self.height):
                self.canvas.create_rectangle(5 + x * 10,
                                             5 + y * 10,
                                             5 + x * 10 + 9,
                                             5 + y * 10 + 9,
                                             fill='grey',
                                             outline='white',
                                             width=0.0)

    # point list 를 기반으로 populated 포인트들을 그리기
    def draw_point(self):
        if self.point_list:
            for i in range(len(self.point_list)):
                self.grid[self.point_list[i].x][self.point_list[i].y] = 1

                self.canvas.create_rectangle(
                    self.point_list[i].x * 10 + 5,
                    self.point_list[i].y * 10 + 5,
                    self.point_list[i].x * 10 + 14,
                    self.point_list[i].y * 10 + 14,
                    fill="red",
                    outline='white',
                    width=0.0)