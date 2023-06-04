# [Bronze III] Viva la Diferencia - 4084 

[문제 링크](https://www.acmicpc.net/problem/4084) 

### 성능 요약

메모리: 31256 KB, 시간: 184 ms

### 분류

사칙연산, 구현, 수학, 시뮬레이션

### 문제 설명

<p>Take any four positive integers: a, b, c, d. Form four more, like this: </p>

<p>|a-b| |b-c| |c-d| |d-a|</p>

<p>That is, take the absolute value of the differences of a with b, b with c, c with d, and d with a. (Note that a zero could crop up, but they’ll all still be non-negative.) Then, do it again with these four new numbers. And then again. And again. Eventually, all four integers will be the same. For example, start with 1,3,5,9:</p>

<p>1 3 5 9 <br>
2 2 4 8 (1)<br>
0 2 4 6 (2)<br>
2 2 2 6 (3)<br>
0 0 4 4 (4)<br>
0 4 0 4 (5)<br>
4 4 4 4 (6)</p>

<p>In this case, the sequence converged in 6 steps. It turns out that in all cases, thesequence converges very quickly. In fact, it can be shown that if all four integers are less than 2n, then it will take no more than 3*n steps to converge!</p>

<p>Given a, b, c and d, figure out just how quickly the sequence converges.</p>

### 입력 

 <p>There will be several test cases in the input. Each test case consists of four positive integers on a single line (1 ≤ a,b,c,d ≤ 2,000,000,000), with single spaces for separation. The input will end with a line with four 0s.</p>

### 출력 

 <p>For each test case, output a single integer on its own line, indicating the number of steps until convergence. Output no extra spaces, and do not separate answers with blank lines.</p>

