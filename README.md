# Streami BE dev assignment : Park Hyung Seok
Conway's Game of Life 구현

![](Animated GIF-source.gif)


해당 과제를 수행하는데 사용한 스택은 아래와 같습니다.

- Python
    - Tkinter
    - Numpy
- Docker


현재 Native Ubuntu 16.04 환경을 조성할 수 있는 여건이 되지 않아
불가피 하게 Windows Host 위에서 돌아가는 Docker 시스템을 통해 코딩 및 디버깅을 하였습니다.

Xming 소프트웨어를 통하여 GUI 환경을 테스트 했습니다.

<br>
<br>

Overview
---------

이런 고민을 하고 구현했습니다.

1. 어떤 언어를 사용할 것인가?
2. 어떤 GUI 패키지를 사용할 것인가?
3. Docker 를 사용할 것인가? 바로 Host 에서 돌릴 것인가?
4. 알고리즘 구현은 어떤 방식으로 할 것인가?
5. 테스트는 어떻게 할 것인가?

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
   

마지막으로 테스트를 하는 방법에 있어서 조금 애를 먹었습니다.