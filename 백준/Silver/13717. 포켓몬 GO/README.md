# [Silver V] 포켓몬 GO - 13717 

[문제 링크](https://www.acmicpc.net/problem/13717) 

### 성능 요약

메모리: 31120 KB, 시간: 48 ms

### 분류

구현

### 제출 일자

2024년 4월 3일 16:10:11

### 문제 설명

<p style="user-select: auto !important;"><img alt="pokemon_go_logo.png" src="https://upload.acmicpc.net/c2245e53-4103-4412-8d1b-859bbb9776fa/-/preview/" style="user-select: auto !important;"></p>

<p style="user-select: auto !important;">모바일 게임을 즐겨 하는 지우는 <a href="https://halfbrick.com/our-games/jetpack-joyride/" style="user-select: auto !important;">Jetpack Joyride</a> 에 금새 질렸고 <a href="https://www.pokemongo.com/" style="user-select: auto !important;">포켓몬 GO</a>를 시작했다! 이 게임의 재미있는 점은 포켓몬을 진화시킬 수 있다는 것이다.</p>

<p style="user-select: auto !important;">지우가 P<sub style="user-select: auto !important;">i</sub> 라는 포켓몬을 진화시키기 위해서는 해당 포켓몬의 K<sub style="user-select: auto !important;">i</sub> 개의 사탕이 필요하다. 진화가 된 후에는 2개의 사탕을 돌려받는다.</p>

<p style="user-select: auto !important;">각 포켓몬은 그들 종의 사탕으로만 진화할 수 있다.</p>

<p style="user-select: auto !important;">지우는 N종의 포켓몬이 있고 P<sub style="user-select: auto !important;">i</sub> 라는 포켓몬의 사탕은 M<sub style="user-select: auto !important;">i</sub> 개를 가지고 있으며 지우는 진화시킬 수 있는 포켓몬의 총 마리수를 궁금해한다.</p>

<p style="user-select: auto !important;">또한, 지우는 가장 많이 진화시킬 수 있는 포켓몬이 무엇인지 알고 싶어한다. 만약 그런 포켓몬들이 여러 종이 있다면 도감번호가 가장 작은 포켓몬을 출력한다. 즉, 입력 데이터에서 더 먼저 나타나는 포켓몬을 출력하면 된다. </p>

### 입력 

 <p style="user-select: auto !important;">첫 번째 줄에는 포켓몬의 종류 수를 나타내는 N (1 ≤ N ≤ 70)이 주어진다.</p>

<p style="user-select: auto !important;">그 다음 2N 줄에는 N개의 데이터 세트가 입력되는데</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">2i 번째 줄에는 i번째 포켓몬의 이름을 나타내는 최대길이 20의 P<sub style="user-select: auto !important;">i</sub> 문자열이 주어진다.</li>
	<li style="user-select: auto !important;">2i + 1 번째 줄에는 K<sub style="user-select: auto !important;">i</sub>  (12 ≤ K<sub style="user-select: auto !important;">i</sub> ≤ 400) , M<sub style="user-select: auto !important;">i</sub> (1 ≤ M<sub style="user-select: auto !important;">i</sub> ≤ 10<sup style="user-select: auto !important;">4</sup>) 가 주어지는데 각각 i 번째 포켓몬이 진화에 필요한 사탕의 수와 지우가 가지고 있는 i 번째 포켓몬의 총 사탕의 수이다.</li>
</ul>

### 출력 

 <p style="user-select: auto !important;">첫 번째 줄엔 진화시킬 수 있는 포켓몬의 총 마리수를 출력한다.</p>

<p style="user-select: auto !important;">두 번째 줄엔 가장 많이 진화시킬 수 있는 포켓몬의 이름을 출력한다.</p>

