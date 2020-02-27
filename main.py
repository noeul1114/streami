from tkinter import *
import os
import argparse

# Optional args 추가
parser = argparse.ArgumentParser()
parser.add_argument('text', nargs='?', default="")
parser.add_argument("gen", nargs='?', default="")
args = parser.parse_args()

# args 입력에 따른 플레이 방법 분류
# 기본적으로 입력이 없을 경우 플레이 방법은 1
PLAY_TYPE = 1

# Input txt 파일이 정상적으로 열리는지 확인.
if args.text:
    text_file_dir = os.path.join(os.getcwd(), args.text)
    try:
        file = open(text_file_dir, "r")
    except OSError:
        raise Exception(f"Cannot open file: {args.text}")
    PLAY_TYPE = 2       # 열린다면 2번째 방법으로 플레이

if args.gen:
    print(args.gen)
    PLAY_TYPE = 3       # 세번째 입력이 있다면 3번째 방법으로 플레이


width = 80
height = 40


class Manager:
    def __init__(self):

        root = Tk()
        root.title("Streami Back-End assignment")
        canvas = Canvas(root, width=width*10+5, height=height*10+5)
        canvas.pack()


        for x in range(width):
            for y in range(height):
                canvas.create_rectangle(5+x*10, 5+y*10, 5+x*10+7, 5+y*10+7, fill='grey')
        mainloop()


Manager()