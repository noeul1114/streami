from tkinter import *


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

        # 입력받은 point_list 가 존재한다면 해당 값들을 초기화.
        if self.point_list:
            for i in range(len(self.point_list)):
                print(self.point_list[i].x, self.point_list[i].y)
                self.canvas.create_rectangle(
                    self.point_list[i].x * 10 + 5,
                    self.point_list[i].y * 10 + 5,
                    self.point_list[i].x * 10 + 12,
                    self.point_list[i].y * 10 + 12,
                    fill="red")

        if self.point_list:
            self.tick_with_init()
        else:
            self.tick_random()
        self.root.mainloop()

    # mainloop 내에서 작동되는 작업. 1초마다 카운터를 증가시키며, 시간 간격마다 캔버스를 다시 그림.
    def tick_random(self):
        self.canvas.create_rectangle(5+self.c*10,
                                     5+self.c*10,
                                     5+self.c*10+7,
                                     5+self.c*10+7,
                                     fill='red')
        self.c += 1
        if self.c == 10000:
            print(f"Counter {self.c} reached.")
        else:
            self.canvas.after(1000, self.tick_random)

    def tick_with_init(self):
        self.canvas.create_rectangle(5+self.c*10,
                                     5+self.c*10,
                                     5+self.c*10+7,
                                     5+self.c*10+7,
                                     fill='red')
        self.c += 1
        if self.c == 10000:
            print(f"Counter {self.c} reached.")
        else:
            self.canvas.after(1000, self.tick_with_init)