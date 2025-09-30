# 6987번: 월드컵 - <img src="https://static.solved.ac/tier_small/12.svg" style="height:20px" /> Gold IV

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/6987)


<p>월드컵 조별 최종 예선에서는 6개국으로 구성된 각 조별로 동일한 조에 소속된 국가들과 한 번씩, 각 국가별로 총 5번의 경기를 치른다. 조별리그가 끝난 후, 기자가 보내온 각 나라의 승, 무승부, 패의 수가 가능한 결과인지를 판별하려고 한다. 다음은 가능한 결과와 가능하지 않은 결과의 예이다.</p>

<table class="table table-bordered" style="width: 100%;">
<tbody>
<tr>
<td style="text-align: center; width: 25%;">
<table class="table table-bordered td-center th-center">
<thead>
<tr>
<th>나라</th>
<th>승</th>
<th>무</th>
<th>패</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>5</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>B</td>
<td>3</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td>C</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td>D</td>
<td>0</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td>E</td>
<td>4</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>F</td>
<td>1</td>
<td>0</td>
<td>4</td>
</tr>
</tbody>
</table>
</td>
<td style="text-align: center; width: 25%;">
<table class="table table-bordered td-center th-center">
<thead>
<tr>
<th>나라</th>
<th>승</th>
<th>무</th>
<th>패</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>4</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>B</td>
<td>3</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td>C</td>
<td>4</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>D</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td>E</td>
<td>0</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td>F</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
</tbody>
</table>
</td>
<td style="text-align: center; width: 25%;">
<table class="table table-bordered td-center th-center">
<thead>
<tr>
<th>나라</th>
<th>승</th>
<th>무</th>
<th>패</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>5</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>B</td>
<td>4</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>C</td>
<td>2</td>
<td>2</td>
<td>1</td>
</tr>
<tr>
<td>D</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td>E</td>
<td>1</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td>F</td>
<td>0</td>
<td>0</td>
<td>5</td>
</tr>
</tbody>
</table>
</td>
<td style="text-align: center; width: 25%;">
<table class="table table-bordered td-center th-center">
<thead>
<tr>
<th>나라</th>
<th>승</th>
<th>무</th>
<th>패</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>5</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>B</td>
<td>3</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>C</td>
<td>2</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>D</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td>E</td>
<td>0</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td>F</td>
<td>1</td>
<td>0</td>
<td>4</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
<tfoot>
<tr>
<th style="text-align: center; width: 25%;">예제 1 가능한 결과</th>
<th style="text-align: center; width: 25%;">예제 2 가능한 결과</th>
<th style="text-align: center; width: 25%;">예제 3 불가능한 결과</th>
<th style="text-align: center; width: 25%;">예제 4 불가능한 결과</th>
</tr>
</tfoot>
</table>

<p>네 가지의 결과가 주어질 때 각각의 결과에 대하여 가능하면 1, 불가능하면 0을 출력하는 프로그램을 작성하시오.</p>



## 입력


<p>첫째 줄부터 넷째 줄까지 각 줄마다 6개국의 결과가 나라별로 승, 무승부, 패의 순서로 빈칸을 하나 사이에 두고 18개의 숫자로 주어진다. 승, 무, 패의 수는 6보다 작거나 같은 자연수 또는 0이다.</p>



## 출력


<p>입력에서 주어진 네 가지 결과에 대하여 가능한 결과는 1, 불가능한 결과는 0을 빈칸을 하나 사이에 두고 출력한다.</p>



## 소스코드

[소스코드 보기](월드컵.py)