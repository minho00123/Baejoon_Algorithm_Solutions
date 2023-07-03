# [Bronze III] 완전 세제곱 - 4690 

[문제 링크](https://www.acmicpc.net/problem/4690) 

### 성능 요약

메모리: 31256 KB, 시간: 2040 ms

### 분류

브루트포스 알고리즘, 구현, 수학

### 문제 설명

<p>For hundreds of years Fermat's Last Theorem, which stated simply that for n > 2 there exist no integers a, b, c > 1 such that a<sup>n</sup> = b<sup>n</sup> + c<sup>n</sup> , has remained elusively unproven. (A recent proof is believed to be correct, though it is still undergoing scrutiny.) It is possible, however, to find integers greater than 1 that satisfy the "perfect cube" equation a<sup>3</sup> = b<sup>3</sup> + c<sup>3</sup> + d<sup>3</sup> (e.g. a quick calculation will show that the equation 12<sup>3</sup> = 6<sup>3</sup> + 8<sup>3</sup> + 10<sup>3</sup> is indeed true). This problem requires that you write a program to find all sets of numbers {a, b, c, d} which satisfy this equation for a ≤ 100.</p>

### 입력 

 Empty

### 출력 

 <p>The output should be listed as shown below, one perfect cube per line, in non-decreasing order of a (i.e. the lines should be sorted by their a values). The values of b, c, and d should also be listed in non-decreasing order on the line itself. There do exist several values of a which can be produced from multiple distinct sets of b, c, and d triples. In these cases, the triples with the smaller b values should be listed first.</p>

<p>Note: The programmer will need to be concerned with an efficient implementation. The official time limit for this problem is 2 minutes, and it is indeed possible to write a solution to this problem which executes in under 2 minutes on a 33 MHz 80386 machine. Due to the distributed nature of the contest in this region, judges have been instructed to make the official time limit at their site the greater of 2 minutes or twice the time taken by the judge's solution on the machine being used to judge this problem.</p>

