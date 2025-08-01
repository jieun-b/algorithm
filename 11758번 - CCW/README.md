# 11758번: CCW - <img src="https://static.solved.ac/tier_small/11.svg" style="height:20px" /> Gold V

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/11758)

<p>2차원 좌표 평면 위에 있는 점 3개 P<sub>1</sub>, P<sub>2</sub>, P<sub>3</sub>가 주어진다. P<sub>1</sub>, P<sub>2</sub>, P<sub>3</sub>를 순서대로 이은 선분이&nbsp;어떤 방향을 이루고 있는지 구하는 프로그램을 작성하시오.</p>

## 입력

<p>첫째 줄에 P<sub>1</sub>의 (x<sub>1</sub>, y<sub>1</sub>), 둘째 줄에 P<sub>2</sub>의 (x<sub>2</sub>, y<sub>2</sub>), 셋째 줄에 P<sub>3</sub>의 (x<sub>3</sub>, y<sub>3</sub>)가 주어진다. (-10,000 ≤ x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, y<sub>2</sub>, x<sub>3</sub>, y<sub>3</sub> ≤ 10,000) 모든 좌표는 정수이다. P<sub>1</sub>, P<sub>2</sub>, P<sub>3</sub>의 좌표는 서로 다르다.</p>

## 출력

<p>P<sub>1</sub>, P<sub>2</sub>, P<sub>3</sub>를 순서대로 이은 선분이 반시계 방향을 나타내면 1, 시계 방향이면 -1, 일직선이면 0을 출력한다.</p>

## 소스코드

[소스코드 보기](CCW.py)