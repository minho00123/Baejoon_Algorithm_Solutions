# [Bronze III] 한다 안한다 - 5789 

[문제 링크](https://www.acmicpc.net/problem/5789) 

### 성능 요약

메모리: 31256 KB, 시간: 124 ms

### 분류

구현, 문자열

### 문제 설명

<p>In the olden days making decisions was easy. One would get a daisy and start to pluck its petals alternating between Do-it and Do-it-Not until the last petal was reached and a decision was made.</p>

<p>Gadget-man wants to use a computerised version. The idea is to work with a random string of zeros and ones. He will pick up two bits, one from each end of the string, and compare them. If they are the same (that is, both ones or both zeros), then it is Do-it. If they differ, then it is Do-it-Not. The two bits are then discarded and the process is repeated on the remaining string until all the bits are picked. The last two bits to be picked will be the decision maker. By the way, the string may be random but it always contains an even number of bits that is greater than zero.</p>

<p>Your task is to write a program that reads a string of zeros and ones and makes the decision for Gadget-man.</p>

### 입력 

 <p>The input starts with an integer N, on a line by itself, that represents the number of test cases. 1 ≤ N ≤ 1000. The description for each test case consists of a string of zeros and ones. There are no blank spaces separating the bits. </p>

### 출력 

 <p>The output consists of a single line, for each test case, which contains a string Do-it or a string Do-it-Not.</p>

