# Streami BE dev assignment : Park Hyung Seok
Conway's Game of Life 구현

#### Windows 10 Pro + Docker Ubuntu 16.04 based Container
![Result](https://media.giphy.com/media/lS21FOMtJqrN2smc47/giphy.gif)
<br>

#### Ubuntu 18.04 Bionic Beaver + Docker Ubuntu 16.04 based Container
![Result](https://media.giphy.com/media/Qy2sMWHkPHgGAwpFzl/giphy.gif)


해당 과제를 수행하는데 사용한 스택은 아래와 같습니다.

- Python
    - Tkinter
    - Numpy
- Docker


Windows Host, Ubuntu 18.04 위에서 Ubuntu 16.04로 돌아가는 Docker 시스템을 통해 코딩 및 디버깅을 하였습니다.

Windows Host 환경에서는 Xming 소프트웨어를 통하여 GUI 환경을 테스트 했습니다.

<br>
<br>

Overview
---------

이런 고민을 하고 구현했습니다.

1. 어떤 언어를 사용할 것인가?
2. 어떤 GUI 패키지를 사용할 것인가?
3. Docker 를 사용할 것인가? 바로 Host 에서 돌릴 것인가?
4. 알고리즘 구현은 어떤 방식으로 할 것인가?

개인적으로 가장 친숙한 언어는 Python 이기 때문에 주저없이 Python을 골랐습니다.

GUI 패키지는 Qt, Tkinter, Kivy 세가지 선택지 중에서 고민을 했습니다. 결과적으로 Python 자체에 구축되어있는 Tkinter 를 사용하는 것이 
최종 결과를 돌리는 Host 컴퓨터에서 안정적으로  돌릴 수 있는 옵션이라 생각했습니다.

두 번째와 같은 이유로 Docker 기반의 환경 구축이 필요하다 생각했고, 따로 16.04 이미지를 기반으로 격리된 환경을 구축했습니다. 자세한 내용은 
Dockerfile 내부를 참고하여 주십시요.

핵심 알고리즘 구현은 
1. argparse 통해 초기입력 유무검사

2. 초기입력에 실행방법 분기

3. 초기입력에 따른 0 generation 패턴 그리드 그리기

4. 아래의 내용을 반복
   - **width+2, height+2 의 크기를 가지는 padding 그리드**를 numpy.zero 로 생성
   - 각 point 좌표들의 8-neighbor 에 대해 점수를 **1점씩 추가**
   - grid_pad 내부에서 기존 grid 의 부분에 대한 좌표 전수검사
   - 전수검사를 통해 1점 이상의 점수를 얻은 포인트들의 List 획득
   - 1점 이상의 포인트들을 기존 Populated 되어있던 포인트와 Empty 포인트로 분류
   - Game of Life 규칙에 따라 각각의 포인트들의 생존/부활 여부 확인
   - 최종적인 다음 Generation 포인트 좌표들을 획득
   - 좌표들을 기반으로 그리드 redraw
   
   ++ 총 세가지 방법으로 구동할 수 있어야 하는데, 세번째 방법은 위의 알고리즘에서 시각화 코드만 제외하고 구동하는 형식으로 구현하였습니다.
   ++ 주요 알고리즘 코드는 Manager 패키지 안의 **base.py** 그리고 세번째 방법 구동 코드는 **play3.py** 에 구현되어 있습니다.
   
<br>
<br>

<hr>

## 구동방법

Ubuntu 환경
---

```
git clone https://github.com/noeul1114/streami.git
```
명령어를 통해 Repo를 복사한 이후, 
<br>

```
chmod +x init.sh
```

를 통해 init 파일을 실행가능하도록 설정한 이후, <br>

```
./init.sh
```
 코드 실행을 통해 해당 파일을 실행시켜주시면 됩니다.
 
 해당 sh 파일은 아래와 같이 구성되어 있습니다.
 
```
#!/usr/bin/env bash
xhost +local:

sudo docker container run -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY willypower/streami:latest bash
```
로컬에서의 xhost 접근을 허용하는 동시에, Docker hub 에 업로드 되어있는 빌드 이미지를 통해 컨테이너를 실행시키게 됩니다.

Docker Host 에서 컨테이너 내부의 GUI 어플리케이션을 구동하기 위한 볼륨을 설정하고, 컨테이너 내부의 디스플레이 환경변수를 호스트와 동기화시킵니다.

실행이 별다른 오류 없이 되었다면, 아래의 커맨드를 통해 프로그램을 구동시킬 수 있습니다.

**!! 위의 sh 파일은 Docker 가 HOST 에 설치되어 있으며 구동중이라는 가정하에 적었습니다.**

```
python3 main.py
python3 main.py plus.txt
python3 main.py plux.txt 10
``` 


Windows 환경
---


Xming이 설치되어있고, 구동중이어야 합니다.

내부 ip를 아래 코드의 <HOST_IP> 에 수정하여 넣으면 실행가능합니다.

```
 docker container run -it --rm -e DISPLAY=<HOST_IP>:0.0 willypower/streami:latest
```
<br>
<br>
<hr>
<hr>
<br>
<br>

추가사항
---

- 상기에서 언급했듯 개인적으로 네이티브한 Ubuntu 16.04 Host 환경 구축 할 여건이 되지 않아 Ubuntu 18.04 Desktop 으로 테스트해보았습니다.
- git repo 상단에 있는 gif 의 새로고침 속도는 gif 를 위해 속도 제한을 걸지 않은 상태입니다. gif 와 달리 실제 프로그램의 그리드 새로고침 속도는 0.5초로 설정되어 있습니다.
- WSL 에서 16.04 네이티브 환경을 구축하고 그 위에서 Docker 를 구동하고 싶었는데, WSL 내에서의 docker 사용은 windows insider 프리뷰를 구축해야 해서 포기했습니다. ㅠㅠ