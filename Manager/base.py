from tkinter import *

# 따로 입력이 없을때의 default width/height
width = 80
height = 40


class Manager:
    def __init__(self):
        self.c = 0              # counter 설정.

        self.root = Tk()        # 기본 윈도우 설정
        self.root.title("Streami Back-End assignment")

        # 한칸의 크기는 7*7 이며 각각의 간격은 3픽셀로 하드코딩 되어있음.
        # 이에 따라 맞는 캔버스 크기 설정
        self.canvas = Canvas(self.root,
                             width=width*10+5,
                             height=height*10+5)
        self.canvas.pack()

        # 기본 바탕이 되는 픽셀들 그리기.
        for x in range(width):
            for y in range(height):
                self.canvas.create_rectangle(5+x*10,
                                             5+y*10,
                                             5+x*10+7,
                                             5+y*10+7,
                                             fill='grey')

        self.tick()
        self.root.mainloop()

    # mainloop 내에서 작동되는 작업. 1초마다 카운터를 증가시키며, 시간 간격마다 캔버스를 다시 그림.
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