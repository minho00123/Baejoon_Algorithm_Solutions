# [Bronze III] 페르시아의 왕들 - 10599 

[문제 링크](https://www.acmicpc.net/problem/10599) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

사칙연산, 구현, 수학

### 문제 설명

<p>Mahya loves to know more about the history of her country. She is in particular interested in the history of the ancient kings of Persia. Recently, Mahya got curious to know how long each of her favorite kings had lived. So, she started searching the web, and collecting information about the kings lives.</p>

<p>Unfortunately, in most cases, the exact dates on which the kings were born or died are not available in resources. So, Mahya could only find some ranges for possible dates of birth and death for each of the kings. For example, for Cyrus the Great, she could only find that the date of birth was between 600 BC and 575 BC, and the date of death was 530 BC. So, she concluded that Cyrus the Great had lived at least 45 years and at most 70 years.</p>

<p>Mahya has created a long list of her favorite kings, and for each king, has written down two ranges showing the birth range and the death range of that king. Since the list is a bit lengthy, she needs your help to process the list, and produce for each king the minimum and the maximum age. Note that if a king was born in year x and died in year y, then he lived y − x years.</p>

### 입력 

 <p>There are multiple test cases in the input. Each test case consists of a line containing four integers a, b, c, d, where −5000 ⩽ a ⩽ b < c ⩽ d ⩽ 2000. The range [a, b] shows the birth range, and [c, d] shows the death range. The input terminates with 0 0 0 0 which should not be processed.</p>

### 출력 

 <p>For each test case, output a line containing the minimum and the maximum age as two integers separated by a space.</p>

