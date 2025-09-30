# 1189번: 컴백홈 - <img src="https://static.solved.ac/tier_small/10.svg" style="height:20px" /> Silver I

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/1189)


<p>한수는 캠프를 마치고 집에 돌아가려 한다. 한수는 현재 왼쪽 아래점에 있고 집은 오른쪽 위에 있다. 그리고 한수는 집에 돌아가는 방법이 다양하다. 단, 한수는 똑똑하여 한번 지나친 곳을 다시 방문하지는 않는다.</p>

<pre>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cdef&nbsp; ...f&nbsp; ..ef&nbsp; ..gh&nbsp; cdeh&nbsp; cdej&nbsp; ...f&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bT..&nbsp; .T.e&nbsp; .Td.&nbsp; .Tfe&nbsp; bTfg&nbsp; bTfi&nbsp; .Tde&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a...&nbsp; abcd&nbsp; abc.&nbsp; abcd&nbsp; a...&nbsp; a.gh&nbsp; abc.&nbsp;
거리 :&nbsp; 6&nbsp;&nbsp;&nbsp;&nbsp; 6&nbsp;&nbsp;&nbsp;&nbsp; 6&nbsp;&nbsp;&nbsp;&nbsp; 8&nbsp;&nbsp;&nbsp;&nbsp; 8&nbsp;&nbsp;&nbsp; 10&nbsp;&nbsp;&nbsp; 6</pre>

<p>위 예제는 한수가 집에 돌아갈 수 있는 모든 경우를 나타낸 것이다. T로 표시된 부분은 가지 못하는 부분이다. 문제는 R x C 맵에 못가는 부분이 주어지고 거리 K가 주어지면 한수가 집까지도 도착하는 경우 중 거리가 K인 가짓수를 구하는 것이다.</p>



## 입력


<p>첫 줄에 정수 R(1 ≤ R ≤ 5), C(1 ≤ C ≤ 5), K(1 ≤ K ≤ R×C)가 공백으로 구분되어 주어진다. 두 번째부터 R+1번째 줄까지는 R×C 맵의 정보를 나타내는 '.'과 'T'로 구성된 길이가 C인 문자열이 주어진다.</p>



## 출력


<p>첫 줄에 거리가 K인 가짓수를 출력한다.</p>



## 소스코드

[소스코드 보기](컴백홈.py)