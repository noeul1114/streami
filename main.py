import os
import argparse

from Manager.base import Manager, Point
from collections import deque

# Optional args 추가
parser = argparse.ArgumentParser()
parser.add_argument('text', nargs='?', default="")
parser.add_argument("gen", nargs='?', default="")
args = parser.parse_args()

# args 입력에 따른 플레이 방법 분류
# 기본적으로 입력이 없을 경우 플레이 방법은 1
PLAY_TYPE = 1

initial_cell_list = deque()
NUM_ROWS, NUM_COLS = 80, 40

# Input txt 파일이 정상적으로 열리는지 확인.
if args.text:
    text_file_dir = os.path.join(os.getcwd(), args.text)
    try:
        file = open(text_file_dir, "r")
    except (FileExistsError, OSError):
        raise Exception(f"Cannot open file: {args.text}")

    PLAY_TYPE = 2  # 열린다면 2번째 방법으로 플레이

    # 첫번째 줄의 NUM_COLS, NUM_ROWS 추출
    tmp = file.readline()
    tmp = tmp.split(" ")
    NUM_COLS, NUM_ROWS = int(tmp[0]), int(tmp[1].rstrip())

    # 두번째 줄의 NUM_CELLS_INIT
    tmp = file.readline()
    NUM_CELLS_INIT = int(tmp.rstrip())

    # 세번째 줄부터 Point 객체를 만들어 initial_list에 append
    for i in range(NUM_CELLS_INIT):
        tmp = file.readline()
        tmp = tmp.split(" ")
        initial_cell_list.append(Point(int(tmp[0]), int(tmp[1].rstrip())))

if args.gen:
    PLAY_TYPE = 3       # 세번째 입력이 있다면 3번째 방법으로 플레이
    GENERATION = args.gen

if __name__ == "__main__":

    if PLAY_TYPE == 1:
        Manager()
    elif PLAY_TYPE == 2:
        # print('PLAY_TYPE = 2')
        Manager(list=initial_cell_list, width=NUM_ROWS, height=NUM_COLS)
    elif PLAY_TYPE == 3:
        print('PLAY_TYPE = 3')
