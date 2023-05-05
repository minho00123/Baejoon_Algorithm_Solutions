# [Bronze III] 집 주소 - 1284 

[문제 링크](https://www.acmicpc.net/problem/1284) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

### 분류

사칙연산, 구현, 수학

### 문제 설명

<p>As the manufacturer of holders for door numbers, you have to know how wide to make them based on the house number each of your customers supplies. Fortunately, all house numbers in your area use exactly the same style of digit, so the calculation is quite easy. Most digits are exactly 3 cm wide, but there is a slight complication in that a 0 is 4 cm wide and a 1 is only 2 cm wide. Also, you have to remember to leave a 1 cm gap between digits, and a 1 cm border at the start and end of the number.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/1284/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-01-12%20%EC%98%A4%EC%A0%84%208.26.11.png" style="height:121px; width:213px"></p>

<p>As you can see from the diagram, a customer who lives at number 120 will need a 13 cm wide holder—4 cm for the border and gaps, 2 cm for the 1, 3 cm for the 2 and 4 cm for the 0. 4 + 2 + 3 + 4 = 13.</p>

### 입력 

 <p>Input for this problem is a series of street numbers (integers between 1 and 9999 inclusive), each on a line of its own. The last number will be 0 and should not be processed.</p>

### 출력 

 <p>For each input line with a non-zero house number, output a line containing a single integer, the width in cm of the required holder for that street number.</p>

