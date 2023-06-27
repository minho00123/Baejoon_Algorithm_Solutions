# [Bronze III] 암호제작 - 1837 

[문제 링크](https://www.acmicpc.net/problem/1837) 

### 성능 요약

메모리: 31256 KB, 시간: 260 ms

### 분류

임의 정밀도 / 큰 수 연산, 브루트포스 알고리즘, 수학

### 문제 설명

<p><img alt="" src="https://www.acmicpc.net/JudgeOnline/upload/201006/Screen%20shot%202010-06-11%20at%204_48_42%20PM.png" style="float:right; height:244px; width:291px">The young and very promising cryptographer Odd Even has implemented the security module of a large system with thousands of users, which is now in use in his company. The cryptographic keys are created from the product of two primes, and are believed to be secure because there is no known method for factoring such a product effectively.</p>

<p>What Odd Even did not think of, was that both factors in a key should be large, not just their product. It is now possible that some of the users of the system have weak keys. In a desperate attempt not to be ﬁred, Odd Even secretly goes through all the users keys, to check if they are strong enough. He uses his very poweful Atari, and is especially careful when checking his boss’ key.</p>

### 입력 

 <p>The first line contains two integers 4 ≤ K ≤ 10<sup>100</sup> and 2 ≤ L ≤ 10<sup>6</sup>. K is the key itself, a product of two primes. L is the wanted minimum size of the factors in the key.</p>

### 출력 

 <p>For number K, if one of its factors are strictly less than the required L, your program should output “BAD p”, where p is the smallest factor in K. Otherwise, it should output “GOOD”.</p>

