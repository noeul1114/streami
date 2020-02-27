import os
import argparse
import time

from Manager import base

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


if __name__ == "__main__":

    if PLAY_TYPE == 1:
        base.Manager()
    elif PLAY_TYPE == 2:
        pass
    elif PLAY_TYPE == 3:
        pass
