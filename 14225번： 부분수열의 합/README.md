# 14225번: 부분수열의 합 - <img src="https://static.solved.ac/tier_small/10.svg" style="height:20px" /> Silver I

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/14225)


<p>수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오.</p>

<p>예를 들어, S = [5, 1, 2]인 경우에 1, 2, 3(=1+2), 5, 6(=1+5), 7(=2+5), 8(=1+2+5)을 만들 수 있다. 하지만, 4는 만들 수 없기 때문에 정답은 4이다.</p>



## 입력


<p>첫째 줄에 수열 S의 크기 N이 주어진다. (1 ≤ N ≤ 20)</p>

<p>둘째 줄에는 수열 S가 주어진다. S를 이루고있는 수는 100,000보다 작거나 같은 자연수이다.</p>



## 출력


<p>첫째 줄에&nbsp;수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 출력한다.</p>



## 소스코드

[소스코드 보기](부분수열의%20합.py)