# [Bronze III] 얼마? - 9325 

[문제 링크](https://www.acmicpc.net/problem/9325) 

### 성능 요약

메모리: 31256 KB, 시간: 1824 ms

### 분류

사칙연산, 수학

### 문제 설명

<p>This ﬁnancial crisis! Even MI6’s technology department does not escape the consequences. With all those constraints on the budget, how can R be expected to supply our spies with cars equipped with all the technological gadgets and weaponry they need to save the world? As if it is not hard enough to put all those tracking systems, oil sprayers, guns, bullets and missiles in one car, now R has to worry about the costs as well.</p>

<p>The management insists, though: before R is allowed to order a car and all the parts he needs, he will ﬁrst need to determine the exact amount of money that he needs. Management will then decide whether he gets to realize his vision or not.</p>

<p>This sort of bureaucratic nonsense is not something that R wants to waste any time on. He therefore wants you to help him. Given the price of the car, a listing of the parts R wants to install, and the price per piece of each part, work out what the total cost is of the project.</p>

### 입력 

 <p>On the ﬁrst line one positive number: the number of test cases, at most 100. After that per test case:</p>

<ul>
	<li>one line with an integer s (1 ≤ s ≤ 100 000): the stock price of the car.</li>
	<li>one line with an integer n (0 ≤ n ≤ 1 000): the number of different parts to be installed.</li>
	<li>n lines with two space-separated integers q<sub>i</sub> and p<sub>i</sub> (1 ≤ q<sub>i</sub> ≤ 100 and 1 ≤ p<sub>i</sub> ≤ 10 000): for each different part i, the number of pieces q<sub>i</sub> required of such part, and the price p<sub>i</sub> for a single piece.</li>
</ul>

### 출력 

 <p>Per test case:</p>

<ul>
	<li>one line with an integer: the total amount of money needed to buy the car and all the parts.</li>
</ul>

