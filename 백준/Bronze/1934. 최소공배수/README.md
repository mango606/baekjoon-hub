# [Bronze I] 최소공배수 - 1934 

[문제 링크](https://www.acmicpc.net/problem/1934) 

### 성능 요약

메모리: 115692 KB, 시간: 868 ms

### 분류

유클리드 호제법, 수학, 정수론

### 문제 설명

<p>두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.</p>

<p>두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)</p>

### 출력 

 <p>첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.</p>

# 풀이1
math.lcm 함수를 사용했다. 맞았다.
```
import math

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
```
# 풀이2
set을 사용해서 풀었다. VCS에서는 잘 실행되는데 시간 초과가 뜬다.
```
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    x = {i for i in range(a, a*b+1, a)} # set(집합), List Comprehension
    y = {j for j in range(b, a*b+1, b)}

    print(min(x&y)) # 교집합의 최소값
```
# 풀이3
이것도 될 줄 알았는데, 시간 초과가 뜬다. 그런데 PyPy3로 제출하니까 맞았다. (풀이1이 덮어쓰기가 되어 현재 코드가 풀이3이 되었다.)
```
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    for i in range (1, b+1):
        if (a*i % b == 0):
            print(a*i)
            break
```
# 내 제출
![image](https://github.com/mango606/baekjoon-hub/assets/75062110/dc0711e9-66d0-4730-af91-4d15834f7059)
